import time
import webbrowser

print("take a break")
breaks=3
count=0
print("this program started on"+time.ctime())
while count<3:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/")
    count=count+1


