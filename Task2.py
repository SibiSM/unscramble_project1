"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
ph={}
for each in calls:
	if each[0] not in ph:
		ph[each[0]]=int(each[3])
	elif each[0] in ph:
		ph[each[0]]+=int(each[3])
	if each[1] not in ph:
		ph[each[1]]=int(each[3])
	elif each[1] in ph:
		ph[each[1]]+=int(each[3])
longest= max(ph.items(), key=lambda x: x[1])
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(*longest))