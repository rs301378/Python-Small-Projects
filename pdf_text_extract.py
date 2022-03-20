'''
author: Rohit
date: 20/03/2022
*********************************
Install PyPDF2 package using pip
!pip install PyPDF2
*********************************
'''
import PyPDF2
#create pdf file obj
pdf_obj = open('example.pdf', 'rb')
#create pdf reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
print(pdf_reader.numPages)
page_obj = pdf_reader.getPage(2)
#extract text from pdf
print(page_obj.extractText())
#close pdf file object
pdf_obj.close()