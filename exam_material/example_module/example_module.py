"""We will use this file to demonstrate importing modules"""
"""Reference organizing_code.py for the import statements"""

"""Example of a basic function"""
def my_module_function():
    print("my_module_function")

"""Example of a class construct"""
class ModuleClassConstruct(object):
    """We move our previous function into the class. The function now becomes a method"""
    def my_class_method(self):
        print("my_module_class_method")