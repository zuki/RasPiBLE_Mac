from pybleno import Characteristic
import array
import struct
import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(24, GPIO.IN)
#GPIO.setup(25, GPIO.OUT)

class NotifyCharacteristic(Characteristic):

	def __init__(self):
		Characteristic.__init__(self, {
			'uuid': 'ff12',
			'properties': ['notify'],
			'value': None
			})
		self._value = array.array('B', [0])

	def onSubscribe(self, maxValueSize, updateValueCallback):
		print('SwitchCharacteristic - onSubscribe')

		self._updateValueCallback = updateValueCallback

		GPIO.add_event_detect(24, GPIO.RISING, callback=self.onoff_callback, bouncetime=200)

	def onUnsubscribe(self):
		print('SwitchCharacteristic - onUnsubscribe');

		self._updateValueCallback = None

	def onoff_callback(self, channel):
		if channel == 24:
			self._value[0] = not self._value[0]
			GPIO.output(25, self._value[0])
			self._updateValueCallback(self._value)
