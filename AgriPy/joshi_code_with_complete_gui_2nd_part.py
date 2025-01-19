import requests
import tkinter as tk

def atharva_joshi_2nd_part():
    api_key = '7d1d85373eb3efbf82e1344bc1d21a5b'

    def get_weather():
        user_input = entry.get()
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

        if weather_data.json()['cod'] == '404':
            result_label.config(text="No City Found")
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = weather_data.json()['main']['temp']
            humidity = weather_data.json()['main']['humidity']

            temp_celsius = (temp - 32) * 5 / 9

            result_label.config(text=f"The weather in {user_input} is: {weather}\n"
                                 f"The temperature in {user_input} is: {temp_celsius}ºC\n"
                                 f"The humidity in {user_input} is: {humidity}%")

            if 'rain' in weather_data:
                rainfall = weather_data['rain'].get('3h', weather_data['rain'].get('1h', "Not Available"))
            else:
                result_label.config(text=result_label.cget("text") + f"\nNo rainfall data available for {user_input}")

            moisture_level = humidity
            check_moisture_level(moisture_level)


    def check_moisture_level(moisture_level):
        if 0 <= moisture_level <= 100:
            if moisture_level < 10:
                result_label.config(text=result_label.cget("text") + "\nDry soil. Water the plants.")
            elif 11 <= moisture_level <= 30:
                result_label.config(text=result_label.cget("text") + "\nMoist soil. No need to water now.")
            elif moisture_level > 30:
                result_label.config(text=result_label.cget("text") + "\nWet soil. Avoid overwatering.")
            else:
                result_label.config(text=result_label.cget("text") + "\nCity not found.")


    root = tk.Tk()
    root.title("𝓦𝓮𝓪𝓽𝓱𝓮𝓻 𝓐𝓷𝓭 𝓜𝓸𝓲𝓼𝓽𝓾𝓻𝓮 𝓓𝓮𝓽𝓮𝓬𝓽𝓸𝓻𝓦𝓮𝓪𝓽𝓱𝓮𝓻 𝓐𝓷𝓭 𝓜𝓸𝓲𝓼𝓽𝓾𝓻𝓮 𝓓𝓮𝓽𝓮𝓬𝓽𝓸𝓻")
    root["bg"]="#1C1C1C"
    root.state('zoomed')            #dimensions of window

    label_default_top = tk.Label(root, text="",font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C", borderwidth="5")
    label_default_top.pack(pady = 20)
    
    label = tk.Label(root, text="Enter City:",font = ('Helvetica',20, 'bold'), fg = '#4FA687', borderwidth="5", bg = "#1C1C1C")
    label.pack(pady = 10)

    entry = tk.Entry(root, font = ('Helvetica',15, 'bold'), fg = '#4FA687', borderwidth="5", bg = "#1C1C1C")
    entry.pack(pady = 10)

    button = tk.Button(root, text="Get Weather and Moisture Level", command=get_weather,font = ('Helvetica',15, 'bold'), fg = '#4FA687', borderwidth="5", bg = "#1C1C1C")
    button.pack(pady = 10)

    result_label = tk.Label(root, text="",font = ('Helvetica',15, 'bold'), fg = '#4FA687', borderwidth="5", bg = "#1C1C1C")
    result_label.pack(pady = 10)

    root.mainloop()
    check_moisture_level()
atharva_joshi_2nd_part()