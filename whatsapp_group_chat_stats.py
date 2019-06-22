# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 18:03:41 2019

@author: 2420412z
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:16:50 2019

@author: 2420412z
"""
import re
import os
import collections

watsup_file = 'ktl_chat.txt'
if os.path.exists(watsup_file):
        file_data = open(watsup_file,'r', encoding="utf8")
        content = file_data.read() 
    
dates = re.findall('\d+\/\d+\/\d+', content)
years = re.findall('\/\d+,', content)
hours = re.findall(',\s\d+:', content)

results_days = (collections.Counter(dates).most_common(20))
results_years = (collections.Counter(years).most_common(5))
results_hours = (collections.Counter(hours).most_common())

for elem_days in results_days:
    print(elem_days)

for elem_years in results_years:
    print(elem_years)
    
for elem_hours in results_hours:
    print(elem_hours)
