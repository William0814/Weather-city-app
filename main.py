import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from functions import get_data


st.set_page_config(page_title="Weather Page", page_icon="images/cloudy.png")
st.title("Weather :blue[Forecast for the Days]")

place = st.text_input("Place:", placeholder="Enter a city")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecast days")

option = st.selectbox('Select data to view', placeholder='Select',
                       options=('', 'Sky', "Temperature"))

st.subheader(f'{option} for the next {days} days in {place}')
try:
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] / 20 for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {'Clouds':'images/cloud.png', 'Clear':'images/clear.png', 
                'Rain':'images/rain.png', 'Snow':'images/snow.png' }
        sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
        image_path = [images[condition] for condition in sky_conditions]
        st.image(image_path, width=150, caption=sky_conditions)
except KeyError:
    st.info("Place invalid, example: Berlin")