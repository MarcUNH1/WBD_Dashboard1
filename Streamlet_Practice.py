import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt
from numpy.random import default_rng as rng

#alt.theme.enable("dark")

st.set_page_config(
    page_title="WBD Buoy Dashboard",
    layout="wide",
    initial_sidebar_state="expanded")

#data = pd.read_csv(r"C:\Users\maj266\Offline\Streamlit_Stuff\test_data_csv.csv")
data = pd.read_csv(r"test_data_csv.csv")
data['Time'] = pd.to_datetime(data['Time'])

col = st.columns((.5, .4, 1), gap='medium')

with col[0]:
    #    st.image(r"C:\Users\maj266\Offline\Streamlit_Stuff\buoy.png", caption="UNH WBD Buoy", )
    st.image(r"buoy.png", caption="UNH WBD Buoy", )
    st.table(
        {
            "first column": ["Site elevation:", "Air temp height:", "Anemometer height:", "Barometer elevation:",
                             "Sea temp depth:", "Water depth:", "Watch circle radius:"],
            "second column": ["Sea Level", "+3m", "+3m", "+3m", "-1m", "70m", "70m"],
        }, hide_header=True, border=False
    )
with col[1]:
    df_map = pd.DataFrame(
        {
            "lat": 43.02,
            "lon": -70.54,
        },
        index=([1, 2]))

    st.map(df_map, latitude="col1", longitude="col2", size=100, zoom=8, height=200)

    st.table(
        {
            "first column": ["Sinker Location", "Latest Location:", "Latest Telemetry:"],
            "second column": ["43.02°N, 70.54°W", "43.02°N, 70.54°W", "2026-04-28 08:00:00Z"],
        }, hide_header=True, border=False, height=120
    )

    st.markdown("###### Data As Of 2026-04-28 08:00:00Z", text_alignment="center", width="stretch")
    recent = st.table(data.iloc[-1, [1, 2, 3, 4, 5, 6, 7, 8]], hide_header=True)

with col[2]:
    #    df = rng(0).standard_normal((10, 1))
    st.title("Past 24 Hours")
    t1, t2, t3, t4, t5, t6, t7, t8 = st.tabs(["WSPD", "WDIR", "AirT", "AirP", "rH", "WaterT", "SigH", "Tp1"])
    all_timestamps = []
    all_timestamps.append(data['Time'])
    print(data['Time'].min().timestamp())
    print(data['Time'].max().timestamp())
    t1.subheader("Wind Speed")
    fig_wspd = px.line(data, x="Time", y="wSPD")
    fig_wspd.update_xaxes(
        range=[data['Time'].min(), data['Time'].max()],
        minallowed=data['Time'].min(),
        maxallowed=data['Time'].max()
    )

    t1.plotly_chart(fig_wspd, use_container_width=True, height=500)

    t2.subheader("Wind Direction")
    fig_wdir = px.line(data, x="Time", y="wDIR")
    t2.plotly_chart(fig_wdir, use_container_width=True, height=500)

    t3.subheader("Air Temperature")
    fig_airT = px.line(data, x="Time", y="AirT")
    t3.plotly_chart(fig_airT, use_container_width=True, height=500)

    t4.subheader("Atmospheric Pressure")
    fig_airP = px.line(data, x="Time", y="AirP")
    t4.plotly_chart(fig_airP, use_container_width=True, height=500)

    t5.subheader("Relative Humidity")
    fig_rh = px.line(data, x="Time", y="rH")
    t5.plotly_chart(fig_rh, use_container_width=True, height=500)

    t6.subheader("Water Temperature")
    fig_seaT = px.line(data, x="Time", y="WaterT")
    t6.plotly_chart(fig_seaT, use_container_width=True, height=500)

    t7.subheader("Significant Wave Height")
    fig_sigh = px.line(data, x="Time", y="SigH")
    t7.plotly_chart(fig_sigh, use_container_width=True, height=500)

    t8.subheader("Wave Peak Spectral Period")
    fig_tp1 = px.line(data, x="Time", y="Tp1")
    t8.plotly_chart(fig_tp1, use_container_width=True, height=500)
