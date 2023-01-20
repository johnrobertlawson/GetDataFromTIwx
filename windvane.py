"""Reverse-engineering TI (TD-106-5D) anemometer to convert voltage into data

Wind directory is TD-106-5D

John R. Lawson, Valparaiso University, 2023
"""
import os

from metpy import units as units

from instrument import Instrument

class WindVane(Instrument):
    def __init__(self):
        """Superclass for all instruments.

        TODO:
            * Convert all to SI as soon as possible after manual text

        Notes:
            * The electronic mechanism only goes 0 to 357 degrees
            * The cable is "3-conductor, 22 gauge"
        """
        self.model_number = "TF-106-5D"
        self.signal_presentation = 5000 * units.ohms
        # Interpret as "plus/minus"
        self.accuracy = 3.0 * units.degrees
        # What is this? As fraction +/-
        self.potentiometer_linearity = 0.005
        self.starting_threshold = 0.5 * units('m/s')
        self.resolution = 1 * units.degrees

        super().__init__()

    def read_data(self):
        pass

if __name__ == '__main__':
    pass

