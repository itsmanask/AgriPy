import datetime
from tkinter import *
from tkinter import messagebox

def OpenNewWindow():
    int_entry_choice = int(entry_choice.get())
    crop_amt = int(entry_cropamt.get())

    newWindow1 = Toplevel(root)
    newWindow1.title("𝙋𝙧𝙞𝙣𝙩𝙞𝙣𝙜 𝙤𝙛 𝙗𝙞𝙡𝙡")
    newWindow1.state('zoomed')
    newWindow1["bg"] = "#1C1C1C"

    label_result_op = Label(newWindow1, text="", font=('Helvetica', 11, 'bold'), fg='#4FA687', bg = "#1C1C1C")
    label_result_op.pack()

    # Displaying order details
    if 1 <= int_entry_choice <= 5 and 1 <= crop_amt <= 100:
        label_result_op.config(text = f"\n\n", bg = "#1C1C1C", font=('Helvetica', 15, 'underline'), fg='#4FA687', borderwidth="5", pady=300)



        label_result_op.config(text=f"Bill / Invoice:\n\n\n"
                                    f"Current date and time: {datetime.datetime.now()}\n\n"
                                    f"Name of customer: {entry_username.get()}\n\n"
                                    f"Contact no. of customer: {int(entry_contactno.get())}\n\n",
                                    bg = "#1C1C1C", font=('Helvetica', 15, 'underline'), fg='#4FA687', borderwidth="5")

        crop_types = {1: ("Tomato", 2356.15), 2: ("Potato", 1396.67), 3: ("Lemons", 4900), 4: ("Cucumber", 1678.57), 5: ("Carrot", 2326.92)}
        crop_name, crop_price = crop_types[int_entry_choice]
        cost = crop_amt * crop_price

        label_result_op.config(text=f"{label_result_op['text']}"
                                    f"Crop ordered: {crop_name}\n\n"
                                    f"Amount of crop ordered (in quintals): {crop_amt}\n\n"
                                    f"Remaining amount of crop (in quintals): {100 - crop_amt}\n\n"
                                    f"Cost of crop ordered (in rupees): {cost}\n\n",
                                    font=('Helvetica', 20, 'bold'), fg='#4FA687', bg = "#1C1C1C", borderwidth="5")
    else:
        '''window_width = 500
        window_height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")'''

        #label_result_op.config(text="", font=('Helvetica', 11, 'bold'), fg='#4FA687', bg = "#1C1C1C", borderwidth="5")

        messagebox.showerror("Error", "Please enter valid input")

def atharva_deshpande():
    global root, entry_username, entry_contactno, entry_choice, entry_cropamt

    root = Tk()
    root["bg"] = "#1C1C1C"
    root.title("𝙇𝙤𝙜𝙞𝙨𝙩𝙞𝙘𝙨 𝙖𝙣𝙙 𝙋𝙧𝙞𝙣𝙩𝙞𝙣𝙜 0𝙛 𝘽𝙞𝙡𝙡")
    root.state('zoomed')

    label_username_ip = Label(root, text="Enter your name:", font=('Helvetica', 15, 'bold'), fg='#4FA687', bg = "#1C1C1C", borderwidth="5")
    label_username_ip.pack()
    entry_username = Entry(root, font=('Helvetica', 15, 'bold'), bg = "#1C1C1C", fg='#4FA687', borderwidth="5")
    entry_username.pack(pady=10)

    label_contactno_ip = Label(root, text="Enter Contact no.:", font=('Helvetica', 15, 'bold'), fg='#4FA687', bg = "#1C1C1C", borderwidth="5")
    label_contactno_ip.pack()
    entry_contactno = Entry(root, font=('Helvetica', 15, 'bold'), fg='#4FA687', bg = "#1C1C1C", borderwidth="5")
    entry_contactno.pack(pady=10)

    
    
    label_display_text1 = Label(root, text="Enter one of the 5 choices from the given options", font=('Helvetica', 15, 'bold', 'underline'), fg='#4FA687', bg = "#1C1C1C", borderwidth="5")
    label_cropnames = Label(root,text="Enter 1. for Tomatoes \nEnter 2. for Potatoes \nEnter 3. for Lemons \nEnter 4. for Cucumber \nEnter 5. for Carrot \n",font=('Helvetica', 15, 'bold'), fg='#4FA687', bg = "#1C1C1C", borderwidth="5")
    label_cropnames.pack()
    
    
    
    label_choice_ip = Label(root, text="Enter your choice:", font=('Helvetica', 15, 'bold'), fg='#4FA687', bg = "#1C1C1C", borderwidth="5")
    label_choice_ip.pack()
    entry_choice = Entry(root, font=('Helvetica', 15, 'bold'), fg='#4FA687', bg = "#1C1C1C", borderwidth="5")
    entry_choice.pack(pady=10)

    label_cropamt_ip = Label(root, text="Enter the amount of crop you want in quintals:", font=('Helvetica', 15, 'bold'), fg='#4FA687', bg = "#1C1C1C", borderwidth="5")
    label_cropamt_ip.pack()
    entry_cropamt = Entry(root, font=('Helvetica', 15, 'bold'), fg='#4FA687', bg = "#1C1C1C")
    entry_cropamt.pack(pady=10)

    label_display_text2 = Label(root, text ="You can only order upto 100 quintals of crops.", font=('Helvetica', 15, 'bold', 'underline'), fg='#4FA687', bg = "#1C1C1C", borderwidth="5")
    label_display_text2.pack(pady = 10)
    

    label_destination_ip = Label(root, text="Enter your final destination:", font=('Helvetica', 15, 'bold'), fg='#4FA687', bg = "#1C1C1C", borderwidth="5")
    label_destination_ip.pack()
    entry_destination = Entry(root, font=('Helvetica', 15, 'bold'), fg='#4FA687', bg = "#1C1C1C")
    entry_destination.pack(pady=10)

    print_button = Button(root, text="Display the bill", font=('Helvetica', 15, 'bold'), fg='#4FA687',bg = "#1C1C1C", borderwidth="5", command=OpenNewWindow)
    print_button.pack(pady=10)

    root.mainloop()

atharva_deshpande()
