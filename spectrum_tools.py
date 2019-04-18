
import os
import subprocess as sub 
import json 
import argparse
import time 
import datetime
import tkinter
import requests as r
import matplotlib.pyplot as plt

# COMMAND --> python spectrum_tools.py --startingf 2.434e9 --endingf 2.438e9

__author__ = 'Preston Lee Turner Jr'

__db_endpoint__ = '<endpoint>'
current_batch_path = '<path>'
history_batch_path = '<batch/batch-collection>'

class SpectrumParser:


    def __init__(self, scan_str):
        self.scan_str = scan_str.split('#')
        self.current_freq = 0.0

    def spectrum_batch_processing(self):
        spectrum_list = list()
        time, center_text, center_freq, freq_text, freq, power_text, power, noise_text, noise = self.scan_str
        packet = dict(center_freq=float(center_freq),frequency=float(freq),power=float(power),noise_floor=float(noise))
        self.current_freq = packet['frequency']
        return packet
        
    def current_frequency(self):
        return self.current_freq

class Spectrum_File:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename,self.mode)   
        return self.file

    def __exit__(self,exc_type,exc_val,traceback):
        self.file.close()

parser = argparse.ArgumentParser(description='This CLI will take in the starting and ending frequency to batch the spectrum analysis scan')
parser.add_argument(
    '-s','--startingf',
    help='enter starting frequency',
    required=True
)

parser.add_argument(
    '-e', '--endingf',
    help='enter ending frequency',
    required=True
)
results = parser.parse_args()

#print(float(results.startingf),float(results.endingf))


if __name__ == '__main__':
    current_directory = os.getcwd()
    directory_to_scan = os.chdir('/usr/local/share/gnuradio/examples/uhd/')

    with Spectrum_File('scan.txt', 'r') as scan:

        lines = scan.readlines()
        lines = lines[1:]
        c_f = list()
        fre = list()
        pwr = list()
        n_f = list()

        for line in lines:
            spectrum = SpectrumParser(line)
            if spectrum.current_freq <= float(results.endingf):
                _scan = spectrum.spectrum_batch_processing()
                #c_f.append(_scan['center_freq'])
                fre.append(_scan['frequency'])
                pwr.append(_scan['power'])
                n_f.append(_scan['noise_floor'])
    
    ## Graph
    plt.plot(fre,pwr)
    plt.plot(fre,n_f)
    plt.show()

    # print(fre)
    # print(pwr)
    # print(n_f)


        


        


