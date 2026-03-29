from Scraper import scrape_table_td
from datetime import date
import os

today = str(date.today())
day = today[8] + today[9] + '.' +today[5] + today[6] + '.' + today[0] + today[1] + today[2] + today[3]
url_eu = "https://cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.so=1&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=R01239&UniDbQuery.From="+day+"&UniDbQuery.To="+day
table_data_eu = scrape_table_td(url_eu)
url_us = "https://cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.so=1&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=R01235&UniDbQuery.From="+day+"&UniDbQuery.To="+day
table_data_us = scrape_table_td(url_us)
url_cn = "https://cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.so=1&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=R01375&UniDbQuery.From="+day+"&UniDbQuery.To="+day
table_data_cn = scrape_table_td(url_cn)
eu = (table_data_eu[2][2])[0] + (table_data_eu[2][2])[1] + '.' + (table_data_eu[2][2])[3] + (table_data_eu[2][2])[4] + (table_data_eu[2][2])[5] + (table_data_eu[2][2])[6]
us = (table_data_us[2][2])[0] + (table_data_us[2][2])[1] + '.' + (table_data_us[2][2])[3] + (table_data_us[2][2])[4] + (table_data_us[2][2])[5] + (table_data_us[2][2])[6]
cn = (table_data_cn[2][2])[0] + (table_data_cn[2][2])[1] + '.' + (table_data_cn[2][2])[3] + (table_data_cn[2][2])[4] + (table_data_cn[2][2])[5] + (table_data_cn[2][2])[6]
current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
file_money = open(current_directory+'/History.py', 'r')
our_file=str(*file_money)
list_day = []
list_eu = []
list_us = []
list_cn = []
str_app = ''
writer = False
chosen = 1
sw = 3
for ix in range(len(our_file)):
    if sw == 0:
        writer = True
        sw = 3
    if sw == 1:
        sw = 0
    if sw == 2:
        sw = 1
    if our_file[ix] == ']':
        writer = False
        chosen += 1
    if our_file[ix] == ',':
        writer = False
        if our_file[ix + 1] == ']':
            sw = 2
        else:
            sw = 0
        if len(str_app)>0:
            if chosen == 1:
                list_day.append(str_app)
            if chosen == 2:
                list_eu.append(float(str_app))
            if chosen == 3:
                list_us.append(float(str_app))    
            if chosen == 4:
                list_cn.append(float(str_app))
            str_app=''
    if writer == True:
        str_app = str_app + our_file[ix]
    if our_file[ix] == '[':
        writer = True
'''
Добавление курсов сегодняшнего дня
if float(eu) != list_eu[len(list_eu) - 1]:
    list_day.append(day)
    list_eu.append(float(eu))
    list_us.append(float(us))
    list_cn.append(float(cn))
'''
add_string = str(list_day) + str(list_eu) + str(list_us) + str(list_cn)
acq_string=''
for iy in range(len(add_string)):
    if add_string[iy] == ' ':
        acq_string = acq_string
    elif add_string[iy] == "'":
        acq_string = acq_string
    elif add_string[iy] == ']':
        acq_string = acq_string + ',]'
    else:
        acq_string = acq_string + add_string[iy]
file_money.close()
file_writer = open(current_directory+'/History.py', 'w')
file_writer.write(acq_string)

file_writer.close()
