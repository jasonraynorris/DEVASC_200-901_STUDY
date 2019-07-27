# DEVASC_200-901_STUDY
<p>Author: Jason Ray Norris</p>
<h4>Developed using Python3.7.4</h4>
<hr>
<h5>1.2 Describe parsing of common data format (XML, JSON, and YAML) to Python data structures
</h5>
<hr>

We will be covering the same data using different formats.  We will only be using native libraries in Python version 3.7.4 for XML and JSON.


Reference: https://docs.python.org/3/library/xml.etree.elementtree.html

Reference: https://docs.python.org/3/library/json.html

There is no current native YAML parser in Python as of the current date and time.  We will use pyyaml 5.1.1 for YAML. 

Reference: https://pyyaml.org/wiki/PyYAMLDocumentation

<hr>
 <h6>Section 1.2.1</h6>
 
# XML: eXtensible Markup Language

An XML element can be represented by any open and closed tag. &lt;tag>&lt;/tag><br>
An element can have attributes. &lt;tag price="free">&lt;/tag><br>
An element can have text. &lt;tag price="free">my element text&lt;/tag><br>
An element can have children. &lt;parent_tag>&lt;child_tag>&lt;/child_tag>&lt;/parent_tag><br>


When describing element relationships we use terms such as parent, child, sibling, and subchild.


The image below represents the hierarchical structure of the example_data_set.xml.

<img src="https://i.ibb.co/P5d47YB/xml-structure.jpg">
<br>
Pay careful attention to the comments in the method we used below to parse the structure above.
We are looking for switches and want to store their hostnames and chassis serial numbers.

<img src="https://i.ibb.co/CwYtY3s/parsexml.jpg">

<hr>
Look at the following XML. XML is the oldest of the three data formats. It's usable and commonly supported, but not always the best choice.  It has the highest transfer and storage cost of all three data formats.

<pre>
&lt;?xml version="1.0" ?>
&lt;root>
	&lt;switch>
		&lt;hostname>switch_000001&lt;/hostname>
		&lt;serial_numbers>
			&lt;chassis>SNXA0018AX00BA&lt;/chassis>
		&lt;/serial_numbers>
		&lt;interface>
			&lt;name>ethernet0/0&lt;/name>
			&lt;description>SW_000002_0/0&lt;/description>
			&lt;speed>1000&lt;/speed>
			&lt;duplex>Full&lt;/duplex>
			&lt;error_count>
				&lt;crc>0&lt;/crc>
				&lt;frame>0&lt;/frame>
				&lt;overrun>0&lt;/overrun>
			&lt;/error_count>
		&lt;/interface>
		&lt;interface>
			&lt;name>ethernet0/1&lt;/name>
			&lt;description>SW_000002_0/1&lt;/description>
			&lt;speed>10&lt;/speed>
			&lt;duplex>Half&lt;/duplex>
			&lt;error_count>
				&lt;crc>0&lt;/crc>
				&lt;frame>0&lt;/frame>
				&lt;overrun>0&lt;/overrun>
			&lt;/error_count>
		&lt;/interface>
	&lt;/switch>
	&lt;switch>
		&lt;hostname>switch_000002&lt;/hostname>
		&lt;serial_numbers>
			&lt;chassis>SNXA0018AX00BC&lt;/chassis>
		&lt;/serial_numbers>
		&lt;interface>
			&lt;name>ethernet0/0&lt;/name>
			&lt;description>SW_000001_0/0&lt;/description>
			&lt;speed>1000&lt;/speed>
			&lt;duplex>Full&lt;/duplex>
			&lt;error_count>
				&lt;crc>0&lt;/crc>
				&lt;frame>0&lt;/frame>
				&lt;overrun>0&lt;/overrun>
			&lt;/error_count>
		&lt;/interface>
		&lt;interface>
			&lt;name>ethernet0/1&lt;/name>
			&lt;description>SW_000001_0/1&lt;/description>
			&lt;speed>10&lt;/speed>
			&lt;duplex>Half&lt;/duplex>
			&lt;error_count>
				&lt;crc>0&lt;/crc>
				&lt;frame>0&lt;/frame>
				&lt;overrun>0&lt;/overrun>
			&lt;/error_count>
		&lt;/interface>
	&lt;/switch>
&lt;/root>
</pre>
<hr>
 <h6>Section 1.2.2</h6>
 
# JSON: JavaScript Object Notation

Take a look at the following JSON. It looks a lot like Python, does it not?  The data representations are the same.  This data format is my personal preference.  It's readable and fast to parse for code usage. It has a slight higher storage and transfer cost as opposed to YAML, but so much faster for parsing.

<pre>
{
    "switches": [
        {
            "hostname": "switch_000001",
            "serial_numbers": {
                "chassis": "SNXA0018AX00BA"
            },
            "interfaces": [
                {
                    "name": "ethernet0/0",
                    "description": "SW_000002_0/0",
                    "speed": 1000,
                    "duplex": "Full",
                    "error_count": {
                        "crc": 0,
                        "frame": 0,
                        "overrun": 0
                    }
                },
                {
                    "name": "ethernet0/1",
                    "description": "SW_000002_0/1",
                    "speed": 10,
                    "duplex": "Half",
                    "error_count": {
                        "crc": 0,
                        "frame": 0,
                        "overrun": 0
                    }
                }
            ]
        },
        {
            "hostname": "switch_000002",
            "serial_numbers": {
                "chassis": "SNXA0018AX00BC"
            },
            "interfaces": [
                {
                    "name": "ethernet0/0",
                    "description": "SW_000001_0/0",
                    "speed": 1000,
                    "duplex": "Full",
                    "error_count": {
                        "crc": 0,
                        "frame": 0,
                        "overrun": 0
                    }
                },
                {
                    "name": "ethernet0/1",
                    "description": "SW_000001_0/1",
                    "speed": 10,
                    "duplex": "Half",
                    "error_count": {
                        "crc": 0,
                        "frame": 0,
                        "overrun": 0
                    }
                }
            ]
        }
    ]
}
</pre>

<hr>
 <h6>Section 1.2.2</h6>
 
# YAML: Ain't Markup Language

Take a look at the following YAML.  It looks very readable does it not? How could you go wrong? It's readable, low transfer and storage cost. There's a catch! YAML (pyyaml) parses very slowly in comparison with the other formats. Look at the previous 1.1 section output data!

It also is not as widely supported natively in common languages.  If you run into a language without a native parser, I suppose you can write your own...?

<pre>
switches:
- hostname: switch_000001
  interfaces:
  - description: SW_000002_0/0
    duplex: Full
    error_count: {crc: 0, frame: 0, overrun: 0}
    name: ethernet0/0
    speed: 1000
  - description: SW_000002_0/1
    duplex: Half
    error_count: {crc: 0, frame: 0, overrun: 0}
    name: ethernet0/1
    speed: 10
  serial_numbers: {chassis: SNXA0018AX00BA}
- hostname: switch_000002
  interfaces:
  - description: SW_000001_0/0
    duplex: Full
    error_count: {crc: 0, frame: 0, overrun: 0}
    name: ethernet0/0
    speed: 1000
  - description: SW_000001_0/1
    duplex: Half
    error_count: {crc: 0, frame: 0, overrun: 0}
    name: ethernet0/1
    speed: 10
  serial_numbers: {chassis: SNXA0018AX00BC}
  </pre>
