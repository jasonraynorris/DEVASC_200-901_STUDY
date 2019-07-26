# DEVASC_200-901_STUDY, Developed using Python3.7
1.2 Describe parsing of common data format (XML, JSON, and YAML) to Python data structures

I will be covering the same data using different formats.

# XML: eXtensible Markup Language

The follow image represents the common hierarchical structure of XML.  When using XML parsers, common variables and functions might include terms such as root,element,parent,child, and subchild.

Reference: https://www.w3schools.com/xml/xml_tree.asp

<img src="https://www.w3schools.com/xml/nodetree.gif">

Take a look at the following xml. As you can see, the python data types are defined as an attribute.Examples of these data types include: list,dictionary,string,integer,float.  Without type included, python parsers will use duct typing to define the data type.

<pre>
&lt;?xml version="1.0" ?>
&lt;root&gt;
	&lt;switches type="list"&gt;
		&lt;item type="dict"&gt;
			&lt;hostname type="str">switch_000001&lt;/hostname>
			&lt;serial_numbers type="dict">
				&lt;chassis type="str">SNXA0018AX00BA&lt;/chassis>
			&lt;/serial_numbers>
			&lt;interfaces type="list">
				&lt;item type="dict">
					&lt;name type="str">ethernet0/0&lt;/name>
					&lt;description type="str">SW_000002_0/0&lt;/description>
					&lt;speed type="int">1000&lt;/speed>
					&lt;duplex type="str">Full&lt;/duplex>
					&lt;error_count type="dict">
						&lt;crc type="int">0&lt;/crc>
						&lt;frame type="int">0&lt;/frame>
						&lt;overrun type="int">0&lt;/overrun>
					&lt;/error_count>
				&lt;/item>
				&lt;item type="dict">
					&lt;name type="str">ethernet0/1&lt;/name>
					&lt;description type="str">SW_000002_0/1&lt;/description>
					&lt;speed type="int">10&lt;/speed>
					&lt;duplex type="str">Half&lt;/duplex>
					&lt;error_count type="dict">
						&lt;crc type="int">0&lt;/crc>
						&lt;frame type="int">0&lt;/frame>
						&lt;overrun type="int">0&lt;/overrun>
					&lt;/error_count>
				&lt;/item>
			&lt;/interfaces>
		&lt;/item>
		&lt;item type="dict">
			&lt;hostname type="str">switch_000002&lt;/hostname>
			&lt;serial_numbers type="dict">
				&lt;chassis type="str">SNXA0018AX00BC&lt;/chassis>
			&lt;/serial_numbers>
			&lt;interfaces type="list">
				&lt;item type="dict">
					&lt;name type="str">ethernet0/0&lt;/name>
					&lt;description type="str">SW_000001_0/0&lt;/description>
					&lt;speed type="int">1000&lt;/speed>
					&lt;duplex type="str">Full&lt;/duplex>
					&lt;error_count type="dict">
						&lt;crc type="int">0&lt;/crc>
						&lt;frame type="int">0&lt;/frame>
						&lt;overrun type="int">0&lt;/overrun>
					&lt;/error_count>
				&lt;/item>
				&lt;item type="dict">
					&lt;name type="str">ethernet0/1&lt;/name>
					&lt;description type="str">SW_000001_0/1&lt;/description>
					&lt;speed type="int">10&lt;/speed>
					&lt;duplex type="str">Half&lt;/duplex>
					&lt;error_count type="dict">
						&lt;crc type="int">0&lt;/crc>
						&lt;frame type="int">0&lt;/frame>
						&lt;overrun type="int">0&lt;/overrun>
					&lt;/error_count>
				&lt;/item>
			&lt;/interfaces>
		&lt;/item>
	&lt;/switches>
&lt;/root>
</pre>

# JSON: JavaScript Object Notation

Take a look at the following json. It looks a lot like python doesn't it?  The data representations are the same.  This data format is my personal favourite.  It's readable and fast to parse for code usage.

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
# YAML: Ain't Markup Language

