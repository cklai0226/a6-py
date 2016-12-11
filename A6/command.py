import Queue
from observer import Observable, Observer

class A6Command(Observer):
    """
      A6 Base Command Class
    """
    pass

class SMSNewShortMessage(A6Command):
    """
      SMS Command Class
    """
    SMS_TEXT = "+CMT"

    def __init__(self):
        self.init = False
        self.queue = Queue.Queue(2)

    def update(self, observable, arg):
        if arg[:4] == self.SMS_TEXT:
            self.init = True

        if self.init:
            self.queue.put(arg)

        if self.queue.full() is False:
            return

        try:
            while not self.queue.empty():
                pdu_message = self.queue.get()

            print pdu_message
        finally:
            self.init = False
