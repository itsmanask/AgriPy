import datetime
import tkinter as tk

def atharva_joshi_1st_part():
    rate_of_flow = 100

    def water_crops():
        wat = int(entry1.get())
        if wat < 70:
            result_label.config(text="Water level is low. Initiating water flow to crops\n"
                                f"Litres of water to flow: {wat}L",font = ('Helvetica',15, 'bold', 'underline'), fg = '#4FA687', bg = "#1C1C1C")
        else:
            result_label.config(text="Water level is sufficient. No need for watering",font = ('Helvetica',15, 'bold', 'underline'), fg = '#4FA687', bg = "#1C1C1C")

    def set_time():
        current_time = datetime.datetime.now().time()
        formatted_time = current_time.strftime("%H:%M")
        result_label.config(text=f"Current time is: {formatted_time}",font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C")

        tim = entry3.get()
        if formatted_time == tim:
            result_label.config(text="Off the flow",font = ('Helvetica',15, 'bold', 'underline'), fg = '#4FA687', bg = "#1C1C1C")
        else:
            result_label.config(text="Keep the flow on",font = ('Helvetica',15, 'bold', 'underline'), fg = '#4FA687', bg = "#1C1C1C")

    def calculate_time():
        tank_capacity = float(entry4.get())
        water_filled = float(entry5.get())
        water_remaining = tank_capacity - water_filled
        time_left = water_remaining / rate_of_flow
        time_full = datetime.datetime.now() + datetime.timedelta(hours=time_left)
        result_label.config(text=f"The time left to fill the tank is {time_left} hours\n"
                            f"The tank will be full by {time_full}",font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C")

    root = tk.Tk()
    root.title("𝒲𝒜𝒯ℰℛ ℳ𝒜𝒩𝒜𝒢ℰℳℰ𝒩𝒯",)
    root["bg"]="#1C1C1C"
    root.state('zoomed')            #dimensions of window

    label_default_top = tk.Label(root, text="",font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C", borderwidth="5")
    label_default_top.pack(pady = 20)

    label1 = tk.Label(root, text="Enter the amount of water in litres: (50-700 litres)",font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C", borderwidth="5")
    label1.pack(pady = 10)


    entry1 = tk.Entry(root, font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C", borderwidth="5")
    entry1.pack()

    button1 = tk.Button(root, text="Check Water Level", command=water_crops, font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C", borderwidth="5")
    button1.pack(pady = 10)


    label2 = tk.Label(root, text="Enter the time in 'HH:MM' format:",font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C", borderwidth="5")
    label2.pack(pady = 10)

    entry3 = tk.Entry(root, font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C", borderwidth="5")
    entry3.pack()

    button2 = tk.Button(root, text="Check Time", command=set_time,borderwidth="5", font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C")
    button2.pack(pady = 10)

    label3 = tk.Label(root, text="Enter the capacity of the tank in litres:",font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C", borderwidth="5")
    label3.pack(pady = 10)

    entry4 = tk.Entry(root, font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C", borderwidth="5")
    entry4.pack()

    label4 = tk.Label(root, text="Enter the amount of water filled in the tank in litres:",font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C", borderwidth="5")
    label4.pack(pady = 10)

    entry5 = tk.Entry(root, font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C", borderwidth="5")
    entry5.pack()

    button3 = tk.Button(root, text="Calculate Time to Fill Tank", command=calculate_time, borderwidth="5", font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C")
    button3.pack(pady = 10)

    result_label = tk.Label(root, text="", font = ('Helvetica',15, 'bold'), fg = '#4FA687', bg = "#1C1C1C", borderwidth="5")
    result_label.pack()

    root.mainloop()
atharva_joshi_1st_part()