'''
author: Rohit
date: 20-03-2022
***************************
Convert HTML/webpage to PDF
There are many websites that do not allow to download the content in 
form of pdf, they either ask to buy their premium version or do not have 
such download service in form of pdf.
* Install pdfkit using pip
!pip install pdfkit
* also install WKHTMLTOPDF ans set path varible to binary folder in environment

'''
import pdfkit
pdfkit.from_url('https://www.google.co.in/', 'google.pdf')

'''
Other examples: -
1. import pdfkit
pdfkit.from_file('test.html', 'out.pdf')

2. import pdfkit
pdfkit.from_string('Shaurya GFG','GfG.pdf')

3. pdfkit.from_url(['google.com', 'geeksforgeeks.org', 'facebook.com'], 'shaurya.pdf')
pdfkit.from_file(['file1.html', 'file2.html'], 'out.pdf')

4. # Use False instead of output path to save pdf to a variable
pdf = pdfkit.from_url('http://google.com', False)

'''