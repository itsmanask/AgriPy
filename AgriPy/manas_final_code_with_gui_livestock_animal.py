import json
import tkinter as tk
from tkinter import messagebox

def manas_kulkarni_livestock_animal():
    class LivestockAnimal:
        def __init__(self, name, breed, age, gender, weight, health_status):
            self.name = name
            self.breed = breed
            self.age = age
            self.gender = gender
            self.weight = weight
            self.health_status = health_status

    def create_window(title, width, height, bg_color='#1C1C1C', font_color='#4FA687'):
        window = tk.Tk()
        window.title(title)
        window.geometry(f"{width}x{height}+{int((window.winfo_screenwidth() - width) / 2)}+{int((window.winfo_screenheight() - height) / 2)}")
    
        if bg_color:
            window.configure(bg=bg_color)
        if font_color:
            window.tk_setPalette(background=bg_color, foreground=font_color)

        return window

    def add_livestock_animal(farm_animals,window):
    
        window.geometry('900x700')
    
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        window_width = 400
        window_height = 350

        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        font = ('Helvetica', 11,'bold')  

        name_label = tk.Label(window, text="Name:", font=font, fg='#4FA687')
        name_entry = tk.Entry(window, font=font, fg='#4FA687')
        breed_label = tk.Label(window, text="Breed:", font=font, fg='#4FA687')
        breed_entry = tk.Entry(window, font=font, fg='#4FA687')
        age_label = tk.Label(window, text="Age:", font=font, fg='#4FA687')
        age_entry = tk.Entry(window, font=font, fg='#4FA687')
        gender_label = tk.Label(window, text="Gender:", font=font, fg='#4FA687')
        gender_entry = tk.Entry(window, font=font, fg='#4FA687')
        weight_label = tk.Label(window, text="Weight (kg):", font=font, fg='#4FA687')
        weight_entry = tk.Entry(window, font=font, fg='#4FA687')
        health_status_label = tk.Label(window, text="Health Status:", font=font, fg='#4FA687')
        health_status_entry = tk.Entry(window, font=font, fg='#4FA687')

        def submit():
            try:
                name = name_entry.get()
                breed = breed_entry.get()
                age = int(age_entry.get())
                gender = gender_entry.get()
                weight = float(weight_entry.get())
                health_status = health_status_entry.get()

                new_animal = LivestockAnimal(name, breed, age, gender, weight, health_status)
                farm_animals.append(new_animal)

                save_data_to_file(farm_animals)

                confirmation_window = show_confirmation("Success", "Livestock Animal added successfully.", window)

                confirmation_window.wait_window()

                window.destroy()
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid input.")

    
          
        submit_button = tk.Button(window, text="Submit", command=submit, font=('Helvetica', 12, 'bold'), bg='#1C1C1C', fg='#4FA687')    
    

        name_label.grid(row=0, column=0, padx=10, pady=10)
        name_entry.grid(row=0, column=1, padx=10, pady=10)
        breed_label.grid(row=1, column=0, padx=10, pady=10)
        breed_entry.grid(row=1, column=1, padx=10, pady=10)
        age_label.grid(row=2, column=0, padx=10, pady=10)
        age_entry.grid(row=2, column=1, padx=10, pady=10)
        gender_label.grid(row=3, column=0, padx=10, pady=10)
        gender_entry.grid(row=3, column=1, padx=10, pady=10)
        weight_label.grid(row=4, column=0, padx=10, pady=10)
        weight_entry.grid(row=4, column=1, padx=10, pady=10)
        health_status_label.grid(row=5, column=0, padx=10, pady=10)
        health_status_entry.grid(row=5, column=1, padx=10, pady=10)
        submit_button.grid(row=7, column=0, columnspan=2, pady=20, ipadx=10, ipady=10)

        window.mainloop()
    
    def list_livestock_animals(farm_animals, window):
        window.destroy()
        window = create_window("List Livestock Animals", 500, 400)

        text_widget = tk.Text(window, wrap=tk.WORD)
        text_widget.configure(font=('Helvetica', 11,'bold'))
        text_widget.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        if not farm_animals:
            text_widget.insert(tk.END, "No Animals Present in the Database")
            text_widget.tag_configure("center", justify='center')
            text_widget.tag_add("center", 1.0, "end")
        else:
            for animal in farm_animals:
                text_widget.insert(tk.END, f"\nName: {animal.name}\nBreed: {animal.breed}\nAge: {animal.age}\nGender: {animal.gender}\nWeight: {animal.weight}\nHealth status: {animal.health_status}\n\n")

        close_button = tk.Button(window, text="Ok", command=window.destroy,font=('Helvetica', 12, 'bold'), bg='#1C1C1C', fg='#4FA687')
        close_button.grid(row=1, column=0, pady=10)

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        window.mainloop()


    def update_health_status(farm_animals, animal_name, window):
        window.destroy()
        window = create_window("Update Health Status", 400, 200)

        found = False

        for animal in farm_animals:
            if animal.name.lower() == animal_name.lower():
                found = True
                new_health_status_label = tk.Label(window, text="Enter the new health status:")
                new_health_status_label.configure(font=('Helvetica', 11,'bold'))
                new_health_status_label.pack(pady=10)
                new_health_status_entry = tk.Entry(window)
                new_health_status_entry.pack(pady=10)

            
                def submit():
                    new_health_status = new_health_status_entry.get()
                    animal.health_status = new_health_status

                
                    save_data_to_file(farm_animals)

                    confirmation_window = show_confirmation("Success", "Health status updated successfully.", window)

                
                    confirmation_window.destroy()
                    window.destroy()

            
                submit_button = tk.Button(window, text="Submit", command=submit)
                submit_button.configure(font=('Helvetica', 12, 'bold'), bg='#1C1C1C', fg='#4FA687')
                submit_button.pack(pady=10)

                break

        if not found:
            message_label = tk.Label(window, text="No such animal found in the database.")
            message_label.configure(font=('Helvetica', 11,'bold'))
            message_label.pack(pady=10)
            close_button = tk.Button(window, text="Close", command=window.destroy)
            close_button.pack(pady=10)

        window.mainloop()


    def remove_livestock_animal(farm_animals, animal_name, window):
        window.destroy()
        window = create_window("Remove Livestock Animal", 400, 200)

        found = False

        for animal in farm_animals:
            if animal.name.lower() == animal_name.lower():
                farm_animals.remove(animal)
                found = True
                break

        if found:
        
            save_data_to_file(farm_animals)

            message_label = tk.Label(window, text="Livestock Animal Removed Successfully")
            message_label.configure(font=('Helvetica', 11,'bold'))
            message_label.pack(pady=10)
        else:
            message_label = tk.Label(window, text="No such animal found in the database.")
            message_label.configure(font=('Helvetica', 11,'bold'))
            message_label.pack(pady=10)

        close_button = tk.Button(window, text="Close", command=window.destroy)
        close_button.configure(font=('Helvetica', 11,'bold'))
        close_button.pack(pady=10)

        window.mainloop()


    def save_data_to_file(data):
        with open("livestock_data.json", "w") as file:
            json.dump([animal.__dict__ for animal in data], file)


    def load_data_from_file():
        try:
            with open("livestock_data.json", "r") as file:
                data = json.load(file)
                return [LivestockAnimal(**animal) for animal in data]
        except FileNotFoundError:
            return []
    
    
    def get_user_input(title, prompt):
        user_input = 'exit'

        def submit():
            nonlocal user_input
            user_input = entry.get()
            root.quit()

        root = tk.Tk()
        root.configure(background='#1C1C1C')
        root.title(title)

        window_width = 600
        window_height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        font_size = 15
        root.option_add('*Dialog.msg.font', f'Helvetica {font_size}')
        root.option_add('*Dialog.msg.foreground', '#4FA687')
        root.option_add('*Dialog.msg.background', '#1C1C1C')

        label = tk.Label(root, text=prompt, bg='#1C1C1C', fg='#4FA687', font=('Helvetica', font_size, 'bold'), anchor='center', justify='center')
        label.pack(pady=10)

        entry = tk.Entry(root, font=('Helvetica', font_size,'bold'), justify='center')
        entry.pack(pady=10)

        def submit_and_close():
            submit()
            root.destroy()

        button = tk.Button(root, text='Submit', command=submit_and_close, font=('Helvetica', 15, 'bold'), bg='#1C1C1C', fg='#4FA687')
        button.pack(pady=15)

        close_button = tk.Button(root, text="Close", command=root.destroy, bg='#1C1C1C', fg='#4FA687', font=('Helvetica', 12,'bold'))
        close_button.pack(pady=10)

        root.mainloop()
        return user_input



    def show_confirmation(title, message, main_window):
        window = tk.Toplevel()
        window.title(title)
    
        window_width = 400
        window_height = 200

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        label = tk.Label(window, text=message, font=('Helvetica', 11,'bold'), fg='white', bg='black', padx=10, pady=10)
        label.pack(expand=True)
        ok_button = tk.Button(window, text="OK", command=lambda: [window.destroy(), main_window.destroy()])
        ok_button.pack(pady=10)


    def main():
    
        farm_animals = load_data_from_file()

        while True:
        
            option = get_user_input("Options", "Choose an option:\n\n1. Add a new livestock animal\n\n2. List all the livestock animals\n\n3. Update the health status of a livestock animal\n\n4. Remove a livestock animal from the farm\n\n5. Exit")
            if option == 'exit':
                exit()
            
            if option:
                try:
                    option = int(option)
                    if option == 1:
                        window = create_window("Add Livestock Animal", 400, 300, bg_color='black', font_color='white')
                        add_livestock_animal(farm_animals, window)
                    elif option == 2:
                        window = create_window("List Livestock Animals", 400, 300, bg_color='black', font_color='white')
                        list_livestock_animals(farm_animals, window)
                    elif option == 3:
                        animal_name = get_user_input("Update Health Status", "Enter the name of the livestock animal:")
                        window = create_window("Update Health Status", 400, 200, bg_color='black', font_color='white')
                        update_health_status(farm_animals, animal_name, window)
                    elif option == 4:
                        animal_name = get_user_input("Remove Livestock Animal", "Enter the name of the livestock animal:")
                        window = create_window("Remove Livestock Animal", 400, 200, bg_color='black', font_color='white')
                        remove_livestock_animal(farm_animals, animal_name, window)
                    elif option == 5:
                        exit()
                    else:
                        messagebox.showerror("Invalid Option", "Invalid option. Please try again")
                    
                except ValueError:
                   messagebox.showerror("Invalid Option", "Invalid option. Please enter a number.")
                
            else:
                messagebox.showerror("Invalid Input", "Invalid input. Please try again.")
            

            save_data_to_file(farm_animals)

            
            again = get_user_input("\n\nContinue?", "Continue? (y/n): ")
            if again.lower() not in ["y", "yes", "n", "no", "exit"]:
                messagebox.showerror("Invalid Input", "Invalid input. Please try again.")
                

            if again.lower() in ["n", "no", "exit"]:
                exit()

    
    main()
manas_kulkarni_livestock_animal()
