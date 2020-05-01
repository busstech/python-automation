# Function - Open a file
# 1.    Standard reading of a file
# inputFile = open('../Files/Students.txt', 'r')  # Specify the file to read
# print(inputFile.read())                         # Print each row as it's read
# inputFile.close()                               # Close the file being read

# 2.    Reading of a file and adding the line numbers before the row
# inputFile = open('../Files/Students.txt', 'r')  # Specify the file to read
# count = 0                                       # count each line and start at id 0 (or first line)
# for line in inputFile:                          # iterate over every line in the file
#     print(str(count) + line)                    # print line number and record
#     count = count + 1                           # for every record increment by 1
# inputFile.close()                               # close the file

# 3.    Print the line count for each row in the file
# inputFile = open('../Files/Students.txt', 'r')  # Specify the file to read
# count = 0                                       # count each line and start at id 0 (or first line)
# for line in inputFile:                          # iterate over every line in the file
#     count = count + 1                           # for every record increment by 1
#     print(count)                              # print line number and record
# inputFile.close()                               # close the file

# 4.    Inspect a file
import inspect
import os

f = inspect.currentframe()
i = inspect.getframeinfo(f)
print(i.lineno)
print(i.filename)
print(i.function)
