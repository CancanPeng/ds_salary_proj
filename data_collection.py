#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 11:04:43 2020

@author: pengcancan
"""

import glassdoor_scraper as gs
import pandas as pd

path = "/Users/pengcancan/Workspace/ds/ds_salary_proj/chromedriver"

df = gs.get_jobs("data_scientist",2,False,path,5);