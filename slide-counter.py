from pyPdf import PdfFileReader
import sys
import os


def printUsage():
    print "Usage: " + sys.argv[0] + " directory"
    print "---------------------------------"
    print "directory: path to directory containing PDFs"
    return


def truncateString(str):
    return (str[:58] + '..') if len(str) > 60 else str


if(len(sys.argv) != 2):
    printUsage()
    sys.exit()

sumPages = 0
for i in os.listdir(sys.argv[1]):
    if i.upper().endswith(".PDF"):
        pdf = PdfFileReader(open(sys.argv[1] + i, 'rb'))
        numPages = pdf.getNumPages()
        sumPages += numPages
        print truncateString(str(i)).ljust(65, ' ') + str(numPages).rjust(5, ' ')
        continue
    else:
        print i
        continue

print '-' * 75
print "Total Pages: " + str(sumPages)
