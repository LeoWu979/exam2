# hw3

### setup<br> 
- uLCD : tx <-> D1, rx <-> D0, reset <-> D2.<br>
- use "sudo screen /dev/ttyACM*" to open screen on terminal.


### Gesture mode : <br>
- Use "/Gesture_UI/run 1" to start the Gesture_UI mode.<br>
- You will see LED1 to be turned on.
- "Ring" : 0, "slope" : 1, "down" : 2.<br>
- Current mode will both show on the uLCD and terminal.<br>
- Published message will received by python and python will send "/Gesture/run 0" to stop the Gesture_UI mode.<br>

### send_data mode : <br>
- This can send the data to python.<br>
- Then python will receive the data to plot.<br>

