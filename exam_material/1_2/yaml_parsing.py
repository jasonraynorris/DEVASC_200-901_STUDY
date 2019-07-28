import os
from os import system, name
import yaml

class YAMLParsing(object):
    def __init__(self):
        print("Using yaml_parsing.py")
        print(
            "\n Let's find the hostname and serial numbers of each switch in example_data_set.yaml.\n")
        self.end_section()
        self.parseyaml()

    def parseyaml(self):
        """We get the current path that our file running this function is in"""
        cur_path = os.path.dirname(__file__)
        """We replace the last directory with data_sets and append the file name"""
        self.yaml_file_name = cur_path.replace("1_2", "data_sets") + "\example_data_set.yaml"
        """We open the file"""
        self.yaml_file = open(self.yaml_file_name,"r")
        """We store the contents of the file as a string"""
        self.yaml_file_read = self.yaml_file.read()
        """We load the string into yaml.loads and return the yaml object"""
        yaml_obj = yaml.load(self.yaml_file_read,Loader=yaml.Loader)
        """We get the list of switches from the top level dictionary(yaml_obj)"""
        switches_list = yaml_obj['switches']
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
    YAMLParsing()



