START py -3.6 Server-Runner.py
@echo Main ready
timeout 2
START py -3.6 script.py
@echo Sleep Ready
cd driverassistant/ObjectDetection
timeout 2
@echo Assistant Ready
START py -3.6 maincameraloop.py
ssh -R 80:127.0.0.1:7000 serveo.net &