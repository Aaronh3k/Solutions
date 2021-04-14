import requests
import json
import xlsxwriter

response=requests.get('https://606f76d385c3f0001746e93d.mockapi.io/api/v1/auditlog').json()

headers=response[0].keys()

workbook = xlsxwriter.Workbook('Demo.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})

row = 0
col = 0

for header in headers:
    worksheet.write(row,col,header,bold)
    col += 1

row=1

for items in response:
    worksheet.write(row,0,items['id'])
    worksheet.write(row,1,items['description'])
    worksheet.write(row,2,items['date'])
    worksheet.write(row,3,items['action'])
    worksheet.write(row,4,items['user_id'])
    worksheet.write(row,5,items['criticality'])
    row+=1

workbook.close()
