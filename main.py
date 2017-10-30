import pbs_parser
from datetime import datetime,timedelta

datadir='E:/cygwin/cygwin64/home/lixuqiang/pbs_accounting/prod_data/'
datafile='20170729'
datapath=datadir+datafile
outputpath='E:/cygwin/cygwin64/home/lixuqiang/pbs_accounting/output.txt'
with open(outputpath,'a') as output:
	with open(datapath,'r') as data:
		log=pbs_parser.parse_file(data,True)
		print >>output,log
		output.close()

# print datetime.now()
# start="07/01/2017 07:02:17"
# date=datetime.strptime(start,"%m/%d/%Y %H:%M:%S")
# print date.date()
# pbs_parser.strfdelta(date,"{days}:{hours}:{minutes}:{seconds}")