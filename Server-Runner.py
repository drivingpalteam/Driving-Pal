from flask import Flask
from flask import jsonify
from flask import request
import os
import smtplib
import winsound
import serial
import json
import socket

app = Flask(__name__)

@app.route('/start', methods=['POST'])
def startScan():
    print("received")
    data = json.loads(json.dumps(request.get_json()))
    print(data)
    meth = (data['queryResult']['intent']['displayName'])
    if meth == 'Start safe driving mode':
        conn.sendall(b'start\n')
        return jsonify(fulfillmentText="Safe mode starting")
    elif meth == 'Start driving helper':
        conn2.sendall(b'start\n')
        return jsonify(fulfillmentText="Assistant starting")

@app.route('/unlock', methods=['GET'])
def servo():
    print('unlocked')
    '''s = smtplib.SMTP("smtp.gmail.com", 587) #This is to send an email when the car is unlocked... Good job on finding this
    s.starttls()                               #hidden feature. Now you can try and get this working (not that hard) ;)
    s.login("email", "password")
    s.sendmail("email", "emailto", "\nYour car has been unlocked")
    s.quit()'''
    winsound.Beep(1500, 3000)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = (socket.gethostname(), 5000)
    print("Binding")
    sock.bind(addr)
    socketman = sock.getsockname()
    print(socketman)
    print('Binded')
    sock.listen(1)
    print('Running Script')
    os.system('Py -3.6 script.py ' + socketman[0])
    conn, ip = sock.accept()
    print('connected1')
    conn2, ip2 = sock.accept()
    app.run(host='0.0.0.0')