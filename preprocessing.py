import pandas as pd
import numpy as np


#	Date  APMC	Commodity	district_name, arrivals_in_qtl	min_price	max_price  
# APMC	Commodity	district_name	arrivals_in_qtl_METHOD	min_price_METHOD	max_price_METHOD	year_METHOD	month_METHOD	day_METHOD
def Preprocess(row):
    
    date = pd.to_datetime(row[0])
    year = date.year
    month = date.month
    day = date.day
    APMC = row[1]
    Commodity = row[2]
    district_name = row[3]
    arrivals_in_qtl = row[4]
    min_price = row[5]
    max_price = row[6]

    columns = np.array([APMC, Commodity, district_name, arrivals_in_qtl, min_price,
                        max_price, year, month, day])

    return columns