"""Null-Object for dry runs."""

from . import util
from .base import CommandExecutor

class ConsoleCommandExecutor(CommandExecutor):
    """The ConsoleCommandExecutor just prints out the commands to be executed.

    It resembles some kind of Null-Object, useful for debugging purposes.
    """

    def execute(self, command, user=None, shell=None, stdout_logfile=None, stderr_logfile=None):
        logger = self.get_logger()
        msg = 'Execute the following command'
        if user is not None:
            msg = f'{msg} as user {user}'
        if shell is not None:
            msg = f'{msg} in a {shell} shell'
        logger.warning('%s:\n  %s', msg, util.stringify_shell_arguments(command))
