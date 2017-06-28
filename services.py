#!/usr/bin/python

import cgi

print "Content-type:text/html\r\n\r\n"
#print ""

#this is for recv data from cloud
data=cgi.FieldStorage()
service=data.getvalue('ch')


if service == "SAAS" :
	print "<META HTTP-EQUIV='refresh' content='0; url=/saas.html' /> "
	
elif service == "STAAS" :
	print "<META HTTP-EQUIV='refresh' content='0; url=/staas.html' />"
	
elif service == "IAAS" :
	print "<META HTTP-EQUIV='refresh' content='0; url=/iaas.html' />"
	
else :
	print "<META HTTP-EQUIV='refresh' content='0; url=/service.html' />"
	

