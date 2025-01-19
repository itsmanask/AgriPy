from tkinter import *
from tkinter import messagebox


def process_choice():
    
    global entry_choice

    
    global opened_codes
    if not 'opened_codes' in globals():
        opened_codes = []

    int_entry_choice = int(entry_choice.get())

    
    if int_entry_choice in opened_codes:
        messagebox.showerror("Error", "You can open a code only once")
        return

    opened_codes.append(int_entry_choice)
    int_entry_choice = int(entry_choice.get())

    if int_entry_choice == 1:
        # Water management
        import joshi_code_with_complete_gui_1st_part
        from joshi_code_with_complete_gui_1st_part import atharva_joshi_1st_part
    
    elif int_entry_choice == 2:
        # Automation for Agriculture
        import joshi_code_with_complete_gui_2nd_part
        from joshi_code_with_complete_gui_2nd_part import atharva_joshi_2nd_part

    elif int_entry_choice == 3:
        # Predict Crop Yields
        import revati_code_predict_crop_yield_with_gui_by_joshi
        from revati_code_predict_crop_yield_with_gui_by_joshi import revati_aute

    elif int_entry_choice == 4:
        # Logistics and Supply chains
        import logistics_and_supply_chain_with_GUI_new
        from logistics_and_supply_chain_with_GUI_new import atharva_deshpande

    elif int_entry_choice == 5:
        # Plant disease detection
        import Pragati_Patil_Camera_Code
        from Pragati_Patil_Camera_Code import pragati_patil
        pragati_patil()

    elif int_entry_choice == 6:
        # crop simulation
        import manas_final_code_with_gui_crop_simulation
        from manas_final_code_with_gui_crop_simulation import manas_kulkarni_crop_simulation
        
        
    elif int_entry_choice == 7:
        # Livestock Management
        import manas_final_code_with_gui_livestock_animal
        from manas_final_code_with_gui_livestock_animal import manas_kulkarni_livestock_animal
    
    else:
        messagebox.showerror("Error", "Enter valid input")

root = Tk()
root.title("AgriPy")
root.configure(bg='#1C1C1C')
root.state('zoomed')



logo = PhotoImage(file = r"C:\Users\hp\Desktop\Agripy final python project\AgriPy Final 1\logo2.png.png")

logo = logo.subsample(2) 



label_logo_top = Label(root, image=logo, bg='#1C1C1C')
flower1 = Label(root, text="🍃", bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 50))
flower2 = Label(root, text="🍃", bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 50))

flower3 = Label(root, text="🌷", bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 50))
flower4 = Label(root, text="🌷", bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 50))

flower5 = Label(root, text="🌾", bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 50))
flower6 = Label(root, text="🌾", bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 50))



screen_width = root.winfo_screenwidth()
position_right = int(screen_width / 2)
label_logo_top.place(x=630, y=-65)

flower1.place(x=50, y=350)
flower2.place(relx=0.96, y=350, anchor='ne')

flower3.place(x=50, y=450)
flower4.place(relx=0.96, y=450, anchor='ne')

flower5.place(x=50, y=250)
flower6.place(relx=0.96, y=250, anchor='ne')


label_title = Label(root, text="", font=('Helvetica', 1, 'bold'), bg='#1C1C1C', fg='#4FA687')
label_title.pack(pady=40)

label_subtitle = Label(root, text="🍀 Welcome to AgriPy, the Smart Agricultural Monitoring System 🍀", font=('Helvetica', 20, 'bold'), bg='#1C1C1C', fg='#4FA687')
label_subtitle.pack(pady=30)

enter_choice="Enter the choice from the options given below: "
enter_choice = Label(root, text=enter_choice, font=('Helvetica', 16, 'underline'), bg='#1C1C1C', fg='#4FA687')
enter_choice.pack(pady=13)

options = "\n 1. Water Management \n\n 2. Automation for Agriculture \n\n 3. Predict Crop Yields \
    \n\n 4. Logistics and Supply Chains  \n\n 5. Plant Disease Detection \n\n 6. Crop Simulation  \n\n 7. Livestock Management "

label_options = Label(root, text=options, font=('Helvetica', 14, 'bold'), bg='#1C1C1C', fg='#4FA687')
label_options.pack(pady=10)

entry_choice = Entry(root, font=('Helvetica', 11, 'bold'), bg='#1C1C1C', fg='#4FA687')
entry_choice.pack(pady=10)

button_submit = Button(root, text="Submit", command=process_choice, font=('Helvetica', 12, 'bold'), bg='#1C1C1C', fg='#4FA687')
button_submit.pack(pady=10)

def close_window():
    root.destroy()

button_close = Button(root, text="Close", command=close_window, font=('Helvetica', 11, 'bold'), bg='#1C1C1C', fg='#4FA687')
button_close.pack(pady=1)


root.mainloop()
