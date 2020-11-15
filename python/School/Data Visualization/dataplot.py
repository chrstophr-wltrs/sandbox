import array
from matplotlib import pyplot as plt

class Pulse:
    """
    Simple class to represent a radiation spike.

    Attributes:
        number (int): The place of the Pulse within the file (first, second, third)
        start (int): Where the pulse begins
        area (int): the sum of the voltages of the pulse
    """
    def __init__(self, number, start, area):
        self.number = number
        self.start = start
        self.area = area
    
    def __str__(self):
        return (f"Pulse {self.number}: {self.start} ({self.area})")

class DataReader:
    """
    A class for reading and plotting data from voltage scan records.

    Attributes:
        file_name (str): The name of a file from which you're going to read radiation data. (ex. '2_Record2308.dat')
        file_title (str): same as file_name, but stripped of its extension; used for outputting files (ex. '2_Record2308')
        raw_data (array): Contains all of the radiation readings from the file
        smooth_data (array): Contains the smoothed data from raw_data; smoothed to make things a little easier to analyze
        pulses (list): list of Pulse objects
    """
    def __init__(self, file_name):
        self.raw_data = array.array('f')
        self.smooth_data = array.array('f')
        self.file_name = file_name
        self.file_title = file_name.strip('.dat')

    def read_data(self):
        """Clears smooth_data and raw_data, then loads them with the data from the file"""
        self.raw_data = array.array('f')
        self.smooth_data = array.array('f')
        with open(self.file_name, 'r') as file:
            for line in file:
                self.raw_data.append(float(line))
        for i in range(len(self.raw_data)):
            if (i > 2) and (i < (len(self.raw_data) - 3)):
                current_data_point = (self.raw_data[i - 3] + (2 * self.raw_data[i - 2]) + (3 * self.raw_data[i - 1]) + (3 * self.raw_data[i]) + (3 * self.raw_data[i + 1]) + (2 * self.raw_data[i + 2]) + self.raw_data[i + 3]) // 15
            else:
                current_data_point = self.raw_data[i]
            self.smooth_data.append(current_data_point)

    def find_pulses(self, vt = 100):
        """
        Uses smooth_data to find pulses, calculates the area of each pulse based on raw_data, then adds it to the pulses list
        
        Parameters:
            vt (int): voltage threshold; the minimum difference between a voltage reading and the reading after next which triggers as 'pulse.' def: 100
        """
        self.pulses = []
        # pulse_flag is used to determine whether a pulse is currently being measured, to prevent false flags of triggering multiple 'pulses' being found at the same location
        pulse_flag = False
        for i in range(len(smooth_data) - 2):
            volt_diff = smooth_data[i + 2] - smooth_data[i]