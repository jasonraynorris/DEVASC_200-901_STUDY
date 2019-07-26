# DEVASC_200-901_STUDY, Developed using Python3.7
1.2 Describe parsing of common data format (XML, JSON, and YAML) to Python data structures

I will be covering the same data using different formats.

# XML: eXtensible Markup Language

The follow image represents the common hierarchical structure of XML.  When using XML parsers, common variables and functions might include terms such as root,element,parent,child, and subchild.

<hr>
Reference: https://www.w3schools.com/xml/xml_tree.asp

<img src="https://www.w3schools.com/xml/nodetree.gif">

<hr>
Take a look at the following xml. Xml is the oldest of the three data formats.  It's usable and commonly supported, but not always the best choice.  It has the highest transfer and storage cost of all three data formats.

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

# JSON: JavaScript Object Notation

Take a look at the following json. It looks a lot like python, does it not?  The data representations are the same.  This data format is my personal preference.  It's readable and fast to parse for code usage. It has a slight higher storage and transfer cost as opposed to yaml, but so much faster for parsing.

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

Take a look at the following yaml.  It looks very readable doesn't it? How could you go wrong? It's readable, low transfer and storage cost. There's a catch! It parses very slowly in comparison with the other formats. Look at the previous sections output data! It also is not as commonly native supported for languages.  If you run into a language without a native parser, I suppose you can write your own...

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
