#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 03:39:00 2018

@author: yohei
"""

class whether_conditions:
    def __init__(self):
        fin = open('tokyo-weather-20170601-20180531.csv',encoding="shift-jis")
        fin.readline()
        date,hitmp,lotmp,rain,sun = [],[],[],[],[]
        for line in fin:
            lst = line.strip().split(",")
            date.append(lst[0])
            hitmp.append(float(lst[1]))
            lotmp.append(float(lst[2]))
            rain.append(float(lst[3]))
            sun.append(float(lst[4]))
        fin.close()
    def mean_temp(self):
        mean_hitmp = sum(hitmp)/len(hitmp)
        mean_lotmp = sum(lotmp)/len(lotmp)
        return(mean_hitmp,mean_lotmp)
    def max_rainy(self):
        max_rain = max(rain)
        max_index_rain = rain.index(max(rain))
        return(date[max_index_rain],max_rain)
    def sun_times_per_months(self):
        month = []
        for index in range(len(date)):
            buf = date[index].rsplit("/",1)
            month.append(buf[0])
            sort_month = sorted(set(month))
        for index in range(len(sort_month)):
            indexes = [i for i, x in enumerate(month) if x == sort_month[index]]
            monthly_sun = sun[min(indexes):max(indexes)+1]
        return(sort_month[index],sum(monthly_sun)/(len(monthly_sun)))
        
doit = whether_conditions()
print(doit.mean_temp())
print(doit.max_rainy())
print(doit.sun_times_per_months())