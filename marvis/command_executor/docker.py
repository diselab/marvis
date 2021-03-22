"""Execute commands in docker containers."""
import logging
from docker.models.containers import Container
from docker.utils.socket import frames_iter_no_tty

from . import util
from .base import CommandExecutor

class DockerCommandExecutor(CommandExecutor):
    """The DockerCommandExecutor runs commands in a Docker container.

    Parameters
    ----------
    name : str
        The name of the command executor.
    container : str
        The container to run the commands in.
    """

    def __init__(self, name, container: Container):
        super().__init__(name)
        #:The container to run the commands in.
        self.container = container

    def execute(self, command, user=None, shell=None, stdout_logfile=None, stderr_logfile=None):
        if shell is not None:
            command = [shell, '-c', util.stringify_shell_arguments(command)]

        logger = self.get_logger()
        logger.debug('%s', command)

        (_, socket) = self.container.exec_run(command, user=user, socket=True)

        with util.LogFile(logger, stdout_logfile) as outlog, util.LogFile(logger, stderr_logfile) as errlog:
            for (stream, data) in frames_iter_no_tty(socket):
                level = logging.WARNING
                if stream == 1:
                    level = logging.INFO
                if stream == 2:
                    level = logging.ERROR
                for line in data.decode('utf8').rstrip().splitlines():
                    if stream == 1:
                        outlog.log(level, line)
                    else:
                        errlog.log(level, line)
