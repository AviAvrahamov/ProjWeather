import requests
import streamlit as st

temperature = 0   # main > temperature - 273.15
weather = ''   # temperature  > temperature
conditions = ''
humidity = 0   # main > temperature

inputCity = st.text_input(r"$\textsf{\Huge Please enter city}$")

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + inputCity +"&APPID=5b9ee17e7a2c2221a87953b1b3562db9")
if response.status_code != 200:
    st.write("wrong input")
else:
    jsonBody = response.json()
    main = jsonBody.get("main")
    if main:
        temp = main.get("temp") - 273.15
        humidity = main.get("humidity")

    weatherL = jsonBody.get("weather")
    if weatherL:
        # print(weatherL)
        mainL = weatherL[0]
        main = mainL.get("id")
        main = mainL.get("main")
        conditions = mainL.get('description')

    st.write("temperature :  {0:.1f}".format(temp))
    st.write(f"humidity : {humidity}")
    st.write(f"main : {main}")
    st.write(f"humidity : {conditions}")

#  C:\Users\F8C0~1\AppData\Roaming\Python\Scripts