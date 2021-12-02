#!/usr/bin/env python

import time
import os
from PyP100 import PyP100

PASS = os.environ.get("TPLINK_PASS")
LOGIN = os.environ.get("TPLINK_LOGIN")
PLUG_IP = os.environ.get("TPLINK_PLUG_IP")

p100 = PyP100.P100(PLUG_IP, LOGIN, PASS)

i = 0
while True or (i < 30):
    try:
        i += 1
        p100.handshake()
        break
    except ConnectionError:
        time.sleep(60)
p100.handshake()
p100.login()
device = p100.getDeviceInfo()['result']

if device['device_on']:
    p100.turnOff()
    time.sleep(5)
p100.turnOn()
print('Plug has been reloaded')

