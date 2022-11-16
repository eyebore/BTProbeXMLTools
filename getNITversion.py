#!/usr/bin/python3
# Gets NIT version number from AnaBinaryTableData API, PID 16, TID 64 using supplied device IP, inputId and tuningSetupId
import requests,sys
import xml.etree.ElementTree as ET
if len(sys.argv)!=4:
 print ('Usage: python3 getNITversion <probe IP addr> <inputId> <tuningSetupId>')
 print ('e.g. python3 getNITversion 10.0.30.165 1 21')
 sys.exit()
# Get tid extension (nwId) from etrData document
etrData=requests.get('http://'+sys.argv[1]+'/probe/etrdata?inputId='+sys.argv[2]+'&tuningSetupId='+sys.argv[3])
xmlData=ET.fromstring(etrData.text)
nwId=xmlData.find('input').find('tuningSetup').get('nwId') 
# Get the AnaBinaryTable data for PID 16 TID 64 tidExtension <nwId>
anaBinTabData=requests.get('http://'+sys.argv[1]+'/probe/etr/AnaBinaryTableData?inputId='+sys.argv[2]+'&etrEngineNo=0&pid=16&tid=64&tidExtension='+nwId)
# Mask to extract bits 3-7 of byte 5 and shift right
NITversion=(anaBinTabData.content[5]&0b00111110)>>1
print (str(NITversion)+'('+str(hex(NITversion))+')')