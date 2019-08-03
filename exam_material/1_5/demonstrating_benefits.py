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

"""This should look familiar to our example_data_set.json"""