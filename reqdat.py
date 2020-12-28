import requests
import random
import time
 

url = 'http://localhost:5000/sensor1'
i = 0
while(1):
    Kloro1 = random.random() * 30
    Kloro2 = random.random() * 30
    Kloro3 = random.random() * 30
    Kloro4 = random.random() * 30
    Do1 = random.random() * 15
    Do2 = random.random() * 15
    Do3 = random.random() * 15
    Do4 = random.random() * 15
    Sal1 = random.random() * 40
    Sal2 = random.random() * 40
    Sal3 = random.random() * 40
    Sal4 = random.random() * 40
    pH1 = random.random() * 20
    pH2 = random.random() * 20
    pH3 = random.random() * 20
    pH4 = random.random() * 20
    myobj = {'Kloro1': Kloro1, 'Kloro2': Kloro2,'Kloro3': Kloro3,'Kloro4': Kloro4,
            'Do1': Do1,'Do2': Do2,'Do3': Do3,'Do4': Do4,
            'sal1':Sal1,'sal2':Sal2,'sal3':Sal3,'sal4':Sal4,
            'pH1':pH1,'pH2':pH2,'pH3':pH3,'pH4':pH4}

    # -------kirim data ke server
    # -------------------------------------------------
    x = requests.post(url, data=myobj)
    print(x.text)
    i = i+1