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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def bangalore_call(call):
    return call[0][0:5] == '(080)'


def area_code(call):
    other = call[1]

    if other[:2] == '(0':
        return other.split(sep=')')[0] + ')'

    if other[:3] == '140':
        return other[:3]

    else:
        return other[:4]


if __name__ == '__main__':
    bang_call = []
    # Part A
    for call in calls:
        if bangalore_call(call):
            bang_call.append(area_code(call))

    list = list(set(bang_call))
    list.sort()

    print("\n The numbers called by people in Bangalore have codes:")
    for i in list:
        print(i)

    # Part B
    bangalore = 0
    for num in bang_call:
        if num == "(080)":
            bangalore += 1

    percentage=round(bangalore / len(bang_call) * 100, 2)
    print("\n {} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format)