'''psuedo

ask for permission to collect information with note on what we do with info
ask for steps done before or any screenshots of what is happening or not happening
what has been tried (histoy)


find and get logs from past 2 days
gather troubleshooting info with sync stuff highlighted
last modified date of sign on

highlight any error in log

send to destinstion for  request
send thank you for submitting and disclaimer that we do not get back to everyone]

SANITIZE DATA
HIGHLIGHGT ERROR DEBUG

where to submit it (remember that you are going to need a privacy bug and )
'''

import os.path, time
import glob, datetime
import inspect

#filepath = 'file:///Users/rmcguigan/Library/Application Support/Firefox/Profiles/l29owbc9.Rachel/weave/logs/'


#print "last modified: %s" % time.ctime(os.path.getmtime(filepath))
def error(k):
	fo = open(k, "rw+")
	for w in fo: 
		if w.find('Error') != -1:
			print w
			info = inspect.getframeinfo(w)
			print info.lineno
	fo.close()
def sanitize(k):
	'''This is meant to take out personalized data in the logs'''

	"https://sync-"

def main():

	#store recent files modified in the last 2 days
	#lsit of file names

	file_names = []
	#if script is in the weave folder -> later likely going to be in the extensions folder of the profile
	file_names = glob.glob("logs/*.txt")
	#print glob.glob("logs/*.txt")
	#print list of last modiefed'
	for i in file_names:
		print "last modified: %s" % time.ctime(os.path.getmtime(i))
		
	for x in file_names: 
		error(x)


if __name__ == '__main__':
	main()
 