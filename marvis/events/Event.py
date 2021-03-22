import ns.core
import queue
from threading import Thread
from time import sleep
from aexpr import aexpr
import subprocess


def event():
    return Event()


def e():
    return event()


events_on_simulation_end = []


def execute_events_on_simulation_end():
    for event_to_exec in events_on_simulation_end:
        event_to_exec.start()


class Event(object):

    def __init__(self):
        self.queue = queue.Queue()

    def after(self, seconds):
        ep = EventPart()
        ep.type = "after"
        ep.seconds = seconds
        self.queue.put(ep)
        return self

    def when(self, condition, result, global_vars, local_vars):
        ep = EventPart()
        ep.type = "when"
        ep.condition = condition
        ep.result = result
        ep.globals = global_vars
        ep.locals = local_vars
        self.queue.put(ep)
        return self

    def check_if(self, command=None, return_code=-1, lambda_expr=None, return_value=None, every=-1):
        ep = EventPart()
        ep.type = "check_if"
        ep.command = command
        ep.return_code = return_code
        ep.lambda_expr = lambda_expr
        ep.return_value = return_value
        ep.seconds = every
        self.queue.put(ep)
        return self

    def execute(self, expression):
        ep = EventPart()
        ep.type = "execute"
        ep.expression = expression
        self.queue.put(ep)
        return self

    def start(self):
        thread = Thread(target=event_worker, args=(self.queue,))
        thread.daemon = True
        thread.start()

    def s(self):
        self.start()

    def start_on_simulation_start(self):
        ns.core.Simulator.Schedule(ns.core.Seconds(0), self.start)

    def start_on_simulation_end(self):
        events_on_simulation_end.append(self)


def event_worker(queue):
    def exec_after(event_part):
        sleep(event_part.seconds)

    def exec_when(event_part):
        aexpr(event_part.condition, event_part.globals, event_part.locals)\
            .on_change(lambda obs, old, new: process() if new == event_part.result else None)

    def exec_check_if(event_part):
        if event_part.command is not None and event_part.lambda_expr is not None:
            print("In check-if is not possible to have a command and a "
                  "lambda-expression at the same time. Aborting execution")
        elif event_part.command is not None:
            return_code = subprocess.call(event_part.command, shell=True)
            if event_part.seconds == -1:
                if return_code == event_part.return_code:
                    process()
            else:
                while return_code is not event_part.return_code:
                    sleep(event_part.seconds)
                    return_code = subprocess.call(event_part.command, shell=True)
                process()
        elif event_part.lambda_expr is not None:
            return_value = event_part.lambda_expr()
            if event_part.seconds == -1:
                if return_value == event_part.return_value:
                    process()
            else:
                while return_value is not event_part.return_value:
                    sleep(event_part.seconds)
                    return_value = event_part.lambda_expr()
                process()
        else:
            print("check-if has neither a command nor a lambda_expr. Aborting execution")

    def exec_execute(event_part):
        event_part.expression()

    def process():
        while not queue.empty():
            cur_elem = queue.get()
            if cur_elem.type is "after":
                exec_after(cur_elem)
            if cur_elem.type is "when":
                exec_when(cur_elem)
                break
            if cur_elem.type is "check_if":
                exec_check_if(cur_elem)
                break
            if cur_elem.type is "execute":
                exec_execute(cur_elem)
    process()


class EventPart(object):

    def __init__(self):
        self.seconds = -1
        self.condition = None
        self.globals = None
        self.locals = None
        self.result = None
        self.command = None
        self.return_code = -1
        self.lambda_expr = None
        self.return_value = None
        self.expression = None
        self.type = None  # "after", "when", "check_if" or "execute
