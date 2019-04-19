from flask import Flask
from flask import jsonify
from flask import request
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
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("inventorshubinc@gmail.com", "Password4u")
    s.sendmail("inventorshubinc@gmail.com", "michaelwu21@gmail.com", "\nYour car has been unlocked")
    s.quit()
    winsound.Beep(1500, 3000)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('192.168.137.1', 5000)
    print("Binding")
    sock.bind(addr)
    print('Binded')
    sock.listen(1)
    socketman = sock.getsockname()
    print(socketman)
    conn, ip = sock.accept()
    print('connected1')
    conn2, ip2 = sock.accept()
    #ser=serial.Serial('/dev/ttyACM0', 9600)
    app.run(host='0.0.0.0')