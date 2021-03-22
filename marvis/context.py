"""Contexts to tear down the simulation."""

import logging
import collections
import threading

logger = logging.getLogger(__name__)


class ThreadLocalStack:

    def __init__(self):
        self.data = threading.local()

    @property
    def stack(self):
        if not hasattr(self.data, 'stack'):
            self.data.stack = []
        return self.data.stack

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None


class Context:
    """A context can be used for deferring function calls.

    In this project, it is used for deferring teardowns of the simulation.

    You can use it like this:

    .. code-block:: python

        with SimpleContext() as ctx:
            defer('Call afunction', afunction, args)
            defer('Call another function', anotherfunction, args)
            ctx.cleanup()
    """
    __stack = ThreadLocalStack()

    @staticmethod
    def current():
        """Return the current context."""
        return Context.__stack.top()

    def __init__(self):
        #: The number of failed cleanups.
        self.fails = 0

    def defer(self, item):
        """Store a :class:`.DeferredItem` for running it later.

        Parameters
        ----------
        item : :class:`.DeferredItem`
            The function to execute later.
        """
        raise NotImplementedError

    def cancel(self, item):
        """Cancel a specific item of the current context.

        Parameters
        ----------
        item : :class:`.DeferredItem`
            The function to cancel.
        """
        raise NotImplementedError

    def cleanup(self):
        """Do whatever is needed to cleanup the context."""
        raise NotImplementedError

    def add_error(self, err: Exception):  # pylint: disable=unused-argument
        """Add an error (to be implemented)."""
        self.fails += 1

    def __enter__(self):
        Context.__stack.push(self)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        assert Context.__stack.pop() is self, 'Invalid context stack, not the same number of push and pop operations'

class DeferredItem:
    """A DeferredItem is used for storing functions calls that need to be executed later on.

    Parameters
    ----------
    ctx
        The context the item belongs to.
    name
        A name for this item (for logging purposes).
    func
        The function to defer.
    args : list
        The positional arguments to be passed to the function.
    kwargs : dict
        The keyword arguments to be passed to the function.
    """
    def __init__(self, ctx: Context, name: str, func: callable, args, kwargs):
        #: The context to execute this item in.
        self.ctx = ctx
        #: The name of the item (and description).
        self.name = name
        #: The callable.
        self.func = func
        #: (Positional) Arguments to be passed to the callable.
        self.args = args
        #: Keyword arguments to be passed to the callable.
        self.kwargs = kwargs

    def cancel(self):
        """Cancel the execution of the item."""
        self.ctx.cancel(self)

    def cleanup(self):
        """Execute the function call."""
        try:
            self.func(*self.args, **self.kwargs)
        except Exception as err: # pylint: disable=broad-except
            logger.error('Failed to cleanup deferred item %s: %s', self.name, err)
            self.ctx.add_error(err)

    def __str__(self):
        return self.name

def defer(name, func, *args, **kwargs):
    """Defer a function call.

    The function call be assigned to the current context.

    Parameters
    ----------
    func : callable
        The function to execute.
    """
    if name is None:
        name = func.__qualname__

    ctx = Context.current()
    if ctx is None:
        logging.warning('No context available to defer %s', name)
        ctx = NoContext()

    item = DeferredItem(ctx, name, func, args, kwargs)
    ctx.defer(item)
    return item

class NoContext(Context):
    """The NoContext is a Null-Object and therefore **does nothing**.

    It does not do any cleanups. This is useful if you do not want your simulated
    containers to be torn down.
    """

    def defer(self, item):
        pass

    def cancel(self, item):
        pass

    def cleanup(self):
        pass

class SimpleContext(Context):
    """The simple context executes deferred items like it is intented."""
    def __init__(self):
        super().__init__()
        ## The deque, the DeferredItems are stored in.
        self.dequeue = collections.deque()

    def defer(self, item):
        logger.debug('Added deferred item: %s', item)
        self.dequeue.appendleft(item)

    def cancel(self, item):
        logger.debug('Removed deferred item: %s', item)
        self.dequeue.remove(item)

    def cleanup(self):
        logger.info('Cleanup %d items', len(self.dequeue))
        while self.dequeue:
            item = self.dequeue.popleft()
            logger.debug('Cleanup deferred item: %s', item)
            item.cleanup()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        super().__exit__(exc_type, exc_value, exc_traceback)
        self.cleanup()
