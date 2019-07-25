import json
import sys
import gzip
import io
import yaml
from os import system, name
import cProfile
import xml
import xml.etree.ElementTree as ET


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
    print("\nFileName:%s" % filename)
    example_xml_file = open(filename, "r")
    example_xml_str = example_xml_file.read()
    '''collect xml data'''
    xml_results = {}
    example_xml_str_no_ws = " ".join(example_xml_str.split()).replace("> <","><")
    root = ET.fromstring(example_xml_str_no_ws)
    example_xml_bytes = xml.etree.ElementTree.tostring(root, method="xml",short_empty_elements=True)
    example_xml_gzipped = gzip_str(example_xml_str_no_ws)
    #example_xml_ungzipped = gunzip_bytes_obj(example_xml_gzipped)
    
    xml_results['str_human_readable'] = {
                                            "Description":"String Human Readable",
                                            "Type":type(example_xml_str),
                                            #"StringRepresentation":repr(example_xml_str),
                                            #"Length":len(example_xml_str),
                                            "Size":example_xml_str.__sizeof__()
                                            }
    for k,v in xml_results['str_human_readable'].items():
        print(" %s:%s" % (k,v))
    xml_results['str_nowhitespace'] = {
                                            "Description":"String No White Space",
                                            "Type":type(example_xml_str_no_ws),
                                            #"StringRepresentation":repr(example_xml_str_no_ws),
                                            #"Length":len(example_xml_str_no_ws),
                                            "Size":example_xml_str_no_ws.__sizeof__()
                                            }
    for k,v in xml_results['str_nowhitespace'].items():
        print(" %s:%s" % (k,v))
    xml_results['bytes_nowhitespace'] = {
                                            "Description":"Bytes No White Space",
                                            "Type":type(example_xml_bytes),
                                            #"StringRepresentation":repr(example_xml_bytes),
                                            #"Length":len(example_xml_bytes),
                                            "Size":example_xml_bytes.__sizeof__()
                                            }
    for k,v in xml_results['bytes_nowhitespace'].items():
        print(" %s:%s" % (k,v))
    xml_results['str_nowhitespace_gzipped'] = {
                                            "Description":"String No White Space Gzipped To Bytes",
                                            " Type":type(example_xml_gzipped),
                                            #"StringRepresentation":repr(example_xml_gzipped),
                                            #"Length":len(example_xml_gzipped),
                                            "Size":example_xml_gzipped.__sizeof__()
                                            }
    for k,v in xml_results['str_nowhitespace_gzipped'].items():
        print(" %s:%s" % (k,v))
    xml_results['parsing_profile'] = cProfile.run('ProfileParseXML()')
    return xml_results

def ProcessJSONFile(filename):
    print("\nFileName:%s" % filename)
    example_json_file = open(filename, "r")
    example_json_str = example_json_file.read()
    '''collect json size data'''
    json_results = {}
    example_json_str_no_ws = (json.dumps(json.loads(example_json_str), separators=(',', ':')))
    example_json_gzipped = gzip_str(example_json_str_no_ws)
    #example_xml_ungzipped = gunzip_bytes_obj(example_xml_gzipped)
    json_results['str_human_readable'] = {
                                            "Description":"String Human Readable",
                                            "Type":type(example_json_str),
                                            #"StringRepresentation":repr(example_xml_str),
                                            #"Length":len(example_xml_str),
                                            "Size":example_json_str.__sizeof__()
                                            }
    for k,v in json_results['str_human_readable'].items():
        print(" %s:%s" % (k,v))
    json_results['str_nowhitespace'] = {
                                            "Description":"String No White Space",
                                            "Type":type(example_json_str_no_ws),
                                            #"StringRepresentation":repr(example_xml_str_no_ws),
                                            #"Length":len(example_xml_str_no_ws),
                                            "Size":example_json_str_no_ws.__sizeof__()
                                            }
    for k,v in json_results['str_nowhitespace'].items():
        print(" %s:%s" % (k,v))
    json_results['bytes_nowhitespace'] = {
                                            "Description":"Bytes No White Space",
                                            "Type":type(bytes(example_json_str_no_ws,encoding="UTF-8")),
                                            #"StringRepresentation":repr(example_xml_bytes),
                                            #"Length":len(example_xml_bytes),
                                            "Size":sys.getsizeof(bytes(example_json_str_no_ws,encoding="UTF-8"))
                                            }
    for k,v in json_results['bytes_nowhitespace'].items():
        print(" %s:%s" % (k,v))
    json_results['str_nowhitespace_gzipped'] = {
                                            "Description":"String No White Space Gzipped To Bytes",
                                            "Type":type(example_json_gzipped),
                                            #"StringRepresentation":repr(example_xml_gzipped),
                                            #"Length":len(example_xml_gzipped),
                                            "Size":example_json_gzipped.__sizeof__()
                                            }
    for k,v in json_results['str_nowhitespace_gzipped'].items():
        print(" %s:%s" % (k,v))
    json_results['parsing_profile'] = cProfile.run('ProfileParseJSON()')
    return json_results

def ProcessYAMLFile(filename):
    print("\nFileName:%s" % filename)
    example_yaml_file = open(filename, "r")
    example_yaml_str = example_yaml_file.read()
    yaml_results = {}
    example_yaml_gzipped = gzip_str(example_yaml_str)
    yaml_results['str_human_readable'] = {
                                            "Description":"String Human Readable",
                                            "Type":type(example_yaml_str),
                                            #"StringRepresentation":repr(example_xml_str),
                                            #"Length":len(example_xml_str),
                                            "Size":example_yaml_str.__sizeof__()
                                            }
    for k,v in yaml_results['str_human_readable'].items():
        print(" %s:%s" % (k,v))
    yaml_results['bytes'] = {
                                            "Description":"Bytes No White Space",
                                            "Type":type(bytes(example_yaml_str,encoding="UTF-8")),
                                            #"StringRepresentation":repr(example_xml_bytes),
                                            #"Length":len(example_xml_bytes),
                                            "Size":sys.getsizeof(bytes(example_yaml_str,encoding="UTF-8"))
                                            }
    for k,v in yaml_results['bytes'].items():
        print(" %s:%s" % (k,v))
    yaml_results['str_gzipped'] = {
                                            "Description":"String Gzipped To Bytes",
                                            "Type":type(example_yaml_gzipped),
                                            #"StringRepresentation":repr(example_xml_gzipped),
                                            #"Length":len(example_xml_gzipped),
                                            "Size":example_yaml_gzipped.__sizeof__()
                                            }
    for k,v in yaml_results['str_gzipped'].items():
        print(" %s:%s" % (k,v))
    yaml_results['parsing_profile'] = cProfile.run('ProfileParseYAML()')
    return yaml_results

print("Objectives:\n"
      " Let's compare the same data sizes using XML,JSON and YAML data structures\n"
      "  1. How large are the data sets when in a human readable format?\n"
      "  2. How large are the data sets when in the smallest transferable format?\n")
end_section()

xml_result_dict = ProcessXMLFile(filename="example_data_set.xml")

json_result_dict = ProcessJSONFile(filename="example_data_set.json")

yaml_result_dict = ProcessYAMLFile(filename="example_data_set.yaml")

print('{:>6}{:>20}{:>20}{:>20}'.format('type','human_read_bytes','xfer_size_bytes','compressed_to_%'))
print('{:>6}{:>20}{:>20}{:>20}'.format('XML',xml_result_dict["str_human_readable"]["Size"],xml_result_dict["str_nowhitespace_gzipped"]["Size"],(int(float(xml_result_dict['str_nowhitespace_gzipped']["Size"])/(float(xml_result_dict['str_human_readable']["Size"]))*100))))
print('{:>6}{:>20}{:>20}{:>20}'.format('JSON',json_result_dict["str_human_readable"]["Size"],json_result_dict["str_nowhitespace_gzipped"]["Size"],(int(float(json_result_dict['str_nowhitespace_gzipped']["Size"])/(float(json_result_dict['str_human_readable']["Size"]))*100))))
print('{:>6}{:>20}{:>20}{:>20}'.format('YAML',yaml_result_dict["str_human_readable"]["Size"],yaml_result_dict["str_gzipped"]["Size"],(int(float(yaml_result_dict['str_gzipped']["Size"])/(float(yaml_result_dict['str_human_readable']["Size"]))*100))))


print("  As of the date of writing this.  You will likely see that YAML is significantly slower to parse.\n  However, it's easily readable for our human eyes.\n  In most cases, what you use is up to you as the developer.\n  I recommend collecting some test data for yourself to make a data driven decision.")
end_section()
