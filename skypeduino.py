import Skype4Py
import sys
import serial

class MySkypeEvents:
  def CallStatus(self, Call, Status):
    print 'The Call status has changed to ' + Status
    if Status == 'INPROGRESS':
      s.write(b'r')
    elif Status == 'FINISHED':
      s.write(b'g')
    elif Status == 'CANCELLED':
      s.write(b'g')
    elif Status == 'RINGING':
      s.write(b'y')
    elif Status == 'UNPLACED':
      s.write(b'y')
    elif Status == 'ROUTING':
      s.write(b'y')
    elif Status == 'EARLYMEDIA':
      s.write(b'y')
    else:
      s.write(b'g')
  
  def Mute(self, Mute):
    print 'Current Mic status: ' + str(Mute)
  
  def Notify(self, Notification):
    if Notification == 'MUTE OFF':
      print 'Signaling MUTE OFF'
      s.write(b'r')
    elif Notification == 'MUTE ON':
      print 'Signaling MUTE ON'
      s.write(b'y')

s = serial.Serial(port='/dev/tty.usbserial-A7006TaZ', baudrate=9600)

skype = Skype4Py.Skype(Events=MySkypeEvents())
skype.FriendlyName = 'Skype4Py_Example'
skype.Attach()
print "Attachment status is " + str(skype.AttachmentStatus)

while 1:
  i = 1

