# DEVASC_200-901_STUDY
<p>Author: Jason Ray Norris</p>
<h4>Developed using Python3.7.4</h4>
<hr>
<h5>1.1 Compare data formats (XML, JSON, and YAML)
</h5>
<hr>
Q. What are these data formats?
<br> &nbsp;&nbsp;&nbsp;A. These data formats are structures intended to serialize data for storage and transfer.
<br><br>
We have written data_structures.py to give you a tool for comparison metrics of XML, JSON, and YAML using code.
<br><br>
If you want to compare a different data set, just replace these example files:

1. example_data_set.XML
1. example_data_set.json
1. example_data_set.yaml


I've attached some excellent reference resources to get a better understanding of each format.  I recommend reading each section.

Reference: https://www.w3schools.com/xml/schema_intro.asp

Reference: https://www.w3schools.com/js/js_json_intro.asp

Reference: https://www.tutorialspoint.com/yaml/

<hr>
 <h6>Section 1.1.1</h6>

# Ranking Data Formats

These rankings represent my own thoughts and opinions. Please come back to this section after 1.0-1.8 for review.
 
Ranking based on the following criteria:
<pre>
HumanProcess     - Ability to read, write and comprehend the overall data structure.
CodeUsability    - Ability to parse and use the data structure in code.
CodePerformance  - Code parsing performance.
Storage&Transfer - Total size for storage and transfer(including compression).
</pre>
<table style="width:100%">
  <tr>
    <th>Type</th>
    <th>HumanProcess</th> 
    <th>CodeUsability</th>
    <th>CodePerformance</th>
    <th>Storage&Transfer</th>
  </tr>
  <tr>
    <td>XML</td>
    <td>7/10</td> 
    <td>?</td>
    <td>7/10</td>
    <td>8/10</td>
  </tr>
  <tr>
    <td>JSON</td>
    <td>9/10</td>
    <td>?</td>
    <td>10/10</td>
    <td>9/10</td>
  </tr>
  <tr>
    <td>YAML</td>
    <td>10/10</td> 
    <td>?</td>
    <td>1/10</td>
    <td>10/10</td>
  </tr>  
</table>
<hr>
 <h6>Section 1.1.2</h6>

# Scripting Data Comparisons
Run data_structures.py.

If you do not wish to run the data_structures.py script yourself, the most recent output from my computer is appended below.

<pre>
Objectives:
 Let's compare the same data sizes using XML,JSON and YAML data structures
  1. Compare parsing times?
  2. How large are the data sets when in a human readable format?
  3. How large are the data sets when in the smallest transferable format?

Compare the following files:
 C:/Users/jason/PycharmProjects/DEVASC_200-901_STUDY/OneZero_One_Eight/data_sets\example_data_set.xml
 C:/Users/jason/PycharmProjects/DEVASC_200-901_STUDY/OneZero_One_Eight/data_sets\example_data_set.json
 C:/Users/jason/PycharmProjects/DEVASC_200-901_STUDY/OneZero_One_Eight/data_sets\example_data_set.yaml
Press Any Key To Continue



Processing FileName:C:/Users/jason/PycharmProjects/DEVASC_200-901_STUDY/OneZero_One_Eight/data_sets\example_data_set.xml
         3011 function calls in 0.032 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.032    0.032 <string>:1(<module>)
     1000    0.003    0.000    0.029    0.000 ElementTree.py:1302(XML)
        1    0.000    0.000    0.000    0.000 _bootlocale.py:11(getpreferredencoding)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 cp1252.py:22(decode)
        1    0.003    0.003    0.032    0.032 data_structures.py:78(ProfileParseXML)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_decode}
        1    0.000    0.000    0.000    0.000 {built-in method _locale._getdefaultlocale}
        1    0.000    0.000    0.032    0.032 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
     1000    0.000    0.000    0.000    0.000 {method 'close' of 'xml.etree.ElementTree.XMLParser' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1000    0.026    0.000    0.026    0.000 {method 'feed' of 'xml.etree.ElementTree.XMLParser' objects}
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.TextIOWrapper' objects}



Processing FileName:C:/Users/jason/PycharmProjects/DEVASC_200-901_STUDY/OneZero_One_Eight/data_sets\example_data_set.json
         10011 function calls in 0.013 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.013    0.013 <string>:1(<module>)
     1000    0.001    0.000    0.012    0.000 __init__.py:299(loads)
        1    0.000    0.000    0.000    0.000 _bootlocale.py:11(getpreferredencoding)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 cp1252.py:22(decode)
        1    0.001    0.001    0.013    0.013 data_structures.py:84(ProfileParseJSON)
     1000    0.001    0.000    0.011    0.000 decoder.py:332(decode)
     1000    0.010    0.000    0.010    0.000 decoder.py:343(raw_decode)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_decode}
        1    0.000    0.000    0.000    0.000 {built-in method _locale._getdefaultlocale}
        1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
     1000    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
     1000    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     2000    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
     2000    0.001    0.000    0.001    0.000 {method 'match' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.TextIOWrapper' objects}
     1000    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}



Processing FileName:C:/Users/jason/PycharmProjects/DEVASC_200-901_STUDY/OneZero_One_Eight/data_sets\example_data_set.yaml
         13819015 function calls (13711015 primitive calls) in 6.327 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    6.327    6.327 <string>:1(<module>)
     1000    0.015    0.000    6.324    0.006 __init__.py:103(load)
        1    0.000    0.000    0.000    0.000 _bootlocale.py:11(getpreferredencoding)
        1    0.000    0.000    0.000    0.000 _collections_abc.py:72(_check_methods)
        1    0.000    0.000    0.000    0.000 _collections_abc.py:92(__subclasshook__)
    41000    0.008    0.000    0.017    0.000 abc.py:137(__instancecheck__)
        1    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
13000/1000    0.080    0.000    5.869    0.006 composer.py:117(compose_mapping_node)
     1000    0.000    0.000    0.000    0.000 composer.py:13(__init__)
     1000    0.002    0.000    5.966    0.006 composer.py:29(get_single_node)
     1000    0.001    0.000    5.899    0.006 composer.py:50(compose_document)
89000/1000    0.164    0.000    5.894    0.006 composer.py:63(compose_node)
    73000    0.102    0.000    0.282    0.000 composer.py:88(compose_scalar_node)
3000/1000    0.013    0.000    5.787    0.006 composer.py:99(compose_sequence_node)
    73000    0.015    0.000    0.019    0.000 constructor.py:109(construct_scalar)
     3000    0.002    0.000    0.015    0.000 constructor.py:116(construct_sequence)
     3000    0.002    0.000    0.013    0.000 constructor.py:121(<listcomp>)
    13000    0.035    0.000    0.255    0.000 constructor.py:124(construct_mapping)
    73000    0.035    0.000    0.061    0.000 constructor.py:165(construct_scalar)
    13000    0.020    0.000    0.023    0.000 constructor.py:172(flatten_mapping)
    13000    0.012    0.000    0.290    0.000 constructor.py:207(construct_mapping)
    16000    0.013    0.000    0.030    0.000 constructor.py:229(construct_yaml_int)
     1000    0.000    0.000    0.000    0.000 constructor.py:24(__init__)
     1000    0.001    0.000    6.295    0.006 constructor.py:39(get_single_data)
    57000    0.014    0.000    0.062    0.000 constructor.py:393(construct_yaml_str)
     6000    0.002    0.000    0.018    0.000 constructor.py:396(construct_yaml_seq)
26000/20000    0.008    0.000    0.301    0.000 constructor.py:401(construct_yaml_map)
     1000    0.008    0.000    0.328    0.000 constructor.py:46(construct_document)
    89000    0.098    0.000    0.204    0.000 constructor.py:59(construct_object)
        1    0.000    0.000    0.000    0.000 cp1252.py:22(decode)
        1    0.003    0.003    6.327    6.327 data_structures.py:90(ProfileParseYAML)
   330000    0.115    0.000    0.115    0.000 error.py:6(__init__)
    16000    0.007    0.000    0.007    0.000 events.py:22(__init__)
     1000    0.001    0.000    0.001    0.000 events.py:37(__init__)
     1000    0.000    0.000    0.000    0.000 events.py:46(__init__)
    17000    0.004    0.000    0.004    0.000 events.py:5(__init__)
     1000    0.000    0.000    0.000    0.000 events.py:55(__init__)
    73000    0.035    0.000    0.035    0.000 events.py:65(__init__)
     1000    0.002    0.000    0.013    0.000 loader.py:23(__init__)
    73000    0.028    0.000    0.028    0.000 nodes.py:27(__init__)
    16000    0.006    0.000    0.006    0.000 nodes.py:36(__init__)
    89000    0.016    0.000    0.016    0.000 parser.py:107(peek_event)
   109000    0.027    0.000    0.034    0.000 parser.py:114(get_event)
     1000    0.001    0.000    0.005    0.000 parser.py:127(parse_stream_start)
     1000    0.002    0.000    0.053    0.000 parser.py:139(parse_implicit_document_start)
     1000    0.001    0.000    0.004    0.000 parser.py:159(parse_document_start)
     1000    0.001    0.000    0.003    0.000 parser.py:190(parse_document_end)
     7000    0.003    0.000    0.134    0.000 parser.py:264(parse_block_node)
    28000    0.012    0.000    0.362    0.000 parser.py:267(parse_flow_node)
    54000    0.027    0.000    0.800    0.000 parser.py:270(parse_block_node_or_indentless_sequence)
    89000    0.277    0.000    1.253    0.000 parser.py:273(parse_node)
     9000    0.014    0.000    0.478    0.000 parser.py:402(parse_indentless_sequence_entry)
     7000    0.006    0.000    0.166    0.000 parser.py:422(parse_block_mapping_first_key)
    34000    0.052    0.000    1.535    0.000 parser.py:427(parse_block_mapping_key)
    27000    0.038    0.000    1.399    0.000 parser.py:446(parse_block_mapping_value)
     6000    0.006    0.000    0.377    0.000 parser.py:537(parse_flow_mapping_first_key)
    20000    0.041    0.000    1.061    0.000 parser.py:542(parse_flow_mapping_key)
    14000    0.021    0.000    0.573    0.000 parser.py:569(parse_flow_mapping_value)
     1000    0.001    0.000    0.001    0.000 parser.py:81(__init__)
     1000    0.000    0.000    0.000    0.000 parser.py:89(dispose)
   272000    0.163    0.000    5.348    0.000 parser.py:94(check_event)
   330000    0.191    0.000    0.307    0.000 reader.py:114(get_mark)
     1000    0.001    0.000    0.003    0.000 reader.py:138(check_printable)
     1000    0.000    0.000    0.000    0.000 reader.py:146(update)
     1000    0.002    0.000    0.005    0.000 reader.py:59(__init__)
  1758000    0.297    0.000    0.297    0.000 reader.py:87(peek)
   192000    0.099    0.000    0.114    0.000 reader.py:94(prefix)
   371000    0.483    0.000    0.510    0.000 reader.py:99(forward)
    89000    0.012    0.000    0.012    0.000 resolver.py:114(ascend_resolver)
    89000    0.093    0.000    0.142    0.000 resolver.py:143(resolve)
     1000    0.000    0.000    0.000    0.000 resolver.py:21(__init__)
    89000    0.013    0.000    0.013    0.000 resolver.py:91(descend_resolver)
   672000    0.431    0.000    4.113    0.000 scanner.py:113(check_token)
   110000    0.040    0.000    0.138    0.000 scanner.py:125(peek_token)
    73000    0.406    0.000    1.385    0.000 scanner.py:1270(scan_plain)
    73000    0.146    0.000    0.375    0.000 scanner.py:1311(scan_plain_spaces)
   197000    0.121    0.000    0.348    0.000 scanner.py:135(get_token)
   167000    0.071    0.000    0.140    0.000 scanner.py:1416(scan_line_break)
  1120000    0.538    0.000    1.014    0.000 scanner.py:145(need_more_tokens)
   141000    0.266    0.000    2.873    0.000 scanner.py:156(fetch_more_tokens)
  1007000    0.163    0.000    0.163    0.000 scanner.py:264(next_possible_simple_key)
  1148000    0.369    0.000    0.369    0.000 scanner.py:279(stale_possible_simple_keys)
    79000    0.073    0.000    0.142    0.000 scanner.py:295(save_possible_simple_key)
    62000    0.011    0.000    0.011    0.000 scanner.py:312(remove_possible_simple_key)
   142000    0.035    0.000    0.046    0.000 scanner.py:325(unwind_indent)
    33000    0.007    0.000    0.008    0.000 scanner.py:349(add_indent)
     1000    0.001    0.000    0.003    0.000 scanner.py:359(fetch_stream_start)
     1000    0.002    0.000    0.008    0.000 scanner.py:371(fetch_stream_end)
    41000    0.018    0.000    0.018    0.000 scanner.py:38(__init__)
     6000    0.002    0.000    0.034    0.000 scanner.py:427(fetch_flow_mapping_start)
     6000    0.010    0.000    0.032    0.000 scanner.py:430(fetch_flow_collection_start)
     6000    0.002    0.000    0.034    0.000 scanner.py:450(fetch_flow_mapping_end)
     6000    0.011    0.000    0.032    0.000 scanner.py:453(fetch_flow_collection_end)
     8000    0.013    0.000    0.042    0.000 scanner.py:470(fetch_flow_entry)
     1000    0.001    0.000    0.004    0.000 scanner.py:48(__init__)
     6000    0.012    0.000    0.033    0.000 scanner.py:484(fetch_block_entry)
    41000    0.113    0.000    0.267    0.000 scanner.py:545(fetch_value)
    73000    0.061    0.000    1.601    0.000 scanner.py:668(fetch_plain)
     6000    0.002    0.000    0.003    0.000 scanner.py:690(check_document_start)
     6000    0.002    0.000    0.003    0.000 scanner.py:706(check_block_entry)
    41000    0.012    0.000    0.017    0.000 scanner.py:721(check_value)
    73000    0.024    0.000    0.036    0.000 scanner.py:731(check_plain)
   141000    0.170    0.000    0.408    0.000 scanner.py:752(scan_to_next_token)
   123000    0.028    0.000    0.028    0.000 tokens.py:3(__init__)
     1000    0.000    0.000    0.000    0.000 tokens.py:33(__init__)
    73000    0.028    0.000    0.028    0.000 tokens.py:98(__init__)
    41000    0.009    0.000    0.009    0.000 {built-in method _abc._abc_instancecheck}
        1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_decode}
        1    0.000    0.000    0.000    0.000 {built-in method _locale._getdefaultlocale}
        1    0.000    0.000    6.327    6.327 {built-in method builtins.exec}
  1420000    0.134    0.000    0.150    0.000 {built-in method builtins.isinstance}
   658000    0.049    0.000    0.049    0.000 {built-in method builtins.len}
    16000    0.003    0.000    0.005    0.000 {built-in method builtins.next}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
   412000    0.047    0.000    0.047    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    94000    0.009    0.000    0.009    0.000 {method 'extend' of 'list' objects}
   146000    0.019    0.000    0.019    0.000 {method 'get' of 'dict' objects}
    48000    0.008    0.000    0.008    0.000 {method 'insert' of 'list' objects}
    73000    0.007    0.000    0.007    0.000 {method 'join' of 'str' objects}
    50000    0.030    0.000    0.030    0.000 {method 'match' of 're.Pattern' objects}
   306000    0.056    0.000    0.056    0.000 {method 'pop' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.TextIOWrapper' objects}
    16000    0.003    0.000    0.003    0.000 {method 'replace' of 'str' objects}
     1000    0.002    0.000    0.002    0.000 {method 'search' of 're.Pattern' objects}
     8000    0.002    0.000    0.002    0.000 {method 'startswith' of 'str' objects}
    13000    0.003    0.000    0.003    0.000 {method 'update' of 'dict' objects}



xml_str_human_readable
Description:String Human Readable
Type:<class 'str'>
Size:1314

xml_str_nowhitespace
Description:String No White Space
Type:<class 'str'>
Size:1098

xml_bytes_nowhitespace
Description:Bytes No White Space
Type:<class 'bytes'>
Size:1068

xml_str_nowhitespace_gzipped
Description:String No White Space Gzipped To Bytes
 Type:<class 'bytes'>
Size:288

json_str_human_readable
Description:String Human Readable
Type:<class 'str'>
Size:1919

json_str_nowhitespace
Description:String No White Space
Type:<class 'str'>
Size:727

json_bytes_nowhitespace
Description:Bytes No White Space
Type:<class 'bytes'>
Size:719

json_str_nowhitespace_gzipped
Description:String No White Space Gzipped To Bytes
Type:<class 'bytes'>
Size:242

yaml_str_human_readable
Description:String Human Readable
Type:<class 'str'>
Size:734

yaml_bytes
Description:Bytes No White Space
Type:<class 'bytes'>
Size:726

yaml_str_gzipped
Description:String Gzipped To Bytes
Type:<class 'bytes'>
Size:238

07/26/19
  As of the date of writing this.  You will likely see that YAML is significantly slower to parse.
  However, it's easily readable for our human eyes.
  In most cases, what you use is up to you as the developer.
  I recommend collecting some test data for yourself to make a data driven decision.

Process finished with exit code 0
</pre>

