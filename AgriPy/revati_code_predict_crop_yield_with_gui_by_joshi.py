import tkinter as tk
import requests

def revati_aute():
    def get_weather():
        api_key = '7d1d85373eb3efbf82e1344bc1d21a5b'
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

            if 'rain' in weather_data:
                user_rainfall = weather_data['rain'].get('3h', weather_data['rain'].get('1h', "Not Available"))
            else:
                user_rainfall = 0

            predicted_yield = 0.5 * user_rainfall + 1 * temp_celsius - 0.5 * humidity
            result_label.config(text=f"Predicted (Average) Crop Yield : {abs(round(predicted_yield,2))}",font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C")


    root = tk.Tk()
    root.title("𝓟𝓻𝓮𝓭𝓲𝓬𝓽 𝓒𝓻𝓸𝓹 𝓨𝓮𝓲𝓵𝓭",)
    root["bg"]="#1C1C1C"
    root.state("zoomed")

    label_default_top = tk.Label(root, text="",font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C", borderwidth="5")
    label_default_top.pack(pady = 20)

    label = tk.Label(root, text="Enter your City:",font = ('Helvetica',18, 'bold'), fg = '#4FA687', bg = "#1C1C1C", borderwidth="8")
    label.pack(pady = 10)

    entry = tk.Entry(root, font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C", borderwidth="8")
    entry.pack(pady = 10)

    button = tk.Button(root, text="Get Weather and Crop Yield", command=get_weather, font = ('Helvetica',15, 'bold'), fg = '#4FA687',borderwidth="8", bg = "#1C1C1C")
    button.pack(pady = 10)

    result_label = tk.Label(root, text="",font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C", borderwidth="8")
    result_label.pack(pady = 10)

    root.mainloop()
revati_aute()