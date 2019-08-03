# DEVASC_200-901_STUDY
<p>Author: Jason Ray Norris</p>
<h4>Developed using Python3.7.4</h4>
<hr>
<h5>1.5 Explain the benefits of organizing code into methods / functions, classes, and modules
</h5>
<hr>

<h6>Section 1.5.1</h6>

# What are methods/functions, classes, and modules?

Methods/functions, classes, and modules are all terms collectively describing object-oriented programming.

<b>function</b> &nbsp;- a function is a block of statements that performs a specific task

<b>method</b> &nbsp;&nbsp;- a method is a block of statements that performs a specific task inside a class

<b>class</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- a construct defining an object through the use of properties and methods

<b>module</b> &nbsp;&nbsp;- a separate modular unit of code.

Reference: organizing_code.py
<br>
<img src="https://i.ibb.co/Wv59BWq/organizing-code.jpg">

You can find the module I used at exam_material/example_module/example_module.py. As you navigate the folder structure, pay attention to the &#95;&#95;init&#95;&#95;.py files in each folder to our target.  This file indicates to python that the containing folder is part of a module package. The navigation of the module is based on parent and child relationships.

<hr>

<h6>Section 1.5.2</h6>

# What are the Class benefits?

Class Benefits:

1. Classes and methods allow us to contain both function(method) and data within a referencable object.
2. Classes allow us to define a template for an object instance. This is helpful when describing the same <b>type</b> of object with different attributes.

Example Reference: demonstrating_benefits.py
<pre>
import json

"""Let's construct a class to represent a switch"""
class SwitchClass(object):
    def __init__(self,hostname=None,vendor=None,model=None,serial_numbers=None,interfaces=None):
        self.hostname = str(hostname)
        self.vendor = str(vendor)
        self.model = str(model)
        if serial_numbers:
            self.serial_numbers = dict(serial_numbers)
        else:
            self.serial_numbers = {}
        if interfaces:
            self.interfaces = dict(interfaces)
        else:
            self.interfaces = {}
    def get_serialized(self):
        return self.__dict__
    def set_hostname(self, hostname):
        if len(hostname) < 15:
            self.vendor = str(hostname)
            return True
        return False
    def set_vendor(self,vendor):
        if len(vendor) < 15:
            self.vendor = str(vendor)
            return True
        return False
    def set_model(self,model):
        if len(model) < 15:
            self.vendor = str(model)
            return True
        return False
    def set_serial_number(self,key,value):
        if len(key) < 20:
            self.serial_numbers[key] = str(value)
            return True
        return False
    def remove_serial_number(self,key):
        if self.serial_numbers[key]:
            del(self.serial_numbers[key])
            return True
        return False
    def set_interface(self,key,value):
        if len(key) < 20:
            self.interfaces[key] = dict(value)
            return True
        return False
    def remove_interface(self,key):
        if self.interfaces[key]:
            del(self.interfaces[key])
            return True
        return False

"""Instantiate an object to represent switch a"""
switch_a = SwitchClass(hostname="switch_000001",vendor="Cisco Systems")
"""We could have instantiated the switch with the serial information, but this will demonstrate
 the methods inside the specific class object"""
switch_a.set_serial_number(key="chassis",value="SNXA0018AX00BA")

"""Instantiate an object to represent switch b"""
switch_b = SwitchClass(hostname="switch_000002",vendor="Cisco Systems")
"""We could have instantiated the switch with the serial information, but this will demonstrate
 the methods inside the specific class object"""
switch_b.set_serial_number(key="chassis",value="SNXA0018AX00BC")

"""instantiate a list to contain our switch data"""
switches = []
"""append serialized data to our switch list"""
switches.append(switch_a.get_serialized())
switches.append(switch_b.get_serialized())
"""instantiate a dictionary to contain our switches"""
json_dict = {}

"""Add our switches list to our json dictionary"""
json_dict["switches"] = switches

"""Print as json"""
print(json.dumps(json_dict,indent=4))

</pre>
You can instantiate this class to an object with different vendors and models assigned to the object.

<hr>

<h6>Section 1.5.2</h6>

# What are the Module benefits?

Module Benefits:

2. Modules allow us to better organize our code in separate files and folders as well as modularize it for re-usability




