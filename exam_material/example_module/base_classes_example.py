"""Construct a base class"""
class DeviceBaseClass(object):

    '''called when class is instantiated'''
    def __init__(self,hostname=None,vendor=None,model=None,serial_numbers=None,mgmt_interfaces=None):
        self.hostname = str(hostname)
        self.vendor = str(vendor)
        self.model = str(model)
        if serial_numbers:
            self.serial_numbers = dict(serial_numbers)
        else:
            self.serial_numbers = {}
        if mgmt_interfaces:
            self.mgmt_interfaces = dict(mgmt_interfaces)
        else:
            self.mgmt_interfaces = {}
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

    '''management interface methods'''
    def set_mgmt_interface(self,key,value):
        if len(key) < 20:
            self.mgmt_interfaces[key] = dict(value)
            return True
        return False
    def remove_mgmt_interface(self,key):
        if self.mgmt_interfaces[key]:
            del(self.mgmt_interfaces[key])
            return True
        return False
    def get_mgmt_interface(self):
        return self.mgmt_interfaces
