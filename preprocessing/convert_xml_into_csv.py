# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup as Soup
from datetime import datetime
import codecs
import csv
import os



XML_FILE = os.path.join(os.path.dirname(__file__), "..","raw-data","RecallsDataSet.xml")
CSV_FILE = os.path.join(os.path.dirname(__file__), "..","raw-data","RecallsDataSet.csv")

handler = codecs.open(XML_FILE,'r','utf-8').read()
soup = Soup(handler)
cnt = 0;

columns = ['reason','company','product_descrpition','brand_name','date']
with codecs.open(CSV_FILE, 'wb','utf-8') as output_file:
    file_writer = csv.writer(output_file)
    file_writer.writerow(columns)
    for product in soup.findAll('product'):
        
        date = datetime.strptime(product.find('date').contents[0], '%a, %d %b %Y %H:%M:%S -%f')
        reason = product.find('reason').contents[0].strip()
        product_description = product.find('product_description').contents[0].strip()
        company = product.find('company').contents[0].strip()
        brand_name = product.find('brand_name').contents[0].strip()
        cnt = cnt+1
        file_writer.writerow([reason,company,product_description,brand_name,date.strftime('%m/%Y')])