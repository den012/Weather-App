from tkinter import *
import requests
import time
from PIL import ImageTk, Image


class App(Tk):
    def __init__(self):
        super().__init__()

        self.resizable(False, False)
        self.geometry("900x900")
        self.configure(bg="#ffffff")
        self.title("Weather App")
        self.canvas = Canvas(
            self,
            bg="#ffffff",
            height=900,
            width=900,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=f"background.png")
        self.background = self.canvas.create_image(
            398.5, 435.5,
            image=self.background_img)

        self.entry0_img = PhotoImage(file=f"img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            433.0, 245.5,
            image=self.entry0_img)

        self.entry0 = Entry(
            bd=0,
            bg="#ffffff",
            highlightthickness=0,
            font=("Raileway", 22))

        self.entry0.place(
            x=326.5, y=220,
            width=213.0,
            height=49)
        self.entry0.focus()
        self.entry0.bind('<Return>', self.getWeather)

        # weather info
        self.labelGeneralInfo = Label(self, font=("Raileway", 30, "bold"), borderwidth=0, highlightthickness=0, padx=30,
                                      pady=5)
        self.labelGeneralInfo.place(x=400, y=300)

        self.labelMinima = Label(self, font=("Raileway", 30), borderwidth=0, highlightthickness=0, padx=30, pady=5)
        self.labelMinima.place(x=150, y=500)

        self.labelMaxima = Label(self, font=("Raileway", 30), borderwidth=0, highlightthickness=0, padx=30, pady=5)
        self.labelMaxima.place(x=150, y=620)

        self.labelRasarit = Label(self, font=("Raileway", 30), borderwidth=0, highlightthickness=0, padx=30, pady=5)
        self.labelRasarit.place(x=150, y=740)

        self.labelVant = Label(self, font=("Raileway", 30), borderwidth=0, highlightthickness=0, padx=30, pady=5)
        self.labelVant.place(x=620, y=500)

        self.labelUmiditate = Label(self, font=("Raileway", 30), borderwidth=0, highlightthickness=0, padx=30, pady=5)
        self.labelUmiditate.place(x=620, y=620)

        self.lableApus = Label(self, font=("Raileway", 30), borderwidth=0, highlightthickness=0, padx=30, pady=5)
        self.lableApus.place(x=620, y=740)

    def getWeather(self, event):
        self.city = self.entry0.get()
        self.api = "https://api.openweathermap.org/data/2.5/weather?q=" + self.city + "&appid=06c921750b9a82d8f5d1294e1586276f"

        self.json_data = requests.get(self.api).json()
        self.condition = self.json_data['weather'][0]['main']
        self.temp = int(self.json_data['main']['temp'] - 273.15)
        self.minTemp = int(self.json_data['main']['temp_min'] - 273.15)
        self.maxTemp = int(self.json_data['main']['temp_max'] - 273.15)
        self.humidity = self.json_data['main']['humidity']
        self.wind = self.json_data['wind']['speed']
        self.sunrise = time.strftime('%I:%M:%S', time.gmtime(self.json_data['sys']['sunrise'] - 21600))
        self.sunset = time.strftime('%I:%M:%S', time.gmtime(self.json_data['sys']['sunset'] - 21600))

        self.generalInfo = self.condition + "\n" + str(self.temp) + "°C"
        self.labelGeneralInfo.config(text=self.generalInfo)

        self.minima = str(self.minTemp)
        self.labelMinima.config(text=self.minima)
        self.maxima = str(self.maxTemp)
        self.labelMaxima.config(text=self.maxima)
        self.umiditate = str(self.humidity)
        self.labelUmiditate.config(text=self.umiditate)
        self.vant = str(self.wind)
        self.labelVant.config(text=self.wind)
        self.rasarit = self.sunrise
        self.labelRasarit.config(text=self.rasarit)
        self.apus = self.sunset
        self.lableApus.config(text=self.apus)


if __name__ == "__main__":
    app = App()
    app.mainloop()
