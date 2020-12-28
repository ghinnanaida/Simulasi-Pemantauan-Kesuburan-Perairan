from flask import Flask, render_template, url_for, request, redirect, make_response, session
import random
import json
from time import time
from datetime import date
from datetime import datetime
from random import random
from flask import Flask, render_template, make_response
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)

# -----Setting Database----------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'refer'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL(app)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('login.html')

@app.route('/register', methods=["GET", "POST"])
def regis():
    if request.method =='GET':
        return render_template('regis.html')
    else :
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO user(name, email, password) values (%s,%s,%s)", (name, email, password,)
        )
        mysql.connection.commit()
        session['name'] = name
        session['email'] = email
        return redirect(url_for('main'))

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM user where email=%s", (email,)
        )
        user =cur.fetchone()
        cur.close()

        if len(user)>0:
            if password == user['password']:
                session['name'] = user['name']
                session['email'] = user ['email']
                return redirect(url_for('home'))
        else:
            return 'Error password or user does not match'
    else :
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('login.html')



@app.route('/home', methods=["GET", "POST"])
def home():
    return render_template('home.html')

@app.route('/stasiun1', methods=["GET", "POST"])
def main1():
    return render_template('stasiun1.html')

@app.route('/stasiun2', methods=["GET", "POST"])
def main2():
    return render_template('stasiun2.html')

@app.route('/stasiun3', methods=["GET", "POST"])
def main3():
    return render_template('stasiun3.html')

@app.route('/stasiun4', methods=["GET", "POST"])
def main4():
    return render_template('stasiun4.html')

@app.route('/fertility', methods=["GET", "POST"])
def main5():
    return render_template('fertil.html')

@app.route('/location', methods=["GET", "POST"])
def main6():
    return render_template('maps.html')

@app.route('/data1', methods=["GET", "POST"])
def data1():
    # Data Format
    # [TIME, Temperature, Humidity] 
    cur = mysql.connection.cursor()
    resultValue = cur.execute(
        "SELECT * FROM stasiun1 order by no desc limit 1")
    if resultValue > 0:
        datasensor = cur.fetchone()
        klorofil = datasensor['sensor1']
        Do = datasensor['sensor2']
        pH = datasensor['sensor3']
        salinitas = datasensor['sensor4']
        data = [time() * 1000, klorofil, Do, pH, salinitas]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
    else:
        klorofil = 0
        Do = 0
        pH = 0
        salinitas = 0
        data = [time() * 1000, klorofil, Do, pH, salinitas]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
    return response

@app.route('/data2', methods=["GET", "POST"])
def data2():
    # Data Format
    # [TIME, Temperature, Humidity]
    cur = mysql.connection.cursor()
    resultValue = cur.execute(
        "SELECT * FROM stasiun2 order by no desc limit 1")
    if resultValue > 0:
        datasensor = cur.fetchone()
        klorofil = datasensor['sensor1']
        Do = datasensor['sensor2']
        pH = datasensor['sensor3']
        salinitas = datasensor['sensor4']
        data = [time() * 1000, klorofil, Do, pH, salinitas]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
    else:
        klorofil = 0
        Do = 0
        pH = 0
        salinitas = 0
        data = [time() * 1000, klorofil, Do, pH, salinitas]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
    return response

@app.route('/data3', methods=["GET", "POST"])
def data3():
    # Data Format
    # [TIME, Temperature, Humidity]
    cur = mysql.connection.cursor()
    resultValue = cur.execute(
        "SELECT * FROM stasiun3 order by no desc limit 1")
    if resultValue > 0:
        datasensor = cur.fetchone()
        klorofil = datasensor['sensor1']
        Do = datasensor['sensor2']
        pH = datasensor['sensor3']
        salinitas = datasensor['sensor4']
        data = [time() * 1000, klorofil, Do, pH, salinitas]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
    else:
        klorofil = 0
        Do = 0
        pH = 0
        salinitas = 0
        data = [time() * 1000, klorofil, Do, pH, salinitas]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
    return response

@app.route('/data4', methods=["GET", "POST"])
def data4():
    # Data Format
    # [TIME, Temperature, Humidity]
    cur = mysql.connection.cursor()
    resultValue = cur.execute(
        "SELECT * FROM stasiun4 order by no desc limit 1")
    if resultValue > 0:
        datasensor = cur.fetchone()
        klorofil = datasensor['sensor1']
        Do = datasensor['sensor2']
        pH = datasensor['sensor3']
        salinitas = datasensor['sensor4']
        data = [time() * 1000, klorofil, Do, pH, salinitas]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
    else:
        klorofil = 0
        Do = 0
        pH = 0
        salinitas = 0
        data = [time() * 1000, klorofil, Do, pH, salinitas]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
    return response

# -------Sensor--------
@app.route('/sensor1', methods=['GET', 'POST'])
def sensor1():
    if request.method == 'POST':
        # mengambil nilai yg dikirimkan
        Kloro1 = request.values.get('Kloro1')
        Kloro2 = request.values.get('Kloro2')
        Kloro3 = request.values.get('Kloro3')
        Kloro4 = request.values.get('Kloro4')
        Do1 = request.values.get('Do1')
        Do2 = request.values.get('Do2')
        Do3 = request.values.get('Do3')
        Do4 = request.values.get('Do4')
        sal1 = request.values.get('sal1')
        sal2 = request.values.get('sal2')
        sal3 = request.values.get('sal3')
        sal4 = request.values.get('sal4')
        pH1 = request.values.get('pH1')
        pH2 = request.values.get('pH2')
        pH3 = request.values.get('pH3')
        pH4 = request.values.get('pH4')
        tgl = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO stasiun1(tgljam, sensor1, sensor2,sensor3, sensor4) VALUES (%s,%s, %s, %s,%s)", (tgl, Kloro1, Do1,pH1, sal1))
        cur.execute(
            "INSERT INTO stasiun2(tgljam, sensor1, sensor2,sensor3, sensor4) VALUES (%s,%s, %s, %s,%s)", (tgl, Kloro2, Do2,pH2, sal2))
        cur.execute(
            "INSERT INTO stasiun3(tgljam, sensor1, sensor2,sensor3, sensor4) VALUES (%s,%s, %s, %s,%s)", (tgl, Kloro3, Do3,pH3, sal3))
        cur.execute( 
            "INSERT INTO stasiun4(tgljam, sensor1, sensor2,sensor3, sensor4) VALUES (%s,%s, %s, %s,%s)", (tgl, Kloro4, Do4,pH4, sal4))
        mysql.connection.commit()
        cur.close()
        return redirect('/')
    elif request.method == 'GET':
        cur = mysql.connection.cursor()
        resultValue = cur.execute(
            "SELECT * FROM stasiun1 order by no desc limit 20")
        if resultValue > 0:
            datasensor = cur.fetchall()
        return render_template('home.html', data=datasensor)


if __name__ == "__main__":
    app.secret_key = "ausEh1284*9A+)(83IG"
    app.run()