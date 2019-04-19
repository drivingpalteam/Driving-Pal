# Driving-Pal

**To start running this project, you will first need to set up Google's DialogFlow API.**

1) Simply go the https://dialogflow.com/, sign in and click on go to console in the top right.
2) Create a new agent and once it has finished creating, click on the gear icon next to the agent name.
3) Click on the Export and Import tab, and choose import from zip.
4) Drag and drop the DrivingPalVoice.zip file and confirm.
5) You will now have a working DialogFlow Agent, but you will need to change the fulfillment later.

**Setting up Driver Assistant:**

1) Download the files here: https://drive.google.com/drive/folders/1lnuWNgmTD-R-IiiVln8bJ7lQSHiR8IAm?usp=sharing
2) Make sure to extract the driverassitant zip to the Driving-Pal folder.
3) Install NodeJS: https://nodejs.org/en/download/
4) "npm install -g browserify" (run as admin)

##  **Starting the Server and all sub-processes**

This is the easier part. Make a note that you will need to use __python3.6__
Run the following commands:

```
pip3 install flask
pip3 install opencv-contrib-python
pip3 import numpy
```
There may be more dependencies that you will need to install with pip

To start the server, just use a terminal to run the Server-Runner.py file. **_Use Python 3.6_**
You will now get a message in the terminal saying that everything is initialized, and you will be given a new URL.
Go the the DialogFlow tab in your browser, and click on the Fulfillment tab in the left-hand panel, change the URL for the Webhook, and click save.
Now you should be able to start the modes, by calling on the google home assistant, and saying:
**"Talk to my Test App"** followed by **"Start safe driving mode"** for sleep detection, or **"Start driving assistant"** to start the HUD.
