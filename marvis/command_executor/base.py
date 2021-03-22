"""Base abstract class for a node."""

import logging

logger = logging.getLogger(__name__)

class CommandExecutor:
    """The CommandExecutor abstracts away the code for running
        code on a Node.

    Parameters
    ----------
    name : str
        You can specify a name for logging purposes.
    """

    def __init__(self, name='unnamed'):
        #: The name of the CommandExecutor.
        self.name = name
        #: A counter for loggers.
        self.counter = 0

    def get_logger(self):
        """Retrieve the logger for this command executor."""
        num = self.counter
        self.counter += 1
        return logging.getLogger(self.name).getChild(str(num))

    def execute(self, command, user=None, shell=None, stdout_logfile=None, stderr_logfile=None):
        """Execute a command.

        Parameters
        ----------
        command : str
            The command to run.
        user : str
            The user to run the command as.
        shell : str
            The type of shell to use (:code:`sh`, :code:`bash`, ...).
        stdout_logfile : str
            The path to the log file to append the stdout output.
        stderr_logfile : str
            The path to the log file to append the stderr output.
        """
        raise NotImplementedError

class ExitCode(Exception):
    """An ExitCode is a container for storing a commands exit code.

    Parameters
    ----------
    code
        The exit code.
    command
        The command that was executed.
    """

    def __init__(self, code: int, command: str):
        super().__init__(code)
        self.code = code
        self.command = command
