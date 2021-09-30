import NextCloud
import json

url = ""
userid = ""
passwd = ""

#True if you want to get response as JSON
#False if you want to get response as XML
tojs = True

nxc = NextCloud.NextCloud(url,userid,passwd,tojs)
#dictt = (nxc.createShare(path="" , shareType=3 , shareWith=None, publicUpload=False , password=None ,  permissions=None))
print = (nxc.getShares())
#print (dictt['ocs']['data']['url'])
#print (dictt)
