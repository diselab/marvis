"""Argument parsing for the simulation."""

import argparse
import logging

class ArgumentParser(argparse.ArgumentParser):
    """A simple-to-use argument parser for log levels.

    ArgumentParser by default defines the `--verbose` and `--log-level` flag.
    It is used to abstract these flags away and prevent repetition in the example scenarios.
    `--verbose` sets the overall log level to `DEBUG`.
    Valid options for log-level are `INFO` and `DEBUG`.

    Parameters
    ----------
    logger : str
        The name of the logger argument to pass to the main function.
    """

    def run(self, main, setup_logging=True, logger_arg=None):
        """Parse the arguments and pass them to a function to be called afterwards

        Parameters
        ----------
        main : callable
            The function to call and to pass the arguments to.
        setup_logging : bool
            Whether to set up logging with the default python logger and parse log levels.
        logger_arg : string
            The name of the argument to pass the logger to the :code:`main` function.
        """
        marvis_name = __name__.rsplit('.', 1)[0]

        if setup_logging:
            default = 'INFO'
            self.add_argument('-v', '--verbose', action='store_const', const='DEBUG', default=default,
                              help=f'enable verbose logging for the {marvis_name} logger', dest='log_level')
            self.add_argument('--log-level', default=default, help=f'log level for the {marvis_name} logger')
            self.add_argument('--global-log-level', default=default, help='log level for the global logger')

        args = vars(self.parse_args())

        if setup_logging:
            log_level = args.pop('log_level')
            global_log_level = args.pop('global_log_level')

            logging.basicConfig(level=global_log_level)
            logging.getLogger().setLevel(global_log_level)
            logging.getLogger(marvis_name).setLevel(log_level)
            # Otherwise pylxd websockets would be a little verbose.
            logging.getLogger('ws4py').setLevel(logging.WARNING)
            logging.getLogger(__name__).debug('log_level=%s, global_log_level=%s', log_level, global_log_level)

            if logger_arg:
                args[logger_arg] = logging.getLogger(self.prog)
                args[logger_arg].setLevel(log_level)

        main(**args)
