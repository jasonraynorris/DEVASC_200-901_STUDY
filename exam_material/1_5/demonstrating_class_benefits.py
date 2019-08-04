import json

"""Construct a switch class"""
class SwitchClass(object):
    '''called when class is instantiated'''
    def __init__(self,interfaces=None,hostname=None,vendor=None,model=None,serial_numbers=None):
        self.hostname = str(hostname)
        self.vendor = str(vendor)
        self.model = str(model)
        if serial_numbers:
            self.serial_numbers = dict(serial_numbers)
        else:
            self.serial_numbers = {}
        self.cam_table = []
        if interfaces:
            self.interfaces = dict(interfaces)
        else:
            self.interfaces = {}
    '''get serialized object data'''
    def get_serialized(self):
        return self.__dict__
    '''hostname methods'''
    def set_hostname(self, hostname):
        if len(hostname) < 15:
            self.hostname = str(hostname)
            return True
        return False
    def get_hostname(self):
        return self.hostname

    '''vendor methods'''
    def set_vendor(self,vendor):
        if len(vendor) < 15:
            self.vendor = str(vendor)
            return True
        return False
    def get_vendor(self):
        return self.vendor

    '''model methods'''
    def set_model(self,model):
        if len(model) < 15:
            self.model = str(model)
            return True
        return False
    def get_model(self):
        return self.model

    '''serial number methods'''
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
    def get_serial_numbers(self):
        return self.serial_numbers

    '''interface methods'''
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
    def get_interface(self):
        return self.interfaces

    def get_cam_table(self):
        return self.cam_table

    '''example of a possible function to call switch and blackhole this mac'''
    def blackhole_mac_address(self,mac_address):
        function_completed = False
        if function_completed:
            print('blackholed:%s' % mac_address)
            return True
        return False

    '''example of a possible function to call shut an interface'''
    def shutdown_interface(self,interface):
        function_completed = False
        if function_completed:
            print('interface is shutdown:%s' % interface)
            return True
        return False

    '''example of a possible function to profile an interface'''
    def profile_interface(self,interface):
        '''check the OUI'''
        '''check the power'''
        '''check CDP'''
        '''check LLDP'''
        function_completed = False
        if function_completed:
            print('interface profiled:%s' % interface)
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

