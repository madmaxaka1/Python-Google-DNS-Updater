import requests as r
import socket

user = "GOOGLE_API_USERNAME" #example: aknleker3w..etc
pw = "GOOGLE_API_PW" #example: dJlkn34Brsdfw..etc..
myDomain = "yourdomain.com" #example: yourdomain.com

#get your current public IP
myIP = r.get("https:/api.ipify.org")

#convert response to string
myIP = myIP.content.decode()

#try to get current IP of domain
try:
 domainIP = socket.gethostbyname(myDomain)
 #if we cant get current IP of domain, assign "" to domainIP
except Exception as e: 
    domainIP = ""

#compare your public IP to the current IP of the domain
if myIP != domainIP:
    #if the IPs are not the same then update the DNS record
    updateIP = r.post('https://' + user + ':' + pw +'@domains.google.com/nic/update?hostname='+ myDomain + '&myip=' + myIP + '')

#the IPs are the same, end.
