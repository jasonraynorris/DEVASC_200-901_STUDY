import json
import sys
import yaml
import dicttoxml
import xml.dom.minidom
from os import system, name
import cProfile
import xml.etree.ElementTree as ET

def clear():
    # for windows
    if name == 'nt':
        _ = system ('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system ('clear')

def end_section():
    input ("\nPress Any Key To Continue\n")
    clear ()

testjson = {
    "switches": [{
                    "hostname": "switch_000001",
                    "serial_numbers": {
                        "chassis": "SNXA0018AX00BA"
                    },
                    "interfaces": [
                                    {
                                        "name":"ethernet0/0",
                                        "description":"SW_000002_0/0",
                                        "speed":1000,
                                        "duplex":"Full",
                                        "error_count":{
                                            "crc":0,
                                            "frame": 0,
                                            "overrun": 0,
                                        }
                                     },
                                    {
                                        "name": "ethernet0/1",
                                        "description": "SW_000002_0/1",
                                        "speed": 10,
                                        "duplex": "Half",
                                        "error_count": {
                                            "crc": 0,
                                            "frame": 0,
                                            "overrun": 0,
                                        }
                                    },
                                ]
                },
                {
                    "hostname": "switch_000002",
                    "serial_numbers": {
                        "chassis": "SNXA0018AX00BC"
                    },
                    "interfaces": [
                                    {
                                        "name": "ethernet0/0",
                                        "description": "SW_000001_0/0",
                                        "speed": 1000,
                                        "duplex": "Full",
                                        "error_count": {
                                            "crc": 0,
                                            "frame": 0,
                                            "overrun": 0,
                                        }
                                    },
                                    {
                                        "name": "ethernet0/1",
                                        "description": "SW_000001_0/1",
                                        "speed": 10,
                                        "duplex": "Half",
                                        "error_count": {
                                            "crc": 0,
                                            "frame": 0,
                                            "overrun": 0,
                                        }
                                    },
                                ],
                }]
}

'''convert json to yaml'''
testyaml = yaml.safe_dump(testjson)

'''convert json to xml'''
testxml = dicttoxml.dicttoxml(testjson)

'''parse xml'''
xml = xml.dom.minidom.parseString(testxml).toprettyxml()

print("  Let's compare data structures between XML, JSON and YAML\n")
end_section()

print(""" Here is a sample byte comparison using the following data set.\n  This notes the ammount of bytes required to transfer the same data using different structures.\n""")

print("Size of XML in bytes:%s" % sys.getsizeof(testxml))
print("Size of JSON in bytes:%s" % (sys.getsizeof(json.dumps(testjson))))
print("Size of YAML in bytes:%s" % sys.getsizeof(testyaml))
end_section()

print(""" Take a look at the human readability of the same data in different structures.\n  You can copy the following data structures into a common parser.\n  Try Notepad++ and set the relevant parsing language\n""")
if input("Print JSON:(Y/N)") == "Y":
    print(json.dumps(testjson,indent=4))
if input("Print XML(Y/N):") == "Y":
    print(xml)
if input("Print YAML(Y/N):") == "Y":
    print(testyaml)
end_section()

print("  Let's look at parsing times using Python.\n  We will parse the data as strings.  We will run each parser 1000 iterations. \n")

json_str = json.dumps(testjson,indent=4)

def ProfileParseJSON():
    for i in range(1000):
        json.loads(json_str)

def ProfileParseXML():
    for i in range(1000):
        ET.fromstring (testxml)

def ProfileParseYAML():
    for i in range(1000):
        yaml.load(testyaml)

if input("Parse XML:(Y/N)") == "Y":
    cProfile.run ('ProfileParseXML()')

if input("Parse JSON:(Y/N)") == "Y":
    cProfile.run ('ProfileParseJSON()')

if input("Parse YAML:(Y/N)") == "Y":
    cProfile.run ('ProfileParseYAML()')

print("  As of the date of writing this.  You will likely see that YAML is significantly slower to parse.\n  However, it's easily readable for our human eyes.\n  In most cases, what you use is up to you as the developer.\n  I would recommend collecting some test data for yourself to make a data driven decision.")
print("  This concludes the current lesson.\n")
end_section()