#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pybleno import *
import sys
import signal
from LightService import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.IN)

bleno = Bleno()
primaryService = LightService()

def onStateChange(state):
	if (state == 'poweredOn'):
		print("bluetooth power on")
		bleno.startAdvertising('led service', ['ff10'])

bleno.on('stateChange', onStateChange)

def onAdvertisingStart(err):
	if not err:
		def on_setServiceError(error):
			print('setServices: %s' % ('error ' + error if error else 'success'))

		bleno.setServices([
			primaryService
		], on_setServiceError)
		print("start advertise")

bleno.on('advertisingStart', onAdvertisingStart)

bleno.start()
print("peripheral start")

print ('Hit <ENTER> to disconnect')

if (sys.version_info > (3, 0)):
	input()
else:
	raw_input()

bleno.stopAdvertising()
bleno.disconnect()
GPIO.output(25, GPIO.LOW)
GPIO.cleanup()

print ('terminated.')
sys.exit(1)
