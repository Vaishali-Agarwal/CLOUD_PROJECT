#!/usr/bin/python

import cgi

print "Content-type:text/html\r\n\r\n"
#print ""

#this is for recv data from cloud
data=cgi.FieldStorage()
choice=data.getvalue('ch')


if choice == "firefox" :
	print "<META HTTP-EQUIV='refresh' content='0; url=/firefox.tar' />"
	#print "<a href=http://192.168.122.78/firefox.tar download>"
	#print "click here"
	#print "</a>"

elif choice == "vlc" :
	#print "<META HTTP-EQUIV='refresh' content='1 url=/vlc.sh' />"
	print "<a href=http://192.168.122.78/vlc.sh download>"
	print "click here"
	print "</a>"

elif choice == "Libreoffice" :
	#print "<META HTTP-EQUIV='refresh' content='1 url=/Libreoffice.sh' />"
	print "<a href=http://192.168.122.78/libreoffice.sh download>"
	print "click here"
	print "</a>"

elif choice == "Calculator" :
	#print "<META HTTP-EQUIV='refresh' content='1 url=/Calculator.sh' />"
	print "<a href=http://192.168.122.78/calculator.sh download>"
	print "click here"
	print "</a>"

elif choice == "Screenshot" :
	#print "<META HTTP-EQUIV='refresh' content='1 url=/Screenshot.sh' />"
	print "<a href=http://192.168.122.78/screenshot.sh download>"
	print "click here"
	print "</a>"

elif choice == "Webcam" :
	#print "<META HTTP-EQUIV='refresh' content='1 url=/Webcam.sh' />"
	print "<a href=http://192.168.122.78/webcam.sh download>"
	print "click here"
	print "</a>"

elif choice == "Imageviewer" :
	#print "<META HTTP-EQUIV='refresh' content='1 url=/Imageviewer.sh' />"
	print "<a href=http://192.168.122.78/imageviewer.sh download>"
	print "click here"
	print "</a>"

elif choice == "gedit" :
	#print "<META HTTP-EQUIV='refresh' content='1 url=/gedit.sh' />"
	print "<a href=http://192.168.122.78/gedit.sh download>"
	print "click here"
	print "</a>"

else :
	print "<META HTTP-EQUIV='refresh' content='0 url=/saas.sh' />"
	






