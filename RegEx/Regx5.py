import re

regx = re.compile(r"[a-zA-z]*\s\d{1,2}\.\d{1,2}\.\d{1,5}")

my_list=['ApacheHTTPServer 2.4.49','ApacheTomcat 10.0.11','IBMHTTPServer 9.0.5.4','lighttpd 1.4.63',
		'Jetty 11.0.6','InternetInformationServices 10.0.17763','Nginx 1.21.0','Jexus 6.2.2',
		'OracleHTTPServer 12.2.1','WebserverChrome 0.5.2','Anirudh 1.0' ]

for i in my_list:
	
	if(regx.findall(i)):

		print("Valid Web servers match")

	else:

		print("Invalid web servers match")


