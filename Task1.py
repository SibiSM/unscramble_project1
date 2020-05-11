"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""


def len_uniquenumbers(d):
    unique_num = set()
    for i in d:
        n1 = i[0]
        n2 = i[1]
        unique_num.add(n1)
        unique_num.add(n2)
    return len(unique_num)


def answer():
    d = texts + calls
    count = len_uniquenumbers(d)
    print(F"There are {count} different telephone numbers in the records.")


answer()
