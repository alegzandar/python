import re
LogFile=open('Visits.txt', 'r')
Data = LogFile.read()
print('data has been read successfully!\n')
IpUsageData={}
AdressHistoryData={}
IpPattern='[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'
AddressPatern='\/\w+\/\w+\/\w+\/\w+\/\w+[\S]+'
Ips=re.findall(IpPattern, Data)
Adresses=re.findall(AddressPatern, Data)
for Ip in Ips:
    if Ip in IpUsageData:
        IpUsageData[Ip]+=1
    elif not Ip in IpUsageData:
        IpUsageData.update({Ip: int(1)})
for Adress in Adresses:
    if Adress in AdressHistoryData:
        AdressHistoryData[Adress]+=1
    elif not Adress in AdressHistoryData:
        AdressHistoryData.update({Adress: int(1)})
print('these are the IPs, starting from the most commonly used: \n')
for ip in sorted(IpUsageData, key=IpUsageData.get, reverse=True):
    print('{} is used {} time/s'.format(ip, IpUsageData[ip]))
for adress in sorted(AdressHistoryData, key=AdressHistoryData.get, reverse=True):
    print('{} has been visited {} time/s'.format(adress, AdressHistoryData[adress]))

