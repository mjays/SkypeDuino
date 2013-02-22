import Skype4Py
import sys
import serial

class MySkypeEvents:
    def UserStatus(self, Status):
        print 'The status of the user changed to ' + Status
        if Status == 'ONLINE':
        	s.write(b'g')
        elif Status == 'AWAY':
        	s.write(b'y')
        elif Status == 'DND':
        	s.write(b'r')
        else:
        	s.write(b'0')


s = serial.Serial(port='/dev/tty.usbserial-A7006Qu2', baudrate=9600)

skype = Skype4Py.Skype(Events=MySkypeEvents())
skype.FriendlyName = 'Skype4Py_Example'
skype.Attach()
while 1:
	print "idling"

print "Attachment status is " + str(skype.AttachmentStatus)

