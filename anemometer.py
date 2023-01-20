"""Reverse-engineering TI (model num) anemometer to convert voltage into data

Wind directory is TD-106-5D

John R. Lawson, Valparaiso University, 2023
"""
from instrument import Instrument

class Anemometer(Instrument):
    def __init__(self):
        """Superclass for all instruments.
        """
        super().__init__()

    def read_data(self):
        pass

if __name__ == '__main__':
    pass

