import matplotlib.pyplot as plt
import numpy as np
import time
import serial

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev)


line1 = s.readline()
l1 = []
l2 = []


if (str(line1) == 'START') :
    for i in range(10):
        f = s.readline()
        l1.append(f)
    for i in range(10):
        f1 = s.readline()
        l2.append(f1)


t1 = [1:11:1]

figure(1)
plot(t1,l1)
ylabel('The extracted features')
figure(2)
plot(t1,l2)
ylabel('The classified gesture events')
