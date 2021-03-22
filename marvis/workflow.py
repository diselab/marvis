"""Allow fault-injection by executing a sequence of instructions."""

import logging
import threading

from aexpr import aexpr

logger = logging.getLogger(__name__)


class Workflow:
    """A workflow is a contains a list of commands for planned execution during the simulation.

    This is based on the work of Arne Boockmeyer's
    `dasylab-testbed <https://gitlab.hpi.de/arne.boockmeyer/dasylab-testbed/>`_.

    Note
    ----
    Every :class:`Workflow` creates a thread.

    Example
    -------
    Please use it with a decorator provided by the :class:`.Scenario`:

    .. code-block:: python

        @scenario.workflow
        def workflow_function_name(workflow):
            do_something()
            workflow.sleep(5)
            do_another_thing()

    Parameters
    ----------
    task : callable
        The function to be executed in the workflow.
    """
    def __init__(self, task):
        #: An event indicating when to stop the workflow thread.
        self.stop_event = threading.Event()
        #: These events are waiting on some condition to come true.
        self.current_waiting_events = []
        #: The function being executed by the workflow thread.
        self.task = task

    def stop(self):
        """Stop the workflow.

        **Warning:** Do not call this manually. This is done by the :class:`.Simulation`.
        """
        logger.debug('Stopping workflow.')
        self.stop_event.set()
        for event in self.current_waiting_events:
            event.set()

    def start(self):
        """Start the workflow.

        **Warning:** Do not call this manually. This is done by the :class:`.Simulation`.
        """
        thread = threading.Thread(target=self.task, args=(self,))
        thread.start()

    def __stopped(self):
        raise Exception('Simulation stopped')

    def __check_stop(self):
        if self.stop_event.is_set():
            self.__stopped()

    def sleep(self, duration):
        """Sleep and wait.

        Parameters
        ----------
        duration : float
            The duration to sleep in seconds.
        """
        logger.debug('Sleep for %gs.', duration)
        close = self.stop_event.wait(duration)
        logger.debug('Slept for %ds or stopped.', duration)
        if close is True:
            self.__stopped()

    def wait_until(self, expression, expected_result, global_variables, local_variables):
        """Wait until an expression is equal to a specific value.

        Like :func:`sleep` this is a blocking call.

        Parameters
        ----------
        expression
            The expression to evaluate.
            **Warning:** not all expressions are supported.
            See https://github.com/active-expressions/active-expressions-static-python for further infos.
        expected_result
            The value to compare againt.
        global_variables
            In order to work properly, you need to pass the global variable space with :code:`globals()`.
        local_variables
            In order to work properly, you need to pass the global variable space with :code:`locals()`.
        """
        logger.debug('Waiting for condition.')
        wait_event = threading.Event()
        aexpr(expression, global_variables, local_variables)\
            .on_change(lambda obs, old, new: wait_event.set() if new == expected_result else None)
        self.current_waiting_events.append(wait_event)
        wait_event.wait()
        self.current_waiting_events.remove(wait_event)
        logger.debug('Finished waiting for condition.')
        self.__check_stop()

    def wait_until_true(self, expression, global_variables, local_variables):
        """Wait until an expression is equal to True.

        Like :func:`sleep` this is a blocking call.

        Parameters
        ----------
        expression
            The expression to evaluate.
            **Warning:** not all expressions are supported.
            See https://github.com/active-expressions/active-expressions-static-python for further infos.
        global_variables
            In order to work properly, you need to pass the global variable space with :code:`globals()`.
        local_variables
            In order to work properly, you need to pass the global variable space with :code:`locals()`.
        """
        logger.debug('Waiting for condition to come true.')
        self.wait_until(expression, True, global_variables, local_variables)
