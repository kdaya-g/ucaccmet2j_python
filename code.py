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

def monthlytotals(location, monthlist):
    for item in location:
        if item["date"][5:7] == "01":
            monthlist[0] += item["value"]
        elif item["date"][5:7] == "02":
            monthlist[1] += item["value"]
        elif item["date"][5:7] == "03":
            monthlist[2] += item["value"]
        elif item["date"][5:7] == "04":
            monthlist[3] += item["value"]
        elif item["date"][5:7] == "05":
            monthlist[4] += item["value"]
        elif item["date"][5:7] == "06":
            monthlist[5] += item["value"]
        elif item["date"][5:7] == "07":
            monthlist[6] += item["value"]
        elif item["date"][5:7] == "08":
            monthlist[7] += item["value"]
        elif item["date"][5:7] == "09":
            monthlist[8] += item["value"]
        elif item["date"][5:7] == "10":
            monthlist[9] += item["value"]
        elif item["date"][5:7] == "11":
            monthlist[10] += item["value"]
        elif item["date"][5:7] == "12":
            monthlist[11] += item["value"]
# after much testing, I was able to specify characters within a key's value
# and using the '+=' function with the list created above allowed me to create
# monthly totals on specific values, even if the coding itself is very much
# a product of just brute force effort
# defining this type-heavy section as a function saves a lot of time later
# even tho I could just take the code into notepad and use find & replace
seattle_by_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    
# later in the code, I was given an error message unless there were 
# values within the list for the indices I was referencing

monthlytotals(seattle_precipitation, seattle_by_month)

seattle_year = sum(seattle_by_month)

seattle_relative = []
# for a list of the percentages throughout the year
for item in seattle_by_month:
    seattle_relative.append(item/seattle_year)

# SAME BUT FOR CINCINNATI
cin_precipitation = []

for item in rain:
    if item["station"] == "GHCND:USW00093814":
        cin_precipitation.append(item)

cin_by_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    

monthlytotals(cin_precipitation, cin_by_month)

cin_year = sum(cin_by_month)

cin_relative = []

for item in cin_by_month:
    cin_relative.append(item/cin_year)

# SAME BUT FOR MAUI
maui_precipitation = []

for item in rain:
    if item["station"] == "GHCND:USC00513317":
        maui_precipitation.append(item)

maui_by_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    

monthlytotals(maui_precipitation, maui_by_month)

maui_year = sum(maui_by_month)

maui_relative = []

for item in maui_by_month:
    maui_relative.append(item/maui_year)
    
# SAME BUT FOR SAN DIEGO    
san_diego_precipitation = []

for item in rain:
    if item["station"] == "GHCND:US1CASD0032":
        san_diego_precipitation.append(item)

san_diego_by_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    

monthlytotals(san_diego_precipitation, san_diego_by_month)

san_diego_year = sum(san_diego_by_month)

san_diego_relative = []

for item in san_diego_by_month:
    san_diego_relative.append(item/san_diego_year)

# FOR ANNUAL DISTRIBUTION    
all_year = [seattle_year, cin_year, maui_year, san_diego_year]
total_precipitation_year = sum(all_year)
total_relative = []

for item in all_year:
    total_relative.append(item/total_precipitation_year)