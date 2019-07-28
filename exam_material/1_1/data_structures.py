import json
import sys
import gzip
import io
import yaml
import os
from os import system, name
import cProfile
import xml
import xml.etree.ElementTree as ET
import time

"""References
https://docs.python.org/3/library/xml.etree.elementtree.html


"""
class DataStructures(object):
    def __init__(self):
        print("Using data_structures.py")
        cur_path = os.path.dirname(__file__)
        self.xml_file_name = cur_path.replace("1_1","data_sets")+"\example_data_set.xml"
        self.json_file_name = cur_path.replace("1_1", "data_sets") + "\example_data_set.json"
        self.yaml_file_name = cur_path.replace("1_1", "data_sets") + "\example_data_set.yaml"
        print("Objectives:\n"
              " Let's compare the same data sizes using XML,JSON and YAML data structures\n"
              "  1. Compare parsing times?\n"
              "  2. How large are the data sets when in a human readable format?\n"
              "  3. How large are the data sets when in the smallest transferable format?\n")
        print("Compare the following files:")
        print(" "+self.xml_file_name)
        print(" "+self.json_file_name)
        print(" "+self.yaml_file_name)
        self.end_section()

        self.results = []
        self.results.append(self.ProcessXMLFile(filename=self.xml_file_name))
        self.results.append(self.ProcessJSONFile(filename=self.json_file_name))
        self.results.append(self.ProcessYAMLFile(filename=self.yaml_file_name))

        for example_data_set_dict in self.results:
            for k,v in example_data_set_dict.items():
                print("\n"+k)
                for each in v.items():
                    print("%s:%s" % (each[0],each[1]))
        print("\n%s\n  As of the date of writing this.  You will likely see that YAML is significantly slower to parse.\n  However, it's easily readable for our human eyes.\n  In most cases, what you use is up to you as the developer.\n  I recommend collecting some test data for yourself to make a data driven decision." % time.strftime("%x"))


    def gunzip_bytes_obj(self,bytes_obj):
        in_ = io.BytesIO()
        in_.write(bytes_obj)
        in_.seek(0)
        with gzip.GzipFile(fileobj=in_, mode='rb') as fo:
            gunzipped_bytes_obj = fo.read()

        return gunzipped_bytes_obj.decode()

    def gzip_str(self,string_):
        out = io.BytesIO()

        with gzip.GzipFile(fileobj=out, mode='w') as fo:
            fo.write(string_.encode())

        bytes_obj = out.getvalue()
        return bytes_obj

    def clear(self):
        if name == 'nt':
            _ = system ('cls')

        else:
            _ = system ('clear')
        print("\n")

    def end_section(self):
        input ("Press Any Key To Continue")
        self.clear ()

    def ProfileParseXML(self):
        example_xml_file = open(self.xml_file_name, "r")
        example_xml_str = example_xml_file.read()
        for i in range(1000):
            ET.fromstring(example_xml_str)

    def ProfileParseJSON(self):
        example_json_file = open(self.json_file_name, "r")
        example_json_str = example_json_file.read()
        for i in range(1000):
            json.loads(example_json_str)

    def ProfileParseYAML(self):
        example_yaml_file = open(self.yaml_file_name, "r")
        example_yaml_str = example_yaml_file.read()
        for i in range(1000):
            yaml.load(example_yaml_str,Loader=yaml.FullLoader)

    def ProcessXMLFile(self,filename):
        print("\nProcessing FileName:%s" % filename)
        example_xml_file = open(filename, "r")
        example_xml_str = example_xml_file.read()
        '''collect xml data'''
        xml_results = {}
        example_xml_str_no_ws = " ".join(example_xml_str.split()).replace("> <","><")
        root = ET.fromstring(example_xml_str_no_ws)
        example_xml_bytes = xml.etree.ElementTree.tostring(root, method="xml",short_empty_elements=True)
        example_xml_gzipped = self.gzip_str(example_xml_str_no_ws)
        #example_xml_ungzipped = gunzip_bytes_obj(example_xml_gzipped)
        xml_results['xml_str_human_readable'] = {
                                                "Description":"String Human Readable",
                                                "Type":type(example_xml_str),
                                                #"StringRepresentation":repr(example_xml_str),
                                                #"Length":len(example_xml_str),
                                                "Size":example_xml_str.__sizeof__()
                                                }
        xml_results['xml_str_nowhitespace'] = {
                                                "Description":"String No White Space",
                                                "Type":type(example_xml_str_no_ws),
                                                #"StringRepresentation":repr(example_xml_str_no_ws),
                                                #"Length":len(example_xml_str_no_ws),
                                                "Size":example_xml_str_no_ws.__sizeof__()
                                                }
        xml_results['xml_bytes_nowhitespace'] = {
                                                "Description":"Bytes No White Space",
                                                "Type":type(example_xml_bytes),
                                                #"StringRepresentation":repr(example_xml_bytes),
                                                #"Length":len(example_xml_bytes),
                                                "Size":example_xml_bytes.__sizeof__()
                                                }
        xml_results['xml_str_nowhitespace_gzipped'] = {
                                                "Description":"String No White Space Gzipped To Bytes",
                                                " Type":type(example_xml_gzipped),
                                                #"StringRepresentation":repr(example_xml_gzipped),
                                                #"Length":len(example_xml_gzipped),
                                                "Size":example_xml_gzipped.__sizeof__()
                                                }
        cProfile.runctx('self.ProfileParseXML()', globals(),locals())
        # cProfile.run('ProfileParseXML()')
        return xml_results

    def ProcessJSONFile(self,filename):
        print("\nProcessing FileName:%s" % filename)
        example_json_file = open(filename, "r")
        example_json_str = example_json_file.read()
        '''collect json size data'''
        json_results = {}
        example_json_str_no_ws = (json.dumps(json.loads(example_json_str), separators=(',', ':')))
        example_json_gzipped = self.gzip_str(example_json_str_no_ws)
        #example_xml_ungzipped = gunzip_bytes_obj(example_xml_gzipped)
        json_results['json_str_human_readable'] = {
                                                "Description":"String Human Readable",
                                                "Type":type(example_json_str),
                                                #"StringRepresentation":repr(example_xml_str),
                                                #"Length":len(example_xml_str),
                                                "Size":example_json_str.__sizeof__()
                                                }
        json_results['json_str_nowhitespace'] = {
                                                "Description":"String No White Space",
                                                "Type":type(example_json_str_no_ws),
                                                #"StringRepresentation":repr(example_xml_str_no_ws),
                                                #"Length":len(example_xml_str_no_ws),
                                                "Size":example_json_str_no_ws.__sizeof__()
                                                }
        json_results['json_bytes_nowhitespace'] = {
                                                "Description":"Bytes No White Space",
                                                "Type":type(bytes(example_json_str_no_ws,encoding="UTF-8")),
                                                #"StringRepresentation":repr(example_xml_bytes),
                                                #"Length":len(example_xml_bytes),
                                                "Size":sys.getsizeof(bytes(example_json_str_no_ws,encoding="UTF-8"))
                                                }
        json_results['json_str_nowhitespace_gzipped'] = {
                                                "Description":"String No White Space Gzipped To Bytes",
                                                "Type":type(example_json_gzipped),
                                                #"StringRepresentation":repr(example_xml_gzipped),
                                                #"Length":len(example_xml_gzipped),
                                                "Size":example_json_gzipped.__sizeof__()
                                                }
        cProfile.runctx('self.ProfileParseJSON()', globals(),locals())
        #cProfile.run('ProfileParseJSON()')
        return json_results

    def ProcessYAMLFile(self,filename):
        print("\nProcessing FileName:%s" % filename)
        example_yaml_file = open(filename, "r")
        example_yaml_str = example_yaml_file.read()
        yaml_results = {}
        example_yaml_gzipped = self.gzip_str(example_yaml_str)
        yaml_results['yaml_str_human_readable'] = {
                                                "Description":"String Human Readable",
                                                "Type":type(example_yaml_str),
                                                #"StringRepresentation":repr(example_xml_str),
                                                #"Length":len(example_xml_str),
                                                "Size":example_yaml_str.__sizeof__()
                                                }
        yaml_results['yaml_bytes'] = {
                                                "Description":"Bytes No White Space",
                                                "Type":type(bytes(example_yaml_str,encoding="UTF-8")),
                                                #"StringRepresentation":repr(example_xml_bytes),
                                                #"Length":len(example_xml_bytes),
                                                "Size":sys.getsizeof(bytes(example_yaml_str,encoding="UTF-8"))
                                                }
        yaml_results['yaml_str_gzipped'] = {
                                                "Description":"String Gzipped To Bytes",
                                                "Type":type(example_yaml_gzipped),
                                                #"StringRepresentation":repr(example_xml_gzipped),
                                                #"Length":len(example_xml_gzipped),
                                                "Size":example_yaml_gzipped.__sizeof__()
                                                }
        cProfile.runctx('self.ProfileParseYAML()', globals(),locals())
                        # cProfile.run('ProfileParseYAML()')
        return yaml_results

if __name__ == "__main__":
    DataStructures()