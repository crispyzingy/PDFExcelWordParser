import PyPDF2
import os

# --------------------
# read pdf files
# --------------------

# os.chdir("c:\\users\\crisp\\Documents") #pdf file location, if not in cwd
pdfFile = open("meetingminutes.pdf", "rb")  # rb: read binary mode
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)
page = reader.getPage(0)
print(page.extractText())

# for all pages
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())
