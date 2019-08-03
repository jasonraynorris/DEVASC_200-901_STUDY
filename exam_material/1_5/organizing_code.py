"""Lets import these from a module as well"""
from exam_material.example_module.example_module import my_module_function
from exam_material.example_module.example_module import ModuleClassConstruct

"""Example of a basic function"""
def my_function():
    print("my_function")

"""Example of a class construct"""
class ClassConstruct(object):
    """We move our previous function into the class. The function now becomes a method"""
    def my_method(self):
        print("my_method")

print("Step 1. Execute Function")
my_function()
print("Step 2. Execute Method In Class")
class_obj = ClassConstruct()
class_obj.my_method()
print("Step 3. Execute Function From Module")
my_module_function()
print("Step 4. Execute Method In Class From Module")
class_from_module_obj = ModuleClassConstruct()
class_from_module_obj.my_class_method()