import os
import json
import csv
import random
import time
import datetime
import pygame
import threading
import requests
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, \
    QPushButton, QCheckBox, QRadioButton, QButtonGroup, QLineEdit
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import Qt

#exception handling - try except finally
try:
    number=int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only numbers")
except Exception:
    print("Something went wrong")
finally:
    print("Do some cleanup here")

#file detection
file_path="test.txt"
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")

else:
    print("The location doesn't exists")

#writing files(.txt, .json, .csv)
text_data="jai mahadev"
with open(file_path,"w")as file:  #returns a file object as file=File()
    file.write(text_data)
    print(f"txt file {file_path} is created")
# "x" - write if file doesn't exist
try:
    with open(file_path, "x") as file:
        file.write(text_data)
        print(f"txt file {file_path} is created")
except FileExistsError:
    print("File already exist")
# "a" - append to existing file
with open(file_path, "a") as file:
    file.write("\n"+text_data)
    print(f"{text_data} is appended")

#working with collections
employees=["Eugene","SpongeBob","Squidward","Patrick"]
with open(file_path, "a") as file:
    for employee in employees:
        file.write("\n"+employee)
    print(f"{employees} is appended")

#json file
employee={
    "name":"Spongebob",
    "age":30,
    "job":"cook"
}
# dump - converts dictionary into json string
file_path="test.json"
try:
    with open(file_path, "w") as file:
        json.dump(employee,file,indent=4)
        print(f"json file {file_path} is created")
except FileExistsError:
    print("file already exists")

#csv file
employees=[["Name","Age","Job"],
           ["Spongebob",30,"Cook"],
           ["Patrick",37,"Unemployed"],
           ["Sandy",27,"Scientist"]]
file_path="test.csv"
# writer is an object
try:
    with open(file_path, "w", newline="") as file:
        writer=csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file {file_path} is created")
except FileExistsError:
    print("file already exists")

#read files(.txt,.json,.csv)
file_path="test.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("you do not have Permission to read the file")

#json file
file_path="test.json"
try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
        print(content["job"])
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("you do not have Permission to read the file")

#csv file
file_path="test.csv"
try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
            print(line[0])
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("you do not have Permission to read the file")

#date and time
date=datetime.date.today()
now=datetime.datetime.now()
# time=now.strftime("%H:%M:%S")
today=now.strftime("%m-%d-%Y")
target_datetime=datetime.datetime(2024,8,7,23,59,59)
print(date)
print(now)
print(time)
print(today)
print(target_datetime)

#python clock
def set_alarm(alarm_time):
    print(f"Alarm is set for {alarm_time}")
    is_running=True
    sound_file="C:\\Users\\HARSH\\Downloads\\Across Seas And Lands - Asher Fulero.wav"
    # while is_running :
    #     current_time=datetime.datetime.now().strftime("%H:%M:%S")
    #     print(current_time)
    #     if current_time==alarm_time:
    #         #mixer - play sound .init to initialize
    #         pygame.mixer.init()
    #         pygame.mixer.music.load(sound_file)
    #         pygame.mixer.music.play()
    #         while pygame.mixer.music.get_busy():
    #             time.sleep(1)
    #         is_running=False
    #     time.sleep(1)


if __name__=="__main__":
    alarm_time=input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)

#multitreading - tasks like fetching data , I/O tasks
# threading.Thread(target=my_function)
def walk_dog(name):
    time.sleep(3)
    print(f"You finished walking {name}")
def take_out_trash():
    time.sleep(3)
    print("You take out the trash")
def get_mail():
    time.sleep(3)
    print("You get the mail")

# tupple with single element ends with comma
chore1=threading.Thread(target=walk_dog,args=("Scooby",))
chore1.start()
chore2=threading.Thread(target=take_out_trash)
chore2.start()
chore3=threading.Thread(target=get_mail)
chore3.start()

#.join - wait till all chores are complete
# chore1.join()
# chore2.join()
# chore3.join()

print("All chore are complete")

#GUI PyQt5
# Boiler plate for a window
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
# def main():
#     app=QApplication(sys.argv)
#     window=MainWindow()
#     window.show()
#     sys.exit(app.exec_())
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Anime")
        self.setGeometry(100,100,600,500) #x,y,width,height
        self.setWindowIcon(QIcon("icon.jpeg"))

        label=QLabel("Top Anime",self) #self is the parent widget of label
        label2=QLabel(self)
        label2.setGeometry(0,0,50,50)
        label.setGeometry(0,0,250,250)
        label.setFont(QFont("Bookman Old Style",20))
        label.setStyleSheet("background-color:#68937C;")
        label.setAlignment(Qt.AlignCenter)
        pixmap=QPixmap("icon.jpeg")
        #image
        label2.setPixmap(pixmap)
        label.width()
        label.height()
        #left justify - self.width()-label.width()
        #bottom justify - self.height-label.height()
        label2.setScaledContents(True)# set image to the label
        label.setGeometry((self.width()-label.width())//2,0,200,50)
        label.setScaledContents(True)
        #layouts
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)
        label1.setStyleSheet("background-color:red")
        label2.setStyleSheet("background-color:yellow")
        label3.setStyleSheet("background-color:green")
        label4.setStyleSheet("background-color:blue")
        label5.setStyleSheet("background-color:black")
        grid = QGridLayout()
        # vbox.addWidget(label1)
        # hbox.addWidget(label1)
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 3, 2)
        central_widget.setLayout(grid)
        self.button = QPushButton("Search", self)
        self.checkbox=QCheckBox("Do you like food? ",label1)
        self.radio1=QRadioButton("Filter",label2)
        #making separate groups for radio btns
        self.button_grp1=QButtonGroup(self)
        self.button_grp2=QButtonGroup(self)

        self.textbox=QLineEdit(self)
        self.initui()
    def initui(self):
        #buttons
        # button=QPushButton("Search",self) #button.setGeometry(150,200,100,20)
        # self.button = QPushButton("Search", self)#move to constructor
        self.button.setObjectName("button1") # for css
        self.button.setStyleSheet("font-size:30px;")
        self.button.clicked.connect(self.on_click)
        #checkbox
        self.checkbox.setStyleSheet("font-size:30px")
        self.checkbox.setGeometry(10,10,200,30)
        self.checkbox.stateChanged.connect(self.on_check)
        #radio btn -select one
        self.setStyleSheet("QRadioButton{"
                           "font-size:40px"
                           "}")   #style to all QRadioButtons
        self.button_grp1.addButton(self.radio1)
        self.radio1.toggled.connect(self.radio_btn_change)
        #line edit widget
        self.textbox.setGeometry(10, 10, 200, 30)
    def on_click(self):
        anime_type=self.textbox.text()
        self.button.setText("Clicked")

        # connecting api
        base_url = "https://api.jikan.moe/v4/top/anime?type="

        def get_top_anime_by_type(name):
            # returns an object
            url = f"{base_url}{name}"
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed to retrieve data {response.status_code}")

        # types=("tv","movie","ova","special","ona","music","cm","pv","tv_special")
        # type=random.choice(types)
        animes = get_top_anime_by_type(anime_type)["data"]
        # print(animes)
        if animes:
            print(f"Anime Type: {anime_type}")
            for anime in animes:
                print()
                print(f"Anime Name: {anime["title_english"] if anime["title_english"] else anime["title"]}")
                print(f"Number of Episodes:{anime["episodes"]}")
                print(f"Status:{anime["status"]}")
                print(f"Duration:{anime["duration"]}")
                print(f"Score:{anime["score"]}")
    def on_check(self,state):
        # print(state) # 2
        if state==Qt.Checked:
            self.button.setText("red")
        else:
            self.button.setText("Search")
    def radio_btn_change(self):
        radio_btn=self.sender() #becomes the sender
        if radio_btn.isChecked():
            print(f"{radio_btn.text()} is Checked")
        # else:
        #     print(f"{radio_btn.text()} is not Checked")

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()

    sys.exit(app.exec_())
if __name__=="__main__":
    main()
