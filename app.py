import streamlit as st
import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import preprocessing
from preprocessing import Preprocess
import datetime

def get_past_dates(date):
    past_dates = []
    for i in range(7):
        past_date = date - datetime.timedelta(days=i+1)
        past_dates.append(past_date)
    return past_dates

st.title("Farmer's E-Market")

pipe = joblib.load("Pipe1")

input_date = st.date_input('Enter Date')

APMC = st.text_input('Enter APMC Market').title()

Commodity = st.text_input('Enter your Commodity').title()

district_name = st.text_input('Enter District Name').title()

arrivals_in_qtl = st.number_input('Enter Amount in qtl')

min_price = st.number_input('Minimum Price in APMC')

max_price = st.number_input('Maximum Price in APMC')

if st.button('Price is'):
    past_dates = get_past_dates(input_date)

    past_dates_str = []
    predicted_prices = []
    min_prices = []
    max_prices = []

    for past_date in past_dates:
        past_datetime = past_date.strftime('%Y-%m-%d')
        query = [past_datetime, APMC, Commodity, district_name, arrivals_in_qtl,
                 min_price, max_price]

        query = Preprocess(query)
        query = query.reshape(1, 9)

        pred = pipe.predict(query)[0]
        
        past_dates_str.append(past_datetime)
        predicted_prices.append(int(pred))
        min_prices.append(min_price)
        max_prices.append(max_price)

    data = {
        'Date': past_dates_str,
        'Predicted Price': predicted_prices,
        'Min Price': min_prices,
        'Max Price': max_prices
    }
    df = pd.DataFrame(data)
    
    st.title("The predicted Price is " + str(int(predicted_prices[0])))
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Date'], df['Predicted Price'], color='blue', linewidth=2, label='Predicted Price')
    ax.fill_between(df['Date'], df['Min Price'], df['Max Price'], color='lightblue', alpha=0.3, label='Price Range')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Price', fontsize=12)
    ax.set_title('Predicted Prices for the Past 7 Days', fontsize=16, fontweight='bold')
    ax.tick_params(axis='x', rotation=45)
    ax.legend(loc='upper left')
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(fig)
