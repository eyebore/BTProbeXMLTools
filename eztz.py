#!/usr/bin/python3
#
# eztz.py
#
# for use with Bridgetech Hardware Probes (HW 1-4 and HW 100)
#  
# set configuration value of ewe/probe/core/setup/params/timeZone (seconds from UTC)
# 
# Edit the list of management IP addresses or domain names
# for devices to change the timeZone setting in
#
# Examples:
# probeIPs=["10.0.1.1","10.0.1.2","10.0.1.3","10.0.1.4"]
# probeIPs=["probe1.mydomain","probe2.mydomain","probe3.mydomain","probe4.mydomain"]

probeIPs=["10.0.30.179","10.0.30.114","10.0.30.162","10.0.30.191"]

import sys, requests, xml.etree.ElementTree as ET

def indent(elem, level=0):
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem 

if len(sys.argv) != 2:
 print ('Edit the first line of code in this file (eztz.py) to confure a list of')
 print ('probes that will have their timeZone paramater modified')
 print ('Examples:')
 print ('probeIPs=["10.0.1.1","10.0.1.2","10.0.1.3","10.0.1.4"]')
 print ('or')
 print ('probeIPs=["probe1.mydomain","probe2.mydomain","probe3.mydomain","probe4.mydomain"]')
 print ('\n')
 print ('Usage: python3 eztz.py newTimeOffset (in hours from UTC)')
 print ('changes timeZone paramater in these devices: ' + str(probeIPs))
 print ('Examples:')
 print ('python eztz.py 2')
 print ('python eztz.py -5')

 sys.exit()
 
newOffset = str(int(sys.argv[1])*3600)

# Create an ewe element tree for setup params with timeZone 
ewe=ET.Element('ewe')
probe=ET.SubElement(ewe,'probe')
core=ET.SubElement(probe,'core')
setup=ET.SubElement(core,'setup')
params=ET.SubElement(setup,'params')
timeZone=ET.SubElement(params,'timeZone').text=newOffset
# add indents and convert tree to utf8 encoded string 
indent(ewe)
xmlstr=ET.tostring(ewe, encoding='utf8', method='xml')
headers = {'Content-Type': 'application/xml'}

# post to devices in probeIPs[] list
for probeIP in probeIPs:
 print ('Writing to device: ' + probeIP)
 response=requests.post('http://' + probeIP + '/probe/core/importExport/data.xml', data=xmlstr, headers=headers)
 print('Probe ' + probeIP + ' HTTP response code: ' + str(response.status_code))
# Unccoment this line to see the response body HTML code
# print('Probe ' + probeIP + ' HTTP response code: ' + str(response.content))
 print ('\n')