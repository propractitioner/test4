# 파일명: app.py
import streamlit as st
from astropy.coordinates import get_sun, get_moon, EarthLocation
from astropy.time import Time
import matplotlib.pyplot as plt
from datetime import datetime

# 위치 설정 (예: 서울)
location = EarthLocation(lat=37.5665, lon=126.9780)

# 현재 시간
time = Time(datetime.utcnow())

# 태양과 달의 위치
sun = get_sun(time).transform_to('altaz', obstime=time, location=location)
moon = get_moon(time).transform_to('altaz', obstime=time, location=location)

# Streamlit 앱
st.title("오늘 밤하늘의 별자리")

# 태양과 달의 위치 표시
st.write(f"Sun's Altitude: {sun.alt:.2f}, Azimuth: {sun.az:.2f}")
st.write(f"Moon's Altitude: {moon.alt:.2f}, Azimuth: {moon.az:.2f}")

# 밤하늘의 별자리 표시
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(sun.az.deg, sun.alt.deg, color='orange', label='Sun')
ax.scatter(moon.az.deg, moon.alt.deg, color='gray', label='Moon')
ax.set_xlim(0, 360)
ax.set_ylim(-90, 90)
ax.set_xlabel('Azimuth (degrees)')
ax.set_ylabel('Altitude (degrees)')
ax.legend()

st.pyplot(fig)
