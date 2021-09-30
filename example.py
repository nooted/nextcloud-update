import NextCloud
import json

url = "http://111.68.101.225/nextcloud/"
userid = "nextcloud"
passwd = "nextcloud"
#passwd = "m8wb5-4ce5D-5wtQc-8QtHP-dmXz4"

#True if you want to get response as JSON
#False if you want to get response as XML
tojs = True

nxc = NextCloud.NextCloud(url,userid,passwd,tojs)
#dictt = (nxc.createShare(path="t1.md" , shareType=3 , shareWith=None, publicUpload=False , password=None ,  permissions=None))
print = (nxc.getShares())
#print (dictt['ocs']['data']['url'])
#print (dictt)
