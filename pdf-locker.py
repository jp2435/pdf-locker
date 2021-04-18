# pip3 install PyPDF2, on console
from PyPDF2 import PdfFileWriter, PdfFileReader

out = PdfFileWriter()

file_path = "sample.pdf"
file = PdfFileReader(file_path)

num = file.numPages
for idx in range(num):
  page = file.getPage(idx)
  out.addPage(page)
  
password = "123456pass"

out.encrypt(password)

with open("encrypted_file.pdf", "wb") as f:
  out.write(f)
