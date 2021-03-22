"""Execute commands in LXD containers."""
import logging
from pylxd.models import Container

from . import util
from .base import CommandExecutor, ExitCode

def create_handler(log, level):
    def handler(line):
        log.log(level, line)
    return handler

class LXDCommandExecutor(CommandExecutor):
    """The LXDCommandExecutor runs commands in a LXD container.

    name : str
        The name of the command executor.
    container : str
        The container to run the commands in.
    """

    def __init__(self, name, container: Container):
        super().__init__(name)
        #: The container to run the commands in.
        self.container = container

    def execute(self, command, user=None, shell=None, stdout_logfile=None, stderr_logfile=None):
        command = util.apply_user_and_shell(command, user=user, shell=shell)
        command = util.split_shell_arguments(command)

        logger = self.get_logger()
        logger.debug('%s', command)

        with util.LogFile(logger, stdout_logfile) as stdout_log, \
            util.LogFile(logger, stderr_logfile) as stderr_log:

            (code, _, _) = self.container.execute(
                command,
                stdout_handler=create_handler(stdout_log, logging.INFO),
                stderr_handler=create_handler(stderr_log, logging.ERROR))

            logger.debug('Exit code: %s', code)
            if code != 0:
                raise ExitCode(code, command)
