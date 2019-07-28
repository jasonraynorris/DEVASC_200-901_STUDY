import os
from os import system, name
import json

class JSONParsing(object):
    def __init__(self):
        print("Using json_parsing.py")
        print(
            "\n Let's find the hostname and serial numbers of each switch in example_data_set.json.\n")
        self.end_section()
        self.parsejson()

    def parsejson(self):
        """We get the current path that our file running this function is in"""
        cur_path = os.path.dirname(__file__)
        """We replace the last directory with data_sets and append the file name"""
        self.json_file_name = cur_path.replace("1_2", "data_sets") + "\example_data_set.json"
        """We open the file"""
        self.json_file = open(self.json_file_name,"r")
        """We store the contents of the file as a string"""
        self.json_file_read = self.json_file.read()
        """We load the string into json.loads and return the json object"""
        json_obj = json.loads(self.json_file_read)
        """We get the list of switches from the top level dictionary(json_obj)"""
        switches_list = json_obj['switches']
        """We iterate over each switch"""
        for switch in switches_list:
            """We print what we want"""
            print("hostname:%s chassis_serial:%s" % (switch["hostname"], switch["serial_numbers"]["chassis"]))


    def clear(self):
        if name == 'nt':
            _ = system ('cls')

        else:
            _ = system ('clear')
        print("\n")

    def end_section(self):
        input ("Press Any Key To Continue")
        self.clear ()

if __name__ == "__main__":
    JSONParsing()



