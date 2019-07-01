from pybleno import *
from ReadWriteCharacteristic import *
from NotifyCharacteristic import *

class LightService(BlenoPrimaryService):
	def __init__(self):
		BlenoPrimaryService.__init__(self, {
			'uuid': 'ff10',
			'characteristics': [
				ReadWriteCharacteristic(),
				NotifyCharacteristic()
			]})
