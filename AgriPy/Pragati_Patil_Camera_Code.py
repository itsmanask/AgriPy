import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
from PIL import Image, ImageTk

def pragati_patil():
    class PlantDiseaseDetectionApp:
        def __init__(self, master):
            self.master = master
            self.master.title("Plant Disease Detection")

            self.open_button = tk.Button(self.master, text="Open Image", command=self.open_image, fg='#4FA687', bg = "#1C1C1C", font = ('Helvetica',15, 'bold'))
            self.open_button.pack(pady = 10)

            self.capture_button = tk.Button(self.master, text="Capture Image", command=self.capture_image, fg='#4FA687', bg = "#1C1C1C", font = ('Helvetica',15, 'bold'))
            self.capture_button.pack(pady = 10)

            self.result_label = tk.Label(self.master, text="", font=('Helvetica', 15, 'bold'), fg='#4FA687', bg = "#1C1C1C")
            self.result_label.pack()

            self.image_label = tk.Label(self.master)
            self.image_label.pack()

            
            self.camera = cv2.VideoCapture(0)  # 0 corresponds to the default camera

            self.update()

        def open_image(self):
            file_path = filedialog.askopenfilename()
            if file_path:
                image = cv2.imread(file_path)
                self.analyze_image(image)
                self.update_image_label(file_path)

        def capture_image(self):
            ret, frame = self.camera.read()
            if ret:
                self.analyze_image(frame)
                self.update_image_label_from_frame(frame)

        def analyze_image(self, image):
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            average_intensity = np.mean(gray_image)
            print(average_intensity)
            disease_threshold = 200
            if average_intensity > disease_threshold:
                self.result_label.config(text="Disease detected", font=('Helvetica', 15, 'bold'), fg='#4FA687', bg = "#1C1C1C")
            else:
                self.result_label.config(text="No disease detected", font=('Helvetica', 15, 'bold'), fg='#4FA687', bg = "#1C1C1C")

        def update_image_label(self, file_path):
            image = Image.open(file_path)
            image = ImageTk.PhotoImage(image)
            self.image_label.config(image=image)
            self.image_label.image = image

        def update_image_label_from_frame(self, frame):
            # Convert the frame from OpenCV format to PIL format
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = ImageTk.PhotoImage(image)
            self.image_label.config(image=image)
            self.image_label.image = image

        def update(self):
            ret, frame = self.camera.read()
            if ret:
                self.update_image_label_from_frame(frame)
            self.master.after(10, self.update)

        def __del__(self):
            
            if hasattr(self, 'camera'):
                self.camera.release()

    app = tk.Tk()
    app["bg"]="#1C1C1C"     #background colour of window
    app.state('zoomed')
    plant_disease_detection_app = PlantDiseaseDetectionApp(app)
    app.mainloop()

pragati_patil()
