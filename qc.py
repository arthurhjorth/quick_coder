import csv
import sys

infile = sys.argv[1]

#  okay, now we have the file name. Open it up and figure out what the fieldnames are; just read the first line and split it by delimiter
fieldnames = []
with open(infile) as inf:
    first_line = inf.readline()
    fieldnames = first_line.split(",")# might want to prompt for custom delimeter
fname_ids = zip(fieldnames, range(len(fieldnames)))

# now ask user which ones to code:
print("coding "  + str(infile.split("/")[-1:]))
print("which fields do you want to code?")
for fname in fname_ids:
    print(str(fname[1]) + " : " + str(fname[0]))

fieldnames_to_code = input()

# reader = csv.DictReader(open(sys.argv[1]))
# print(reader.next())


# fieldname = sys.argv[2]
# new_fieldnames = sys.argv[3:]
# entries = [e for e in reader]
# out_entries = []
# for e in entries:
#     print(e[fieldname])
#     for f in new_fieldnames:
#         print("old value: " + e[f])
#         e.update({str(f) : input(str(f))})
#     out_entries.append(e)
# outfile = open(sys.argv[1] + '_out', 'w')
# writer = csv.DictWriter() # this is not going to work because we don't write the headers
# writer.write(out_entries)
# outfile.close()
