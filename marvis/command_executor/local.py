"""Execute commands on the simulation host."""
import logging
import subprocess
import threading

from . import util
from .base import CommandExecutor, ExitCode

def log_file(logger, level, file, logfile):
    with file, util.LogFile(logger, logfile) as log:
        for line in file:
            log.log(level, line.rstrip())

class LocalCommandExecutor(CommandExecutor):
    """The LocalCommandExecutor runs commands on the simulation host.

    *Warning:* This raises an execption if something goes wrong.
    Be sure to catch it or the simulation will stop.
    """

    def __init__(self, name=None):
        super().__init__(name)

    def execute(self, command, user=None, shell=None, stdout_logfile=None, stderr_logfile=None):
        if user is not None:
            raise ValueError('LocalCommandExecutor does not implement user argument')
        if stdout_logfile is not None or stderr_logfile is not None:
            raise ValueError('LocalCommandExecutor does not implement logfiles')

        if user is not None:
            command = util.apply_user_and_shell(command, user=user, shell=shell)
            shell = None

        logger = self.get_logger()
        logger.debug('%s', command)
        process = subprocess.Popen( # pylint: disable=subprocess-run-check
            command,
            shell=False if shell is None else shell,
            encoding='utf8',
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out_thread = threading.Thread(target=log_file, args=(logger, logging.INFO, process.stdout, stdout_logfile))
        err_thread = threading.Thread(target=log_file, args=(logger, logging.ERROR, process.stderr, stderr_logfile))

        out_thread.start()
        err_thread.start()

        code = process.wait()
        out_thread.join()
        err_thread.join()

        if code != 0:
            raise ExitCode(code, command)
