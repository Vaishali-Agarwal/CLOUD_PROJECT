#!/usr/bin/python

import cgi,cgitb
import mysql.connector as mariadb 
print "Content-type:text/html\r\n\r\n"
#print ""
cgitb.enable()

#this is for recv data from cloud
data=cgi.FieldStorage()
s=data.getvalue('tab')
if s == "Sign Up" :
	u_name=data.getvalue('u_name')
	u_pass=data.getvalue('u_pass')
	u_cpass=data.getvalue('u_cpass')
	u_email=data.getvalue('u_email')
	try:     
	        mariadb_connection = mariadb.connect(user="root",password="vaishali", database="cloud") 

		cursor = mariadb_connection.cursor()       
 
		cursor.execute("INSERT INTO users(username,password,email) VALUES (%s,%s,%s)",(u_name,u_pass,u_email))
			 	
		mariadb_connection.commit()
		mariadb_connection.close() 
	except:
		print "error"
  		mariadb_connection.rollback()

elif s=="Sign In":
	u=data.getvalue('user')
	p=data.getvalue('pass')
	if u == 'root' and p == 'redhat':
		print "<META HTTP-EQUIV='refresh' content='0; url=/services.html' />"
		#print "<a href=http://192.168.122.78/services.html>"
		#print " services loading"
		#print " </a> "
	else :
		print "<META HTTP-EQUIV='refresh' content='0; url=/index.html' />"
	

