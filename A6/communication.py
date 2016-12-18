from threading import Thread
from observer import *

class A6Communication(Thread, Observable):
    """Threaded A6 communication """
    def __init__(self, comm):
        super(A6Communication, self).__init__()
        Observable.__init__(self)

        self.comm = comm

    def run(self):
        while True:
            mes = self.comm.readline()

            self.setChanged()
            self.notify(mes)
