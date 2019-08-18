
class Observable:
    """Any observers that wants to listen to what I have to say, come subscribe now!"""
    def __init__(self,name=None):
        """set can not have duplicate items and always ordered"""
        self.observers = []
        self.__name__ = name
        print("%s Observable instantiated" % self.__name__)

    """add observer to our subscription set"""
    def subscribe(self, observer):
        observer._subscribed_to.append(self)
        if observer not in self.observers:
            self.observers.append(observer)
        print("\n%s subscribed to %s" % (observer.__name__,self.__name__))

    """remove observer from our subscription set"""
    def unsubscribe(self, observer):
        observer._subscribed_to.remove(self)
        self.observers.remove(observer)
        print("\n%s unsubscribed to %s" % (observer.__name__,self.__name__))

    """notify_subscribers"""
    def notify_subscribers(self,message):
        for observer in self.observers:
            observer.update("%s" % message,self)

    """wake up"""
    def wake_up(self):
        print("\n\033[1;31;40mEVENT/STATUS:\033[0;37;0m %s: wake_up" % (self.__name__))
        self.notify_subscribers("waking up")

    """eat breakfast"""
    def eat_breakfast(self):
        print("\n\033[1;31;40mEVENT/STATUS:\033[0;37;0m %s: eat_breakfast" % (self.__name__))
        self.notify_subscribers("eating breakfast")

    """brush teeth"""
    def brush_teeth(self):
        print("\n\033[1;31;40mEVENT/STATUS:\033[0;37;0m %s: brush_teeth" % (self.__name__))
        self.notify_subscribers("brushing teeth")

    """go to work"""
    def go_to_work(self):
        print("\n\033[1;31;40mEVENT/STATUS:\033[0;37;0m %s: going to work" % (self.__name__))
        self.notify_subscribers("going to work")

    """pickup kids"""
    def pickup_kids(self):
        print("\n\033[1;31;40mEVENT/STATUS:\033[0;37;0m %s: picking up kids" % (
         self.__name__))
        self.notify_subscribers("picking up kids")

    """eat dinner"""
    def eat_dinner(self):
        print("\n\033[1;31;40mEVENT/STATUS:\033[0;37;0m %s: eating dinner" % (self.__name__))
        self.notify_subscribers("eating dinner")

    """go to sleep"""
    def go_to_sleep(self):
        print("\n\033[1;31;40mEVENT/STATUS:\033[0;37;m %s: going to sleep" % (self.__name__))
        self.notify_subscribers("going to sleep")

    "teach"
    def teach_subject(self,subject=""):
        print("\n\033[1;31;40mEVENT/STATUS:\033[0;37;0m %s: teach_subject-%s" % (self.__name__,subject))
        self.notify_subscribers("teaching %s" % subject)

class Observer(object):
    def __init__(self,name):
        self._subscribed_to = []
        self.__name__ = name
        print("%s Observer instantiated" % self.__name__)

    """default callback method is update"""
    def update(self,message,observable):
        print("--------%s observation(%s:%s)" % (self.__name__,observable.__name__,message))
        self.do_something(observable=observable,message=message)
        pass

    def do_something(self,observable,message):
        """Do something if/elseif"""
        if message == "going to sleep":
            print("\033[1;31;40mACTION:\033[0;37;0m %s: unsubscribing from %s" % (self.__name__,observable.__name__))
            observable.unsubscribe(self)
        elif message == "going to work":
            print("\033[1;31;40mACTION:\033[0;37;0m %s: unsubscribing from %s" % (self.__name__, observable.__name__))
            observable.unsubscribe(self)
        else:
            print("-------- %s has no action for:(%s)" % (self.__name__, message))

    def get_subscribed_to(self):
        return self._subscribed_to

    def unsubscribe_all(self):
        for subscription in self._subscribed_to:
            subscription.unsubscribe(self)

def simulate():

    print("SIMULATING OUR DAY. CHILDREN AS OBSERVERS, ADULTS AS OBSERVABLES")
    print("SIMULATING A SEQUENCE OF OBSERVABLE EVENTS WHEN OBSERVED")

    """instantiate observables"""
    observable_dad_obj = Observable(name="\033[0;31;0mdad\033[0;37;0m")
    observable_mom_obj = Observable(name="\033[0;33;0mmom\033[0;37;0m")
    observable_elementary_teacher_obj = Observable(name="\033[0;36;0melementary_teacher\033[0;37;0m")
    observable_daycare_teacher_obj = Observable(name="\033[0;30;0mdaycare_teacher\033[0;37;0m")

    """instantiate observers"""
    observer_john_obj = Observer(name="\033[0;32;0mlittle-john\033[0;37;0m")
    observer_sam_obj = Observer(name="\033[0;34;0mbig-sam\033[0;37;0m")
    observer_sally_obj = Observer(name="\033[0;35;0mbaby-sally\033[0;37;0m")



    """subscribe observers to observable dad"""
    observable_dad_obj.subscribe(observer_john_obj)
    observable_dad_obj.subscribe(observer_sam_obj)

    """subscribe observers to observable mom"""
    observable_mom_obj.subscribe(observer_sally_obj)

    observable_mom_obj.wake_up()

    observable_dad_obj.wake_up()

    observable_dad_obj.eat_breakfast()
    observable_mom_obj.eat_breakfast()

    observable_dad_obj.brush_teeth()

    observable_dad_obj.go_to_work()

    observable_mom_obj.subscribe(observer_john_obj)
    observable_mom_obj.subscribe(observer_sam_obj)

    observable_mom_obj.brush_teeth()

    observable_mom_obj.go_to_work()

    observable_elementary_teacher_obj.subscribe(observer_john_obj)
    observable_elementary_teacher_obj.subscribe(observer_sam_obj)
    observable_daycare_teacher_obj.subscribe(observer_sally_obj)

    observable_elementary_teacher_obj.teach_subject("Math")
    observable_daycare_teacher_obj.teach_subject("Reading")
    observable_elementary_teacher_obj.unsubscribe(observer_john_obj)
    observable_elementary_teacher_obj.unsubscribe(observer_sam_obj)
    observable_daycare_teacher_obj.unsubscribe(observer_sally_obj)
    observable_dad_obj.subscribe(observer_john_obj)
    observable_dad_obj.subscribe(observer_sam_obj)
    observable_dad_obj.subscribe(observer_sally_obj)
    observable_dad_obj.pickup_kids()

    observable_mom_obj.subscribe(observer_john_obj)
    observable_mom_obj.subscribe(observer_sam_obj)
    observable_mom_obj.subscribe(observer_sally_obj)

    observable_dad_obj.eat_dinner()
    observable_mom_obj.eat_dinner()

    observable_dad_obj.go_to_sleep()
    observable_mom_obj.go_to_sleep()


simulate()







