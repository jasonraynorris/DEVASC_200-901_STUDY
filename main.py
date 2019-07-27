from OneZero_One_Eight.one_one.data_structures import DataStructures
from OneZero_One_Eight.one_two.xml_parsing import XMLParsing
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')
    print("\n")

def end_section():
    print("\nThis concludes the section")
    input ("Press Any Key To Continue")
    clear ()

while True:

    print("1.    1.1 Compare data formats (XML, JSON, and YAML)")
    print("2.    1.2.1 Describe parsing of common data format (XML, JSON, and YAML) to Python data structures - XML")
    print("2.    1.2.2 Describe parsing of common data format (XML, JSON, and YAML) to Python data structures - JSON")
    print("2.    1.2.3 Describe parsing of common data format (XML, JSON, and YAML) to Python data structures - YAML")
    answer = input("\nPlease enter your selection:(1-10)")
    option_list = ['1','2']
    if answer not in option_list:
        pass
    clear()
    if answer == "1":
        DataStructures()
        end_section()
    elif answer == "2":
        XMLParsing()
        end_section()
