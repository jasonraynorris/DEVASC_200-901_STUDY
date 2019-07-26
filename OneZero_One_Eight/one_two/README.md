# DEVASC_200-901_STUDY, Developed using Python3.7
1.2 Describe parsing of common data format (XML, JSON, and YAML) to Python data structures

The follow image represents the common hierarchical structure of XML.  When using XML parsers, common variables and functions might include terms such as root,element,parent,child, and subchild.

Reference: https://www.w3schools.com/xml/xml_tree.asp

<img src="https://www.w3schools.com/xml/nodetree.gif">

Look at the next xml 
<div type = "text" style="margin: 0 auto;max-width: 700px;height: 100px;background-color: #ccc;border-radius: 3px;">
<?xml version="1.0" ?>
<root>
	<switches type="list">
		<item type="dict">
			<hostname type="str">switch_000001</hostname>
			<serial_numbers type="dict">
				<chassis type="str">SNXA0018AX00BA</chassis>
			</serial_numbers>
			<interfaces type="list">
				<item type="dict">
					<name type="str">ethernet0/0</name>
					<description type="str">SW_000002_0/0</description>
					<speed type="int">1000</speed>
					<duplex type="str">Full</duplex>
					<error_count type="dict">
						<crc type="int">0</crc>
						<frame type="int">0</frame>
						<overrun type="int">0</overrun>
					</error_count>
				</item>
				<item type="dict">
					<name type="str">ethernet0/1</name>
					<description type="str">SW_000002_0/1</description>
					<speed type="int">10</speed>
					<duplex type="str">Half</duplex>
					<error_count type="dict">
						<crc type="int">0</crc>
						<frame type="int">0</frame>
						<overrun type="int">0</overrun>
					</error_count>
				</item>
			</interfaces>
		</item>
		<item type="dict">
			<hostname type="str">switch_000002</hostname>
			<serial_numbers type="dict">
				<chassis type="str">SNXA0018AX00BC</chassis>
			</serial_numbers>
			<interfaces type="list">
				<item type="dict">
					<name type="str">ethernet0/0</name>
					<description type="str">SW_000001_0/0</description>
					<speed type="int">1000</speed>
					<duplex type="str">Full</duplex>
					<error_count type="dict">
						<crc type="int">0</crc>
						<frame type="int">0</frame>
						<overrun type="int">0</overrun>
					</error_count>
				</item>
				<item type="dict">
					<name type="str">ethernet0/1</name>
					<description type="str">SW_000001_0/1</description>
					<speed type="int">10</speed>
					<duplex type="str">Half</duplex>
					<error_count type="dict">
						<crc type="int">0</crc>
						<frame type="int">0</frame>
						<overrun type="int">0</overrun>
					</error_count>
				</item>
			</interfaces>
		</item>
	</switches>
</root>
</div>

