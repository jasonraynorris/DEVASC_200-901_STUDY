import os
import xml.etree.ElementTree as ET
from os import system, name

class XMLParsing(object):
    def __init__(self):
        print("Using xml_parsing.py")
        print(
            "\n Let's find the hostname and serial numbers of each switch in example_data_set.xml.\n Since we know the structure, this shouldn't be that hard\n")
        self.end_section()
        self.parsexml()

    def parsexml(self):
        """We get the current path that our file running this function is in"""
        cur_path = os.path.dirname(__file__)
        """We replace the last directory with data_sets and append the file name"""
        self.xml_file_name = cur_path.replace("one_two","data_sets")+"\example_data_set.xml"
        """We parse the xml file using the native xml parser at xml.etree.ElementTree.ET.parse() and return the xml tree"""
        tree = ET.parse(self.xml_file_name)
        """We use the tree objects built-in function getroot() to return the root element of the tree"""
        root = tree.getroot()
        """We iterate over the root element for elements with the tag switch"""
        for switch in root.iter('switch'):
            """For every switch we instantiate a dictionary object to store what we find about our switch"""
            switch_out = {'hostname': None, "chassis_serial": None}
            """We iterate over the switch element for elements with the tag hostname"""
            for switch_hostname_element in switch.iter("hostname"):
                """We store the text within the tagged element to our previously created dictionary as switch_out['hostname']"""
                switch_out['hostname'] = switch_hostname_element.text
            """We iterate over the switch element for elements with the tag serial_numbers"""
            for switch_serial_numbers_element in switch.iter("serial_numbers"):
                """We iterate over the serial_numbers element for elements with the tag chassis"""
                for switch_chassis_serial_number_element in switch_serial_numbers_element.iter("chassis"):
                    """We store the text within the tagged element to our previously created dictionary as switch_out['chassis_serial']"""
                    switch_out['chassis_serial'] = switch_chassis_serial_number_element.text
            """Finally, we print what we found"""
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