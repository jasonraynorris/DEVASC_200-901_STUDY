import json
import sys
import yaml
# import dicttoxml
import xml.dom.minidom
from os import system, name
import cProfile
from lxml import etree
import xml.etree.ElementTree as ET

def clear():
    if name == 'nt':
        _ = system ('cls')

    else:
        _ = system ('clear')

def end_section():
    input ("Press Any Key To Continue")
    clear ()

'''Open data structures and read to string vars'''
example_xml_file = open("example_data_set.xml","r")
example_xml = example_xml_file.read()
example_json_file = open("example_data_set.json","r")
example_json = example_json_file.read()
example_yaml_file = open("example_data_set.yaml","r")
example_yaml = example_yaml_file.read()

print("Let's compare the same data using different data structures")


'''collect xml size data'''
xml_size_results = {}

xml_size_results["xml_whitespace_string"] = example_xml.__sizeof__()
parser = etree.XMLParser(remove_blank_text=True)
elem = etree.XML(example_xml, parser=parser)
#xml_size_results["xml_nowhitespace_string"] = etree.tostring(elem).__sizeof__()
xml_size_results["xml_nowhitespace_bytes"] = sys.getsizeof(etree.tostring(elem))

'''collect json size data'''
json_size_results = {}

json_size_results["json_whitespace_string"] = example_json.__sizeof__()
json_no_whitespace = (json.dumps(json.loads(example_json), separators=(',', ':')))
#json_size_results["json_nowhitespace_string"] = json_no_whitespace.__sizeof__()
json_size_results["json_nowhitespace_bytes"] = sys.getsizeof(json_no_whitespace)

'''collect yaml size data'''

yaml_size_results = {}
yaml_size_results["yaml_whitespace_string"] = example_yaml.__sizeof__()
yaml_size_results["yaml_whitespace_bytes"] = sys.getsizeof(example_yaml)

print('{:>6}{:>10}{:>10}'.format('type','pre_xfer','xfer_size'))
print('{:>6}{:>10}{:>10}'.format('XML',xml_size_results["xml_whitespace_string"],xml_size_results["xml_nowhitespace_bytes"]))
print('{:>6}{:>10}{:>10}'.format('JSON',json_size_results["json_whitespace_string"],json_size_results["json_nowhitespace_bytes"]))
print('{:>6}{:>10}{:>10}'.format('YAML',yaml_size_results["yaml_whitespace_string"],yaml_size_results["yaml_whitespace_bytes"]))
end_section()

print(""" Take a look at the human readability of the same data in different structures.\n  You can copy the following data structures into a common parser.\n  Try Notepad++ and set the relevant parsing language\n""")

if input("Print XML(Y/N):") == "Y":
    print(example_xml)
if input("Print JSON:(Y/N)") == "Y":
    print(json.dumps(example_json,indent=4))
if input("Print YAML(Y/N):") == "Y":
    print(example_yaml)
end_section()

# print("  Let's look at parsing times using Python.\n  We will parse the data as strings.  We will run each parser 1000 iterations. \n")
#
# json_str = json.dumps(testjson,indent=4)
#
# def ProfileParseJSON():
#     for i in range(1000):
#         json.loads(json_str)
#
# def ProfileParseXML():
#     for i in range(1000):
#         ET.fromstring (testxml)
#
# def ProfileParseYAML():
#     for i in range(1000):
#         yaml.load(testyaml)
#
# if input("Parse XML:(Y/N)") == "Y":
#     cProfile.run ('ProfileParseXML()')
#
# if input("Parse JSON:(Y/N)") == "Y":
#     cProfile.run ('ProfileParseJSON()')
#
# if input("Parse YAML:(Y/N)") == "Y":
#     cProfile.run ('ProfileParseYAML()')
#
# print("  As of the date of writing this.  You will likely see that YAML is significantly slower to parse.\n  However, it's easily readable for our human eyes.\n  In most cases, what you use is up to you as the developer.\n  I would recommend collecting some test data for yourself to make a data driven decision.")
# print("  This concludes the current lesson.\n")
# end_section()

# '''convert json to yaml'''
# testyaml = yaml.safe_dump(testjson)
#
# '''convert json to xml'''
# testxml = dicttoxml.dicttoxml(testjson)
#
# '''parse xml'''
# xml = xml.dom.minidom.parseString(testxml).toprettyxml()