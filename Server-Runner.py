from flask import Flask
from flask import jsonify
from flask import request
import subprocess
from multiprocessing import Process
import threading
from subprocess import call
import os
import time
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
    s.login("from_email", "password")          #You will need to change security features on the sender email to allow less secure apps
    s.sendmail("from_email", "to_email", "\nYour car has been unlocked")
    s.quit()'''
    winsound.Beep(1500, 3000)

def runCV():
    call(["python", "script.py"])

def runBlockstack():
    p = os.path.dirname(os.path.abspath(__file__))
    subprocess.Popen(["python", "maincameraloop.py"], shell=True,
                     stdout=subprocess.PIPE,
                     cwd=p + "/driverassistant/ObjectDetection")

def serveo(socketman):
    textBuffer = ''
    #os.system('ssh -tt -R 80:' + str(socketman[0]) + ":5000 serveo.net")
    p = subprocess.call(["ssh", "-R", "80:" + str(socketman[0]) + ":7000", "serveo.net"], shell=False);
    (output, err) = p.communicate()

    ## Wait for date to terminate. Get return returncode ##
    p_status = p.wait()
    print
    "Command output : ", output
    print
    "Command exit status/return code : ", p_status
    print('finished')

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = (socket.gethostname(), 10000)
    print("Binding")
    sock.bind(addr)
    socketman = sock.getsockname()
    print(socketman)
    print('Binded')
    sock.listen(2)
    print('Running Script for Sleep Detection')

    #_thread.start_new_thread(os.system('Py -3.6 script.py ' + socketman[0]))
    #processThread = threading.Thread(target=runCV)  # <- note extra ','
    #processThread.start()
    print("running")

    conn, ip = sock.accept()
    #print('connected1')
    #print('Running Script for Unlock and HUD')
    #processThread1 = threading.Thread(target=runBlockstack)  # <- note extra ','
    #processThread1.start()
    #os.system('Py -3.6 driverassistant\ObjectDetection\maincameraloop.py ' + socketman[0])
    conn2, ip2 = sock.accept()

    #print("DONE!!\n\nUse this URL with serveo.net in it")
    '''processThread2 = threading.Thread(target=serveo(socketman))  # <- note extra ','
    processThread2.start()'''
    #p = Process(target=serveo, args=(socketman,))
    #p.start()
    #conn2.sendall(b'start\n')
    print("All done")
    app.run(port=7000)
