# Driving-Pal

**To start running this project, you will first need to set up Google's DialogFlow API.**

1) Simply go the https://dialogflow.com/, sign in and click on go to console in the top right.
2) Create a new agent and once it has finished creating, click on the gear icon next to the agent name.
3) Click on the Export and Import tab, and choose import from zip.
4) Drag and drop the DrivingPalVoice.zip file and confirm.
5) You will now have a working DialogFlow Agent, but you will need to change the fulfillment later.

**Setting up Driver Assistant:**

1) Download the zip file here: https://drive.google.com/drive/folders/1J6aHkDpwxa9eR_Ddlk1Meda7LK7juhnH?usp=sharing
2) Make sure to extract the driverassitant zip into the Driving-Pal folder.
    It should look like this:
   ``` 
    -Driving-Pal
      -script.py
      -Server-Runner.py
      -runner.bat
      -README.md
      -driverassistant
        -hello-world-tutorial
        -ObjectDetection
        -index.html
    ```
3) Install NodeJS: https://nodejs.org/en/download/
4) ```npm install -g browserify``` (run as admin)
**Note: If you get a port occupied error, make sure the port is not being used. Otherwise, kill all node.js instances (```taskkill /f /im node.exe``` for windows)

##  **Starting the Server and all sub-processes**

This is the easier part. Make a note that you will need to use __python3.6__.

Run the following commands:

```
pip3 install skikit-image
pip3 install scipy
pip3 install https://download.pytorch.org/whl/cu90/torch-1.0.1-cp36-cp36m-win_amd64.whl
pip3 install torchvision
pip3 install flask
pip3 install opencv-contrib-python
pip3 import numpy
```
There may be more dependencies that you will need to install with pip

To start the server, just double click the file named runner.bat.
On one of the windows you will be given a new URL containing the phrase 'serveo.net'.
Copy the entire URL, go the the DialogFlow tab in your browser, and click on the Fulfillment tab in the left-hand panel, change the URL for the Webhook, and click save. -- It should be something like <https://random.serveo.net/start> **The ```/start``` is very important**
Now you should be able to start the modes, by calling on the google home assistant, and saying:
**"Talk to my Test App"** followed by **"Start safe driving mode"** for sleep detection, or **"Start driving assistant"** to start the HUD.


Have Fun!

### Notes

1) This is still in production.
2) This program will only work with 2 webcams. The first one is used by the _Driver Assistant_ and the second one is used by _Safe Driving Mode_
3) This has only been tested on windows 10, you might need to change some things for different operating systems.
4) Make sure you have python3.6 installed and all the dependencies should be added to that.
