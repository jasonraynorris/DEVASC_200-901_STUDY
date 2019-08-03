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

# What are the Class/Method benefits?

Class Benefits:

1. Classes and methods allow us to contain both function(method) and data within a referencable object.
2. Classes allow us to define a template for an object instance. This is helpful when describing the same <b>type</b> of object with different attributes.

Example Reference: demonstrating_benefits.py
<br>
<img src="https://i.ibb.co/JF1x368/class-method-benefit.jpg">

You can instantiate this class to an object with different vendors and models assigned to the object. It's re-usable code!

Here is the output from the code we ran above.

<pre>
{
    "switches": [
        {
            "hostname": "switch_000001",
            "vendor": "Cisco Systems",
            "model": "None",
            "serial_numbers": {
                "chassis": "SNXA0018AX00BA"
            },
            "interfaces": {}
        },
        {
            "hostname": "switch_000002",
            "vendor": "Cisco Systems",
            "model": "None",
            "serial_numbers": {
                "chassis": "SNXA0018AX00BC"
            },
            "interfaces": {}
        }
    ]
}
</pre>

This should look familiar.  It's a similar data structure to what's in example_data_set.json.  Now you can begin to see how we can use this data from code to storage/transfer and back to code.

<hr>

<h6>Section 1.5.3</h6>

# What are the Module benefits?

Module Benefits:

Any python file can become a module for use in another application or script. Modules can also be C and C++ extensions.

 1. Easier to organize our code in separate files and folders.
 2. Easier to <b>*modular</b>ize our code for re-usability
 3. Easier to design
 4. Easier to comprehend
 5. Easier to scale
 




