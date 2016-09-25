import csv
import sys

infile = sys.argv[1]

#  okay, now we have the file name. Open it up and figure out what the fieldnames are; just read the first line and split it by delimiter

def get_fieldnames():
    with open(infile) as inf:
        first_line = inf.readline()
        return first_line.split(",")# might want to prompt for custom delimeter
fieldnames = get_fieldnames()
fname_ids = [d for d in zip(range(len(fieldnames)), fieldnames)]

# now ask user which ones to code:
def select_fnames():
    print("coding "  + str(infile.split("/")[-1:]))
    print("which fields do you want to code?")
    for key, value in fname_ids:
        print((key, value))
    print("separate by comma")
fieldnames_to_code = [int(n) for n in input().split(",")]
print("Coding: ")
fieldnames_to_code = select_fnames()
print(str(fieldnames_to_code))
for f in fieldnames_to_code:
    print(str(f), fname_ids[f])
