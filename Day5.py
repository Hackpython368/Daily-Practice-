import time 
import playsound

hour = int(input("Enter no of hours :"))
minuts = int(input("Enter no of minutes :"))
seco = int(input("Enter no of seconds :"))

total_in_second = (hour*60*60)+(minuts*60)+(seco)

while True:
    time.sleep(1)
    total_in_second -= 1
    print(total_in_second)
    if total_in_second==0:
        break

playsound.playsound("/audioFile/audio.mp3")