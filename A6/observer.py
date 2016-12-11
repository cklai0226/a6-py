

class Observer(object):
    """
    Observer class implementation
    http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Observer.html
    """
    def update(self, observable, arg):
        """
        Called when the observed object is
        modified. You call an Observable object's
        notifyObservers method to notify all the
        object's observers of the change.
        """

        pass

class Observable(object):
    """
    Observable class implementation
    http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Observer.html
    """
    def __init__(self):
        self.obs = []
        self.changed = 0

    def register(self, observer):
        """
        Register observer in list
        """
        if observer not in self.obs:
            self.obs.append(observer)

    def unregister(self, observer):
        """
        Unregister observer in list
        """
        self.obs.remove(observer)

    def notify(self, arg=None):
        """
        If 'changed' indicates that this object
        has changed, notify all its observers, then
        call clearChanged(). Each observer has its
        update() called with two arguments: this
        observable object and the generic 'arg'.
        """

        if not self.changed:
            return
        # Make a local copy in case of synchronous
        # additions of observers:
        localArray = self.obs[:]
        self.clearChanged()

        # Updating is not required to be synchronized:
        for observer in localArray:
            observer.update(self, arg)

    def count(self):
        return len(self.obs)

    def setChanged(self):
        self.changed = True

    def clearChanged(self):
        self.changed = False

    def hasChanged(self):
        return self.changed