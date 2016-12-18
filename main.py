import time
from A6.command import SMSNewShortMessage
from A6.communication import A6Communication
import serial

# self.serialport.write('ath\r');
# time.sleep(2)
# self.serialport.write('atd33443744;\r')
# self.serialport.write('AT\r')
# self.serialport.write('ATI\r')
# self.serialport.write('AT+CNUM\r')
# self.serialport.write('AT+CCID\r')

# self.serialport.write('AT+CREG?\r')
# self.serialport.write('AT+CSQ\r')

class SmsSendCommand(object):

    """
    Class to send SMS on A6 gsm/gprs chip
    """

    def __init__(self, port):

        self.serialport = port

    def send(self):
        """
        send sms
        """

        self.serialport.write('at+cmgf=1\r')
        time.sleep(2)

        self.serialport.write('at+cmgs=\"999349859"')
        self.serialport.write('\r\n')
        time.sleep(2)

        self.serialport.write('GSM A6 test mesage!')
        time.sleep(0.5)

        self.serialport.write("\x1a")




serialcom = serial.Serial()

serialcom.port = '/dev/ttyAMA0'
serialcom.baudrate = 115200
serialcom.parity = serial.PARITY_NONE
serialcom.stopbits = serial.STOPBITS_ONE
serialcom.bytesize = serial.EIGHTBITS

serialcom.open()

serialcom.reset_input_buffer()
serialcom.reset_output_buffer()

t = A6Communication(serialcom)
t.register(SMSNewShortMessage())

t.setDaemon(True)
t.start()

while True:
    time.sleep(3)
print "Exiting Main Thread"

# self.serialport.write('AT')
# time.sleep(3)

# while 1:
#  self.serialport.write('AT')
#  x=self.serialport.read()
