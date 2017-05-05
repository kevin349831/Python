#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:06:04 2017

@author: haoyu
"""
#回收期
print("********************************************************************************")
print()
print("回收期間法")
print()

FP = 30000000 #本金
years = 6 #年數
CFi = 6500000 #現金流量
temp = FP;
print("年度\t每年現金流入量\t累積現金流量")
print("----------------------------------------")
print("0\t$(",FP,")\t$(",FP,")")
print("----------------------------------------")
for i in range(years):
    i=i+1
    FP -= CFi
    if FP > 0:
        print(i,"\t$",CFi,"\t$(",FP,")")
    else:
        print(i,"\t$",CFi,"\t$",FP*-1)
    print("----------------------------------------")

temp = round(temp/CFi,3)#計算回正年數
print("回收期間=",temp,"年")

print()
print("********************************************************************************")
print()
#折現回收期
print("折現回收期間法")
print()

FP = 30000000 #本金
years = 6 #年數
CFi = 6500000 #現金流量
k = 0.08 #折現因子---折現率
temp_FP = FP
count = 0 
temp_year = 0
print("年度\t每年現金流入量\t  折現因子(",round(k*100),"%)   \t現金流量折現因子\t累積現金流量折現值")
print("----------------------------------------------------------------------------------")
print("0\t$(",FP,")\t 1      \t$(",FP,")","\t$(",FP,")")
print("----------------------------------------------------------------------------------")
for i in range(years):
    temp_year = temp_FP
    i=i+1
    ss = round((CFi/((1+k)**i))-temp_FP)
    temp_FP = round(temp_FP+ss)
    temp_k = round(temp_FP/CFi,4)
    if ss < 0:
        print(i,"\t$",CFi,"\t",temp_k," \t$",temp_FP,"\t$(",ss*-1,")")
        count = count + 1
    else:
        print(i,"\t$",CFi,"\t",temp_k," \t$",temp_FP,"\t$",ss)
        temp_year = round(temp_year/temp_FP,4)
    temp_FP = ss*-1
    print("----------------------------------------------------------------------------------")
print("折現回收期間＝",count+temp_year)
print()
print("********************************************************************************")
