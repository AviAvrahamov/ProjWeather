import requests
import streamlit as st

temperature = 0   # main > temperature - 273.15
weather = ''   # temperature  > temperature
conditions = ''
humidity = 0   # main > temperature

txt1 = st.text_input("please enter City")
if txt1:
    txt2 = st.text_input("Enter some more text")




inputCity = input("please enter City: ")
inputCity = 'Berlin'
response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + inputCity +"&APPID=5b9ee17e7a2c2221a87953b1b3562db9")
if response.status_code != 200:
    print("wrong input")
else:
    jsonBody = response.json()
    # data = json.loads(jsonBody)
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


st.write(f"temperature : {temp}")
st.write(f"humidity : {humidity}")
st.write(f"main : {main}")
st.write(f"humidity : {conditions}")

# print('temperature : ' , temp)
# print('humidity : ' , humidity)
# print('main : ' + main)
# print('humidity : ' + conditions  )



#  C:\Users\F8C0~1\AppData\Roaming\Python\Scripts