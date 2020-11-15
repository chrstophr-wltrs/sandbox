import array
from matplotlib import pyplot as plt
import glob

class Pulse:
    """
    Simple class to represent a radiation spike.

    Attributes:
        number (int): The place of the Pulse within the file (first, second, third)
        start (int): Where the pulse begins
        area (int): the sum of the voltages of the pulse
    """
    def __init__(self, number, start, area = 0):
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
        print(f"Created data reader for {self.file_title}")

    def read_data(self):
        """Clears smooth_data and raw_data, then loads them with the data from the file"""
        self.raw_data = array.array('f')
        self.smooth_data = array.array('f')
        print(f"Importing data for {self.file_name}...")
        with open(self.file_name, 'r') as file:
            for line in file:
                self.raw_data.append(float(line))
        print(f"Data imported; smoothing data...")
        for i in range(len(self.raw_data)):
            if (i > 2) and (i < (len(self.raw_data) - 3)):
                current_data_point = (self.raw_data[i - 3] + (2 * self.raw_data[i - 2]) + (3 * self.raw_data[i - 1]) + (3 * self.raw_data[i]) + (3 * self.raw_data[i + 1]) + (2 * self.raw_data[i + 2]) + self.raw_data[i + 3]) // 15
            else:
                current_data_point = self.raw_data[i]
            self.smooth_data.append(current_data_point)
        print(f"Data smoothed")

    def find_pulses(self, vt = 100):
        """
        Uses smooth_data to find pulses, calculates the area of each pulse based on raw_data, then adds it to the pulses list
        
        Parameters:
            vt (int): voltage threshold; the minimum difference between a voltage reading and the reading after next, which triggers as 'pulse.' def: 100
        """
        self.pulses = []
        pulse_counter = 0
        # pulse_flag is used to determine whether a pulse is currently being measured, to prevent false flags of triggering multiple 'pulses' being found at the same location
        pulse_flag = False
        print(f"Searching {self.file_title}'s smooth_data for pulses...")
        for i in range(len(self.smooth_data) - 2):
            volt_diff = self.smooth_data[i + 2] - self.smooth_data[i]
            if (volt_diff > vt) and (pulse_flag == False):
                print(f"Found a pulse starting at {i}!")
                pulse_flag = True
                pulse_start = i
                pulse_counter += 1
                current_pulse = Pulse(pulse_counter, pulse_start)
                self.pulses.append(current_pulse)
                print(f"Added new pulse to {self.file_title}'s pulses list")
            elif (volt_diff < 0) and (pulse_flag == True):
                print("Voltage is decreasing, searching for new pulses...")
                pulse_flag = False
        print(f"Found {pulse_counter} pulses, calculating area...")
        for i in range(len(self.pulses)):
            current_pulse = self.pulses[i]
            current_pulse
            print(f"Calculating Pulse {current_pulse.number}'s area using {self.file_title}'s raw_data...")
            if i >= len(self.pulses) - 1:
                next_pulse_start = len(self.raw_data)
            else:
                next_pulse_start = self.pulses[i + 1].start 
            if (current_pulse.start + 50) > next_pulse_start:
                print(f"Pulse {current_pulse.number} is close to the next pulse, so its area will be smaller.")
                pulse_area = int(sum(self.raw_data[current_pulse.start:next_pulse_start]))
            elif (current_pulse.start + 50) >= len(self.raw_data):
                print(f"Pulse {current_pulse.number} is close to the end of the data, so its area will be smaller.")
                pulse_area = int(sum(self.raw_data[current_pulse.start:]))
            else:
                pulse_area = int(sum(self.raw_data[current_pulse.start:current_pulse.start + 50]))
            print(f"Pulse {current_pulse.number}'s area equals {pulse_area}")
            current_pulse.area = pulse_area
    
    def plot_and_output(self):
        """
        Plots raw_data and smooth_data on separate axes, saves the plot to a pdf,
        then outputs the pulse information to a .out file.
        """
        print(f"Plotting data for {self.file_title}...")
        figure, (raw_dat, sm_dat) = plt.subplots(nrows = 2)
        raw_dat.plot(range(len(self.raw_data)), self.raw_data)
        raw_dat.set_ylabel("raw")
        raw_dat.set_title(self.file_name)
        sm_dat.plot(range(len(self.smooth_data)), self.smooth_data)
        sm_dat.set_ylabel("smooth")
        figure.savefig(f"{self.file_title}.pdf")
        print(f"Data is plotted and saved to pdf")
        print(f"Outputting and saving pulse data...")
        with open(f"{self.file_title}.out", 'w') as file:
            pulses_string = (f"{self.file_name}:")
            for i in self.pulses:
                pulses_string += (f"\n{i}")
            file.write(pulses_string)
        print(f"Pulse data saved!")
        print(f"Finished output for {self.file_title}")

    
def analyze(fname):
    """
    Analyzes and saves the radiation data, from a .dat file

    Parameters:
        fname (str): the string ending in '.dat' which you want analyzed.
    """
    data = DataReader(fname)
    data.read_data()
    data.find_pulses()
    data.plot_and_output()

def main():
    for fname in glob.glob('*.dat'):
        analyze(fname)

if __name__ == "__main__":
    main()