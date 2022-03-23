import datetime
import time

with open("file.txt", 'w') as f:
    f.write("Today is {0}!".format(datetime.date.today()))
f.close()

with open("file.txt", 'r') as f:
    print(f.read())
f.close()
