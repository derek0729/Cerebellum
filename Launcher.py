
import Parser as App
import time


print("Running \n")
time.sleep(0.25)
print("Processing Code...\n")
time.sleep(0.25)

file = 'Launch.txt'


App.translate(file)
time.sleep(5)
print("file succesfully writen and uploaded!\n")
#except:
#    print("Errors were encountered\n")