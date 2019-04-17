
import os
import subprocess as sub 
import json 
import argparse
import time 
import datetime
import requests as r


__author__ = 'Preston Lee Turner Jr'

__db_endpoint__ = 'https://spectrum-graph.firebaseio.com/'
current_batch_path = 'batch/current'
history_batch_path = 'batch/batch-collection'

class SpectrumParser:

    def __init__(self, scan_str):
        self.scan_str = scan_str.split(' ')

    def spectrum_batch_processing(self):
        spectrum_list = list()
        time, center_text, center_freq, freq_text, freq, power_text, power, noise_text, noise = self.scan_str
        packet = dict(center_freq=float(center_freq),frequency=float(freq),power=float(power),noise_floor=float(noise))

class Spectrum_File:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename,self.mode)   
        return self.file

    def __exit__(self,exc_type,exc_val,traceback):
        self.file.close()

parser = argparse.ArgumentParser(description='This CLI will take in the starting and ending frequency to batch scan')
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

print(results.startingf,results.endingf)


current_directory = os.getcwd()
directory_to_scan = os.chdir('/usr/local/share/gnuradio/examples/uhd/')

# with Spectrum_File('scan.txt', 'r') as scan:
#     # Lets remove the gain for its not important 
#     # at the moment 
#     gain = scan.readline()
#     spectrum = scan.readlines()
#     print(spectrum)