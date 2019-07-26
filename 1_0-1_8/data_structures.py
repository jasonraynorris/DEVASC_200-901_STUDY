import json
import sys
import gzip
import io
import yaml
from os import system, name
import cProfile
import xml
import xml.etree.ElementTree as ET
import time

"""References
https://docs.python.org/3/library/xml.etree.elementtree.html


"""

xml_file_name = "example_data_set.xml"
json_file_name = "example_data_set.json"
yaml_file_name = "example_data_set.yaml"

def gunzip_bytes_obj(bytes_obj):
    in_ = io.BytesIO()
    in_.write(bytes_obj)
    in_.seek(0)
    with gzip.GzipFile(fileobj=in_, mode='rb') as fo:
        gunzipped_bytes_obj = fo.read()

    return gunzipped_bytes_obj.decode()

def gzip_str(string_):
    out = io.BytesIO()

    with gzip.GzipFile(fileobj=out, mode='w') as fo:
        fo.write(string_.encode())

    bytes_obj = out.getvalue()
    return bytes_obj

def clear():
    if name == 'nt':
        _ = system ('cls')

    else:
        _ = system ('clear')

def end_section():
    input ("Press Any Key To Continue")
    clear ()

def ProfileParseXML():
    example_xml_file = open(xml_file_name, "r")
    example_xml_str = example_xml_file.read()
    for i in range(1000):
        ET.fromstring(example_xml_str)

def ProfileParseJSON():
    example_json_file = open(json_file_name, "r")
    example_json_str = example_json_file.read()
    for i in range(1000):
        json.loads(example_json_str)

def ProfileParseYAML():
    example_yaml_file = open(yaml_file_name, "r")
    example_yaml_str = example_yaml_file.read()
    for i in range(1000):
        yaml.load(example_yaml_str,Loader=yaml.FullLoader)

def ProcessXMLFile(filename):
    print("\nProcessing FileName:%s" % filename)
    example_xml_file = open(filename, "r")
    example_xml_str = example_xml_file.read()
    '''collect xml data'''
    xml_results = {}
    example_xml_str_no_ws = " ".join(example_xml_str.split()).replace("> <","><")
    root = ET.fromstring(example_xml_str_no_ws)
    example_xml_bytes = xml.etree.ElementTree.tostring(root, method="xml",short_empty_elements=True)
    example_xml_gzipped = gzip_str(example_xml_str_no_ws)
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
    cProfile.run('ProfileParseXML()')
    return xml_results

def ProcessJSONFile(filename):
    print("\nProcessing FileName:%s" % filename)
    example_json_file = open(filename, "r")
    example_json_str = example_json_file.read()
    '''collect json size data'''
    json_results = {}
    example_json_str_no_ws = (json.dumps(json.loads(example_json_str), separators=(',', ':')))
    example_json_gzipped = gzip_str(example_json_str_no_ws)
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
    cProfile.run('ProfileParseJSON()')
    return json_results

def ProcessYAMLFile(filename):
    print("\nProcessing FileName:%s" % filename)
    example_yaml_file = open(filename, "r")
    example_yaml_str = example_yaml_file.read()
    yaml_results = {}
    example_yaml_gzipped = gzip_str(example_yaml_str)
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
    cProfile.run('ProfileParseYAML()')
    return yaml_results

print("Objectives:\n"
      " Let's compare the same data sizes using XML,JSON and YAML data structures\n"
      "  1. Compare parsing times?\n"
      "  2. How large are the data sets when in a human readable format?\n"
      "  3. How large are the data sets when in the smallest transferable format?\n")

end_section()

results = []
results.append(ProcessXMLFile(filename="example_data_set.xml"))
results.append(ProcessJSONFile(filename="example_data_set.json"))
results.append(ProcessYAMLFile(filename="example_data_set.yaml"))

for example_data_set_dict in results:
    for k,v in example_data_set_dict.items():
        print("\n"+k)
        for each in v.items():
            print("%s:%s" % (each[0],each[1]))




print("\n%s\n  As of the date of writing this.  You will likely see that YAML is significantly slower to parse.\n  However, it's easily readable for our human eyes.\n  In most cases, what you use is up to you as the developer.\n  I recommend collecting some test data for yourself to make a data driven decision." % time.strftime("%x"))

