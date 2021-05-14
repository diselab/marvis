"""Interface class for providing co-simulation positional status output."""

class MobilityProvider:

    def getVehicleDetails(vehId):
        """This function returns if the vehicle is currently simulated on the map and if yes, furter details."""
        raise NotImplementedError
