import os
import xml.etree.ElementTree as ET
from os import system, name

class XMLParsing(object):
    def __init__(self):
        print("Using xml_parsing.py")
        print(
            "\n Let's find the hostname and serial numbers of each switch in example_data_set.xml.\n")
        self.end_section()
        self.parsexml()

    def parsexml(self):
        """We get the current path that our file running this function is in"""
        cur_path = os.path.dirname(__file__)
        """We replace the last directory with data_sets and append the file name"""
        self.xml_file_name = cur_path.replace("1_2","data_sets")+"\example_data_set.xml"
        """We parse the xml file using the native xml parser at xml.etree.ElementTree.ET.parse() and return the xml tree"""
        tree = ET.parse(self.xml_file_name)
        """We use the tree objects built-in function getroot() to return the root element of the tree"""
        root = tree.getroot()
        """We iterate over the root element for elements with the tag switch"""
        for switch in root.findall('switch'):
            """For every switch we instantiate a dictionary object to store what we find about our switch"""
            switch_out = {'hostname': None, "chassis_serial": None}
            """We find and store the hostname text within the tagged element to our previously created dictionary as switch_out['hostname']"""
            switch_out['hostname'] = switch.find("hostname").text
            """We find the switch serial numbers element"""
            switch_serial_numbers_element = switch.find("serial_numbers")
            """We find and store the chassis serial text within the tagged element to our previously created dictionary as switch_out['chassis_serial']"""
            switch_out['chassis_serial'] = switch_serial_numbers_element.find("chassis").text
            """Finally, we print what we found"""
            """We could remove some of this code and use some one *one-liners*, but this should be easier to understand"""
            print("hostname:%s chassis_serial:%s" % (switch_out['hostname'], switch_out['chassis_serial']))


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
    XMLParsing()