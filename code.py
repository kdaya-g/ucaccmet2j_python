# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:37:10 2018

@author: Kyle
"""

import json

with open("precipitation.json") as file:
    rain = json.load(file)
   
seattle_precipitation = []

for item in rain:
    if item["station"] == "GHCND:US1WAKG0038":
        seattle_precipitation.append(item)

seattle_by_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    

for item in seattle_precipitation:
    if item["date"][5:7] == "01":
        seattle_by_month[0] += item["value"]
    elif item["date"][5:7] == "02":
        seattle_by_month[1] += item["value"]
    elif item["date"][5:7] == "03":
        seattle_by_month[2] += item["value"]
    elif item["date"][5:7] == "04":
        seattle_by_month[3] += item["value"]
    elif item["date"][5:7] == "05":
        seattle_by_month[4] += item["value"]
    elif item["date"][5:7] == "06":
        seattle_by_month[5] += item["value"]
    elif item["date"][5:7] == "07":
        seattle_by_month[6] += item["value"]
    elif item["date"][5:7] == "08":
        seattle_by_month[7] += item["value"]
    elif item["date"][5:7] == "09":
        seattle_by_month[8] += item["value"]
    elif item["date"][5:7] == "10":
        seattle_by_month[9] += item["value"]
    elif item["date"][5:7] == "11":
        seattle_by_month[10] += item["value"]
    elif item["date"][5:7] == "12":
        seattle_by_month[11] += item["value"]

seattle_year = sum(seattle_by_month)

seattle_relative = []

for item in seattle_by_month:
    seattle_relative.append(item/seattle_year)

cin_precipitation = []

for item in rain:
    if item["station"] == "GHCND:USW00093814":
        cin_precipitation.append(item)

cin_by_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    

for item in cin_precipitation:
    if item["date"][5:7] == "01":
        cin_by_month[0] += item["value"]
    elif item["date"][5:7] == "02":
        cin_by_month[1] += item["value"]
    elif item["date"][5:7] == "03":
        cin_by_month[2] += item["value"]
    elif item["date"][5:7] == "04":
        cin_by_month[3] += item["value"]
    elif item["date"][5:7] == "05":
        cin_by_month[4] += item["value"]
    elif item["date"][5:7] == "06":
        cin_by_month[5] += item["value"]
    elif item["date"][5:7] == "07":
        cin_by_month[6] += item["value"]
    elif item["date"][5:7] == "08":
        cin_by_month[7] += item["value"]
    elif item["date"][5:7] == "09":
        cin_by_month[8] += item["value"]
    elif item["date"][5:7] == "10":
        cin_by_month[9] += item["value"]
    elif item["date"][5:7] == "11":
        cin_by_month[10] += item["value"]
    elif item["date"][5:7] == "12":
        cin_by_month[11] += item["value"]

cin_year = sum(cin_by_month)

cin_relative = []

for item in cin_by_month:
    cin_relative.append(item/cin_year)

maui_precipitation = []

for item in rain:
    if item["station"] == "GHCND:USC00513317":
        maui_precipitation.append(item)

maui_by_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    

for item in maui_precipitation:
    if item["date"][5:7] == "01":
        maui_by_month[0] += item["value"]
    elif item["date"][5:7] == "02":
        maui_by_month[1] += item["value"]
    elif item["date"][5:7] == "03":
        maui_by_month[2] += item["value"]
    elif item["date"][5:7] == "04":
        maui_by_month[3] += item["value"]
    elif item["date"][5:7] == "05":
        maui_by_month[4] += item["value"]
    elif item["date"][5:7] == "06":
        maui_by_month[5] += item["value"]
    elif item["date"][5:7] == "07":
        maui_by_month[6] += item["value"]
    elif item["date"][5:7] == "08":
        maui_by_month[7] += item["value"]
    elif item["date"][5:7] == "09":
        maui_by_month[8] += item["value"]
    elif item["date"][5:7] == "10":
        maui_by_month[9] += item["value"]
    elif item["date"][5:7] == "11":
        maui_by_month[10] += item["value"]
    elif item["date"][5:7] == "12":
        maui_by_month[11] += item["value"]

maui_year = sum(maui_by_month)

maui_relative = []

for item in maui_by_month:
    maui_relative.append(item/maui_year)
    
san_diego_precipitation = []

for item in rain:
    if item["station"] == "GHCND:US1CASD0032":
        san_diego_precipitation.append(item)

san_diego_by_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    

for item in san_diego_precipitation:
    if item["date"][5:7] == "01":
        san_diego_by_month[0] += item["value"]
    elif item["date"][5:7] == "02":
        san_diego_by_month[1] += item["value"]
    elif item["date"][5:7] == "03":
        san_diego_by_month[2] += item["value"]
    elif item["date"][5:7] == "04":
        san_diego_by_month[3] += item["value"]
    elif item["date"][5:7] == "05":
        san_diego_by_month[4] += item["value"]
    elif item["date"][5:7] == "06":
        san_diego_by_month[5] += item["value"]
    elif item["date"][5:7] == "07":
        san_diego_by_month[6] += item["value"]
    elif item["date"][5:7] == "08":
        san_diego_by_month[7] += item["value"]
    elif item["date"][5:7] == "09":
        san_diego_by_month[8] += item["value"]
    elif item["date"][5:7] == "10":
        san_diego_by_month[9] += item["value"]
    elif item["date"][5:7] == "11":
        san_diego_by_month[10] += item["value"]
    elif item["date"][5:7] == "12":
        san_diego_by_month[11] += item["value"]

san_diego_year = sum(san_diego_by_month)

san_diego_relative = []

for item in san_diego_by_month:
    san_diego_relative.append(item/san_diego_year)
    
all_year = [seattle_year, cin_year, maui_year, san_diego_year]
total_precipitation_year = sum(all_year)
total_relative = []

for item in all_year:
    total_relative.append(item/total_precipitation_year)
