# import xml
import os
import json
# from xml.etree.ElementTree import ElementTree

class JSONParsing(object):
    def __init__(self):
        cur_path = os.path.dirname(__file__)
        """We replace the last directory with data_sets and append the file name"""
        self.json_file_name = cur_path.replace("one_two", "data_sets") + "\example_data_set.json"
        self.json_file = open(self.json_file_name,"r")
        self.json_file_read = self.json_file.read()
        json_obj = json.loads(self.json_file_read)
        # xml_obj = ElementTree(element=json_obj, file=None)
        # xml_obj_root = xml_obj.getroot()
        #xml_obj_str = xml.etree.ElementTree.tostring(xml_obj_root, encoding="us-ascii", method="xml", short_empty_elements=True)
        #print(xml_obj_str)

JSONParsing()