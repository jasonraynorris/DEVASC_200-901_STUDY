import os
import xml.etree.ElementTree as ET
import xml


class XMLParsing(object):
    def __init__(self):
        cur_path = os.path.dirname(__file__)
        self.xml_file_name = os.path.relpath('..\\data_sets\\example_data_set.xml', cur_path)
        #self.xml_file = open(self.xml_file_name,'r')
        #self.json_file_name = os.path.relpath('.\\data_sets\\example_data_set.json', cur_path)
        #self.yaml_file_name = os.path.relpath('.\\data_sets\\example_data_set.yaml', cur_path)
        #print(self.xml_file_name)
        tree = ET.parse(self.xml_file_name)
        print(xml.etree.ElementTree.tostring(tree.getroot(), encoding="UTF-8", method="xml",
                                           short_empty_elements=True))
        # print("root.tag:%s" % root.tag)
        # for switch in root:
        #     print("child.tag:%s child.attrib:%s" % (switch.tag,switch.attrib))
            # for child,v in switch.items():
                # print("child.tag:%s child.attrib:%s" % (child.tag, child.attrib))

if __name__ == "__main__":
    XMLParsing()