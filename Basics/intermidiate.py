import os
import json
import csv
import time
import datetime
import pygame
import threading

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
chore1.join()
chore2.join()
chore3.join()

print("All chore sre complete")