from pybleno import Characteristic
import array
import struct
import RPi.GPIO as GPIO

class ReadWriteCharacteristic(Characteristic):

	def __init__(self):
		Characteristic.__init__(self, {
			'uuid': 'ff11',
			'properties': ['read', 'write'],
			'value': None
			})
		self._value = array.array('B', [0])

	def onReadRequest(self, offset, callback):
		print('SwitchCharacteristic - %s - onReadRequest: value = %s' % (self['uuid'], self._value[0]))
		callback(Characteristic.RESULT_SUCCESS, self._value)

	def onWriteRequest(self, data, offset, withoutResponse, callback):
		global ledState
		self._value = data

		print('SwitchCharacteristic - %s - onWriteRequest: value = %s' % (self['uuid'], data[0]))

		#Set GPIO pin 40 HIGH or LOW
		if data[0] == 1:
			GPIO.output(25, GPIO.HIGH)
			ledState = GPIO.HIGH
			print("LED is ON!")
		elif data[0] == 0:
			GPIO.output(25, GPIO.LOW)
			ledState = GPIO.LOW
			print("LED is OFF!")
		else:
			print("Unknown message!")

		callback(Characteristic.RESULT_SUCCESS)

	def onSubscribe(self, maxValueSize, updateValueCallback):
		print('SwitchCharacteristic - onSubscribe')

		self._updateValueCallback = updateValueCallback

	def onUnsubscribe(self):
		print('SwitchCharacteristic - onUnsubscribe');

		self._updateValueCallback = None
