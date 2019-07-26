import os
import xml.etree.ElementTree as ET
from os import system, name

class XMLParsing(object):
    def __init__(self):
        print(
            " Let's find the hostname and serial numbers of each switch in example_data_set.xml.\n Since we know the structure, this shouldn't be that hard\n")
        self.end_section()
        self.parsexml()

    def parsexml(self):
        cur_path = os.path.dirname(__file__)
        self.xml_file_name = cur_path.replace("one_two","data_sets")+"\example_data_set.xml"
        tree = ET.parse(self.xml_file_name)
        root = tree.getroot()

        for switch in root.iter('switch'):
            switch_out = {'hostname': None, "chassis_serial": None}
            for switch_element in switch:
                if "hostname" == switch_element.tag:
                    switch_out['hostname'] = switch_element.text
                if "serial_numbers" == switch_element.tag:
                    for serial_element in switch_element:
                        if serial_element.tag == "chassis":
                            switch_out['chassis_serial'] = serial_element.text
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