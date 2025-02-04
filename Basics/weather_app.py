
# "a2d8501d934a4b62addb3a2e0e4de8d5";
import sys
import requests
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,
                             QPushButton,QHBoxLayout,QVBoxLayout,QLineEdit)
from PyQt5.QtCore import QTimer,QTime,Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label=QLabel("Enter city name: ",self)
        self.city_input=QLineEdit(self)
        self.get_weather_button=QPushButton("Get Weather",self)
        self.temp_label=QLabel(self)
        self.emoji_label=QLabel(self)
        self.description_label=QLabel(self)
        self.initui()

    def initui(self):
        self.setWindowTitle("Weather APP")
        vbox=QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.setStyleSheet("""
        QLabel,QPushButton{
            font-family:calibri;
        }
        QLabel#city_label{
            font-size:40px;
            font-style:italic;
        }
        QLineEdit#city_input{
            font-size:40px;
        }
        QPushButton#get_weather_button{
            font-size:30px;
            font-style:bold;
        }
        QLabel#temp_label{
            font-size:75px;
        }
        QLabel#emoji_label{
        font-size:100px;
        font-family:Segoe UI emoji;
        }
        QLabel#description_label{
            font-size:50px;
        }
        """)
        self.get_weather_button.clicked.connect(self.get_weather)
    def get_weather(self):
        api_key="a7c5e6b76ebb00325ed57808e3620181"
        city=self.city_input.text()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            res = requests.get(url)
            res.raise_for_status() # raise http errors
            data = res.json()
            if data["cod"]==200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
            match res.status_code:
                case 400:
                    self.display_error("Bad request\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized\nInvalid api key")
                case 403:
                    self.display_error("Forbidden\nAccess denied")
                case 404:
                    self.display_error("Not Found\nCity Not Found")
                case 400:
                    self.display_error("Internal Server Error\nPlease try again later")
                case 400:
                    self.display_error("Bad Gateway\nInvalid response from server")
                case 400:
                    self.display_error("Service Unavailable\nServer is down")
                case 400:
                    self.display_error("Gateway timeout\nNo Response from server")
                case _:
                    self.display_error(f"HTTP Error occured\n{http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck your url")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")
    def display_error(self,message):
        self.temp_label.setStyleSheet("""
            font-size:30px;
        """)
        self.temp_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()
    def display_weather(self,data):
        self.temp_label.setStyleSheet("""
                    font-size:75px;
                """)
        temp_k=data["main"]["temp"]
        temp_c=temp_k-273.15
        temp_f=(temp_k*9/5)-459.67
        desc = data["weather"][0]["description"]
        weather_id=data["weather"][0]["id"]
        self.temp_label.setText(f"{temp_c:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(desc)
    @staticmethod
    def get_weather_emoji(weather_id):
        if 200<=weather_id<=232:
            return "⛈️"
        elif 300<=weather_id<=321:
            return "☁️"
        elif 500<=weather_id<=532:
            return "🌧️"
        elif 600<=weather_id<=632:
            return "❄️"
        elif 700<=weather_id<=741:
            return "🌫️"
        elif weather_id== 762:
            return "🌋"
        elif weather_id==771:
            return "💨"
        elif weather_id==800:
            return "☀️"
        elif 800<=weather_id<=804:
            return "⛅"
        else:
            return ""



if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())