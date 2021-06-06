class MobilityProvider:
    """Interface class for providing co-simulation positional status output."""

    def getVehicleDetails(self, vehId):
        """
        Return current vehicle status. If the vehicle is not part of the simulation, `isVehicleActive` will be False.
        Only if `isVehicleActive` is True the other fields contain correct values.

        Parameters
        ----------
        vehId - str
            The id of the vehicle in SUMO.
        """
        raise NotImplementedError

    def stopAtEndOfCurrentSegment(self, vehId, duration=0):
        """
        Schedule a stop the end of the current road segment for `vehId`. The stop will last `duration` seconds.

        Parameters
        ----------
        vehId - str
            The id of the vehicle in SUMO.
        duration - float
            The duration of the stop (default: 0)
        """
        raise NotImplementedError

    def resumeOrCancelStop(self, vehId):
        """
        Resume from a stop or remove the scheduled stop.

        Parameters
        ----------
        vehId - str
            The id of the vehicle in SUMO.
        """
        raise NotImplementedError
