import os
import datetime

text=input('Please enter file contents?')

if text:
    date=datetime.datetime.now().date()
    time=datetime.datetime.now().time()
    if not os.path.exists(f'./{date}'):
        os.mkdir(f'./{date}')
    f = open(f"./{date}/{time}.txt", "x")
    f.write(text)
    f.close()