#!/usr/bin/env python3
##
## csv2xml.py
## Convert CSV file to BT probe XML streamlist configuration.

## This program is free software. It comes without any warranty or support.
## Users of this software must accept responsibility and liability for all consequences
## arising from it's use. You may modify and/or distribute this software as much as you like.

# First row of the csv files must comtain the paramater names

# example CSV file:

# name,tuningId,addr,port,sessionId,vlan_id,joinIfaceName,ssmAddr,ssmName,ssmAddr2,ssmName2,ssmAddr3,ssmName3,ssmAddr4,ssmName4,ssmAddr5,ssmName5,tpreset,vbcpreset,etrThresholds,pidThresholds,serviceThresholds,monitorEtr,referenceThresholds,etrEngine,join,extractThumbs,enableFec,page,dispPage,t2miStream,t2miPid,t2miPlp,dash7Stream1,dash7Stream2
# myStream_1,101,232.1.1.1,5500,0,0,eth0,0.0.0.0,,0.0.0.0,,0.0.0.0,,0.0.0.0,,0.0.0.0,,Default,Default,Default,Default,Default,false,[None],1,true,true,false,1,1,,4096,-1,,
# myStream_2,102,232.1.1.2,5500,0,0,eth0,0.0.0.0,,0.0.0.0,,0.0.0.0,,0.0.0.0,,0.0.0.0,,Default,Default,Default,Default,Default,false,[None],1,true,true,false,1,1,,4096,-1,,
# myStresm_3,103,232.1.1.3,5500,0,0,eth0,0.0.0.0,,0.0.0.0,,0.0.0.0,,0.0.0.0,,0.0.0.0,,Default,Default,Default,Default,Default,false,[None],1,true,true,false,1,1,,4096,-1,,
# myStream_4,104,232.1.1.4,5500,0,0,eth0,0.0.0.0,,0.0.0.0,,0.0.0.0,,0.0.0.0,,0.0.0.0,,Default,Default,Default,Default,Default,false,[None],1,true,true,false,1,1,,4096,-1,,

import sys
import csv

if len(sys.argv) != 2:
 print ('Usage: python3 csv2xml.py myFile.csv')
 print ('  generates myFile.xml')
 sys.exit()

csvFile = sys.argv[1]
xmlFile = csvFile[:-4] + '.xml'
csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')
xmlData.write('<ewe mask="0x80" hw_type="4" br="BT" release="5.5.0-5">' + "\n")
xmlData.write(' <probe>' + "\n")
xmlData.write('  <core>' + "\n")
xmlData.write('   <setup>' + "\n")
xmlData.write('    <mcastnames>' + "\n")
xmlData.write('     <mclist xmlChildren="list" GreatestUsedTuningId="500">' + "\n")

rowNum = 0
for row in csvData:
 if rowNum == 0:
  params = row
 else:
  if len(row)!=0: # skip empty rows
   xmlData.write('      <mcastChannel')
   for i in range(len(params)):
    xmlData.write(' ' + params[i] + '=' + '"' + row[i] + '"')
   xmlData.write('/>' + "\n")
  else:
   0 # print('empty row')  
 rowNum +=1  

xmlData.write('     </mclist>' + "\n") 
xmlData.write('    </mcastnames>' + "\n")
xmlData.write('   </setup>' + "\n")
xmlData.write('  </core>' + "\n")
xmlData.write(' </probe>' + "\n")
xmlData.write('</ewe>' + "\n")

xmlData.close()
