import json
from exam_material.example_module.base_classes_example import DeviceBaseClass

"""Let's construct a class to represent a switch"""
class SwitchClass(DeviceBaseClass):
    def __init__(self,interfaces=None,hostname=None,vendor=None,model=None,serial_numbers=None,mgmt_interfaces=None,cam_table=None):
        DeviceBaseClass.__init__(self, hostname,vendor,model,serial_numbers,mgmt_interfaces)
        '''Example of how we might handle input exceptions'''
        try:
            self.cam_table = list(cam_table)
        except Exception as ex:
            print("Exception:%s Handling:Setting var to empty table" % ex)
            self.cam_table = []
        '''if we want the code to fail with bad input, let it'''
        if interfaces:
            self.interfaces = dict(interfaces)
        else:
            self.interfaces = {}
        if interfaces:
            self.interfaces = dict(interfaces)
        else:
            self.interfaces = {}
    def set_interface(self,key,value):
        '''Maybe we do some input validation?'''
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
    def set_cam_table(self,cam_table):
        self.cam_table = list(cam_table)
        return True
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

