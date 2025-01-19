#Manas's Crop Simulation with GUI Final 1
import requests
import math
import tkinter as tk
from tkinter import messagebox

def manas_kulkarni_crop_simulation():
    
    def get_weather_data(api_key, user_input):
   
        if not user_input:
            messagebox.showerror("Error", "Please enter a city name.")
            return None

        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

        if weather_data.json()['cod'] == '404':
            messagebox.showerror("Error", "No City Found. Please enter a valid city name.")
            return None
        else:
            return weather_data.json()


    def weather():
        global user_input, weather_data
        api_key = '7d1d85373eb3efbf82e1344bc1d21a5b'
        user_input = city_entry.get()

        weather_data = get_weather_data(api_key, user_input)

        if weather_data:
            weather = weather_data['weather'][0]['main']
            temp = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
        
            if 'rain' in weather_data:
                rainfall = weather_data['rain'].get('3h', weather_data['rain'].get('1h', "Not Available"))
            else:
                rainfall = "Not Available"

            temp_celsius = (temp - 32) * 5/9

            weather_label.config(text=f"The Weather in {user_input} is: {weather}")
            temp_label.config(text=f"The Temperature in {user_input} is: {round(temp_celsius,2)}ºC")
            humidity_label.config(text=f"The Humidity in {user_input} is: {humidity}%")
            rainfall_label.config(text=f"The Rainfall in {user_input} is (in mm): {rainfall}")

        return user_input, weather_data


    def CropSimulation(user_input, weather_data):
        global window
        if weather_data:
            try:
            
                initial_height = float(height_entry.get())
                growth_rate = float(growth_rate_entry.get())
                temperature = (weather_data['main']['temp'] - 32) * 5/9  
                soil_moisture = weather_data['main']['humidity']

                if 'rain' in weather_data:
                    rainfall = weather_data['rain'].get('3h', weather_data['rain'].get('1h', "Not Available"))
                else:
                    rainfall = 0

                number_of_days = int(days_entry.get())

            
                def calculate_daily_growth(temperature, rainfall, soil_moisture):
                
                    temperature_factor = math.exp(0.1 * (temperature - 25))
                    rainfall_factor = math.exp(0.05 * (rainfall - 50))

                    soil_moisture_factor = math.exp(0.2 * (soil_moisture - 60))
                    daily_growth = growth_rate * temperature_factor * rainfall_factor * soil_moisture_factor

                    return daily_growth

                current_height = initial_height

                for day in range(number_of_days):
                
                    daily_growth = calculate_daily_growth(temperature, rainfall, soil_moisture)
                    current_height += daily_growth

           
                window.destroy()

                output_window = tk.Tk()
                output_window.configure(bg='#1C1C1C')

                # Update idle tasks before getting the window dimensions
                output_window.update_idletasks()

                
                screen_width = output_window.winfo_screenwidth()
                screen_height = output_window.winfo_screenheight()

                
                window_width = 500
                window_height = 250

                
                position_top = int(screen_height / 2 - window_height / 2)
                position_right = int(screen_width / 2 - window_width / 2)

                
                output_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
               

                result_label = tk.Label(output_window, text=f"The Final Crop Height is {round(current_height,2)} cm.", bg='#1C1C1C', fg='#4FA687', font=("Helvetica", 11, "bold"))
                result_label.place(relx=0.5, rely=0.4, anchor='center')

                close_button = tk.Button(output_window, text="Close", command=output_window.destroy, bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 11,'bold'))
                close_button.place(relx=0.5, rely=0.7, anchor='center')

                output_window.mainloop()

            except ValueError:
            
                messagebox.showerror("Error", "Invalid input. Please enter the data again.")
        else:
            messagebox.showerror("Error", "Please fetch the weather data first.")


    def next_window():
        global height_entry, growth_rate_entry, days_entry, result_label, window
        if 'weather_data' in globals():
            root.destroy()
            window = tk.Tk()
            window.configure(bg='#1C1C1C')
            window.geometry("500x500")  
            window.title("Crop Simulation")

            window_width = 500
            window_height = 500
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            position_top = int(screen_height / 2 - window_height / 2)
            position_right = int(screen_width / 2 - window_width / 2)
            window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

            height_label = tk.Label(window, text="Enter the initial crop height in cm: ", bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 11,'bold'))
            height_label.place(relx=0.5, rely=0.2, anchor='center')
            height_entry = tk.Entry(window, font=('Helvetica', 11,'bold'))
            height_entry.place(relx=0.5, rely=0.3, anchor='center')

            growth_rate_label = tk.Label(window, text="Enter the crop growth rate in cm/day: ", bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 11,'bold'))
            growth_rate_label.place(relx=0.5, rely=0.4, anchor='center')
            growth_rate_entry = tk.Entry(window, font=('Helvetica', 11,'bold'))
            growth_rate_entry.place(relx=0.5, rely=0.5, anchor='center')

            days_label = tk.Label(window, text="Enter the number of days to simulate: ", bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 11,'bold'))
            days_label.place(relx=0.5, rely=0.6, anchor='center')
            days_entry = tk.Entry(window, font=('Helvetica', 11,'bold'))
            days_entry.place(relx=0.5, rely=0.7, anchor='center')

            simulate_button = tk.Button(window, text="Simulate", command=lambda: CropSimulation(user_input, weather_data), bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 11,'bold'))
            simulate_button.place(relx=0.5, rely=0.8, anchor='center')

            result_label = tk.Label(window, bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 11,'bold'))
            result_label.pack(pady=10)

            window.mainloop()
        else:
            messagebox.showerror("Error", "Please fetch the weather data first.")

    root = tk.Tk()
    root.configure(bg='#1C1C1C')
    root.geometry("600x600")  
    root.title("AgriPy- Crop Simulation")

    window_width = 550
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    city_label = tk.Label(root, text="Enter Your City: ", bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 11,'bold'))
    city_label.pack(pady=10)
    city_entry = tk.Entry(root, font=('Helvetica', 11,'bold'))
    city_entry.pack(pady=10)

    fetch_button = tk.Button(root, text="Fetch Weather", command=weather, bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 11,'bold'))
    fetch_button.pack(pady=10)

    weather_label = tk.Label(root, bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 11,'bold'))
    weather_label.pack(pady=10)

    temp_label = tk.Label(root, bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 11,'bold'))
    temp_label.pack(pady=10)

    humidity_label = tk.Label(root, bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 11,'bold'))
    humidity_label.pack(pady=10)

    rainfall_label = tk.Label(root, bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 11,'bold'))
    rainfall_label.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=next_window, bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 11,'bold'))
    next_button.pack(pady=10)

    root.mainloop()
      
manas_kulkarni_crop_simulation()