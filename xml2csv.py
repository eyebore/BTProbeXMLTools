#!/usr/bin/env python3
##
## xml2csv.py
## Convert BT probe XML stream list configuration file to CSV

## This program is free software. It comes without any warranty or support.
## Users of this software must accept responsibility and liability for all consequences
## arising from it's use. You may modify and/or distribute this software as much as you like.

# example xml file:
#
# <ewe mask="0x80" hw_type="4" br="BT" release="5.5.0-5">
#  <probe>
#   <core>
#    <setup>
#     <mcastnames>
#      <mclist xmlChildren="list" GreatestUsedTuningId="500">
#       <mcastChannel name="myStream_1" tuningId="101" addr="232.1.1.1" port="5500" sessionId="0" vlan_id="0" joinIfaceName="eth0" ssmAddr="0.0.0.0" ssmName="" ssmAddr2="0.0.0.0" ssmName2="" ssmAddr3="0.0.0.0" ssmName3="" ssmAddr4="0.0.0.0" ssmName4="" ssmAddr5="0.0.0.0" ssmName5="" tpreset="Default" vbcpreset="Default" etrThresholds="Default" pidThresholds="Default" serviceThresholds="Default" monitorEtr="false" referenceThresholds="[None]" etrEngine="1" join="true" extractThumbs="true" enableFec="false" page="1" dispPage="1" t2miStream="" t2miPid="4096" t2miPlp="-1" dash7Stream1="" dash7Stream2=""/>
#       <mcastChannel name="myStream_2" tuningId="102" addr="232.1.1.2" port="5500" sessionId="0" vlan_id="0" joinIfaceName="eth0" ssmAddr="0.0.0.0" ssmName="" ssmAddr2="0.0.0.0" ssmName2="" ssmAddr3="0.0.0.0" ssmName3="" ssmAddr4="0.0.0.0" ssmName4="" ssmAddr5="0.0.0.0" ssmName5="" tpreset="Default" vbcpreset="Default" etrThresholds="Default" pidThresholds="Default" serviceThresholds="Default" monitorEtr="false" referenceThresholds="[None]" etrEngine="1" join="true" extractThumbs="true" enableFec="false" page="1" dispPage="1" t2miStream="" t2miPid="4096" t2miPlp="-1" dash7Stream1="" dash7Stream2=""/>
#       <mcastChannel name="myStresm_3" tuningId="103" addr="232.1.1.3" port="5500" sessionId="0" vlan_id="0" joinIfaceName="eth0" ssmAddr="0.0.0.0" ssmName="" ssmAddr2="0.0.0.0" ssmName2="" ssmAddr3="0.0.0.0" ssmName3="" ssmAddr4="0.0.0.0" ssmName4="" ssmAddr5="0.0.0.0" ssmName5="" tpreset="Default" vbcpreset="Default" etrThresholds="Default" pidThresholds="Default" serviceThresholds="Default" monitorEtr="false" referenceThresholds="[None]" etrEngine="1" join="true" extractThumbs="true" enableFec="false" page="1" dispPage="1" t2miStream="" t2miPid="4096" t2miPlp="-1" dash7Stream1="" dash7Stream2=""/>
#       <mcastChannel name="myStream_4" tuningId="104" addr="232.1.1.4" port="5500" sessionId="0" vlan_id="0" joinIfaceName="eth0" ssmAddr="0.0.0.0" ssmName="" ssmAddr2="0.0.0.0" ssmName2="" ssmAddr3="0.0.0.0" ssmName3="" ssmAddr4="0.0.0.0" ssmName4="" ssmAddr5="0.0.0.0" ssmName5="" tpreset="Default" vbcpreset="Default" etrThresholds="Default" pidThresholds="Default" serviceThresholds="Default" monitorEtr="false" referenceThresholds="[None]" etrEngine="1" join="true" extractThumbs="true" enableFec="false" page="1" dispPage="1" t2miStream="" t2miPid="4096" t2miPlp="-1" dash7Stream1="" dash7Stream2=""/>
#      </mclist>
#     </mcastnames>
#    </setup>
#   </core>
#  </probe>
# </ewe>

import sys
import csv
import xml.etree.ElementTree as ET

params=["name","tuningId","addr","port","sessionId","vlan_id","joinIfaceName","ssmAddr","ssmName","ssmAddr2","ssmName2","ssmAddr3","ssmName3","ssmAddr4","ssmName4","ssmAddr5","ssmName5","tpreset","vbcpreset","etrThresholds","pidThresholds","serviceThresholds","monitorEtr","referenceThresholds","etrEngine","join","extractThumbs","enableFec","page","dispPage","t2miStream","t2miPid","t2miPlp","dash7Stream1","dash7Stream2"]

if len(sys.argv) != 2:
 print ('Usage: python3 xml2csv.py myFile.xml')
 print ('generates myFile.csv')
 sys.exit()
 
xmlFile = sys.argv[1]
csvFile = xmlFile[:-4] + '.csv'
data = open(csvFile, 'w')
csvwriter = csv.writer(data, delimiter=',',escapechar=' ',quoting=csv.QUOTE_NONE)
csvwriter.writerow(params)
tree=ET.parse(xmlFile)
mclist=tree.find('probe').find('core').find('setup').find('mcastnames').find('mclist')

for mcastChannel in mclist.iter('mcastChannel'):
 row=[]
 for param in params:
  row.append(mcastChannel.get(param))
 csvwriter.writerow(row)
data.close()
