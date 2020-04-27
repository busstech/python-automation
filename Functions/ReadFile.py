# Function - Open a file
inputFile = open('../Files/Students.txt', 'r')  # Specify the file to read

count = 0                                       # count each line and start at id 0 (or first line)

for line in inputFile:                          # iterate over every line in the file
    print(str(count) + line)                    # print line number and record
    count = count + 1                           # for every record increment by 1

inputFile.close()                               # close the file
