# DEVASC_200-901_STUDY
<p>Author: Jason Ray Norris</p>
<h4>Developed using Python3.7.4</h4>
<hr>
<h5>*!WORK IN PROGRESS!* 1.6 Identify the advantages of common design patterns (MVC and Observer)
</h5>
<hr>

Note: Either of these can be considered an architecture(think big picture) or a design pattern(think smaller). These descriptions can also be used synonymously.

<h6>Section 1.6.1</h6>
# What is MVC?

<h6>Section 1.6.2.1</h6>

# What is Observer pattern?


<h5>My plan for covering this topic is the same all over the internet.  They stole my idea! Just kidding of course. We'll try to cater this towards networking.</h5>

An observer pattern as a basic description is one-to-many(observable-to-observed) application design pattern. 

Very basic comparable networking example:
1. Think of objects being a hub(observable) and spoke(observer). When you plug your device into the hub, you are physically registering your device to the messages being broadcast by the hub.
</p>

Some very common applications that generally use this design pattern today:
1. Chat programs
3. Social Media Feeds
   
Anytime you(object) are registering to a subscriber list, you are likely using this pattern.

<img src="https://i.ibb.co/Wxw7j1q/observer-pattern.jpg">
<br>
<br>

This is a synchronous pattern.  All Observers get notified at the same time. In similar concept result of a broadcast UDP.  Fire and forget. However, This is still an iteration of single targets..

Observations:
<br>
&nbsp;&nbsp;1. Simple
<br>
&nbsp;&nbsp;2. No transaction guarantee
<br>
&nbsp;&nbsp;3. Low overhead
 <br>
&nbsp;&nbsp;4. Poor scaling design
<br>
<hr>
<h6>Section 1.6.2.2</h6>

# Additional Observer pattern details?

There are some over overlapping terms within the industry.  The terms belows are commonly interchanged, but may have subtle differences.
Feel free to ignore the rest of this section.  I think it's important to understand the differences.

Interchanged Terms:
    <br>
    1. Observer Model,Pub-Sub Model,Event and Listener Model
    <br>
    2. Observer, Subscriber, Event Listener
    <br>
    3. Observable, Publisher, Event and Channel


Some consider the following models as types of observer models or synonymous in some ways.

Pub-Sub is a distributed architecture. From Publisher to MQ is generally synchronous.  MQ to subscriber is generally asynchronous message que'ing.
<br>
This is a more distributed model. We also don't care about the message recipient delivery order.

Observations:
1. Better transaction guarantee.
2. Better decoupling of responsibility.
3. Poor consistency across listeners with coupled functionality.
4. Greater scaling design

<img src="https://i.ibb.co/KjJd36X/pub-sub.png" >

Events can be described as messages in an MQ or any channel feed.

<h6>Section 1.6.2.3</h6>

# Let's look at some examples

The code below represents a family of 5.  Lets make the two parents observables and the three children observers.  We can simulate some events to see how this model might operate.
<br>
There is ANSI color code in this code.  The output is much easier to read and follow in a terminal.

Let's cover the concepts below.

Reference: observer.py
<pre>

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
</pre>

output:
<pre>
SIMULATING OUR DAY. CHILDREN AS OBSERVERS, ADULTS AS OBSERVABLES
SIMULATING A SEQUENCE OF OBSERVABLE EVENTS WHEN OBSERVED
dad Observable instantiated
mom Observable instantiated
elementary_teacher Observable instantiated
daycare_teacher Observable instantiated
little-john Observer instantiated
big-sam Observer instantiated
baby-sally Observer instantiated

little-john subscribed to dad

big-sam subscribed to dad

baby-sally subscribed to mom

EVENT/STATUS: mom: wake_up
--------baby-sally observation(mom:waking up)
-------- baby-sally has no action for:(waking up)

EVENT/STATUS: dad: wake_up
--------little-john observation(dad:waking up)
-------- little-john has no action for:(waking up)
--------big-sam observation(dad:waking up)
-------- big-sam has no action for:(waking up)

EVENT/STATUS: dad: eat_breakfast
--------little-john observation(dad:eating breakfast)
-------- little-john has no action for:(eating breakfast)
--------big-sam observation(dad:eating breakfast)
-------- big-sam has no action for:(eating breakfast)

EVENT/STATUS: mom: eat_breakfast
--------baby-sally observation(mom:eating breakfast)
-------- baby-sally has no action for:(eating breakfast)

EVENT/STATUS: dad: brush_teeth
--------little-john observation(dad:brushing teeth)
-------- little-john has no action for:(brushing teeth)
--------big-sam observation(dad:brushing teeth)
-------- big-sam has no action for:(brushing teeth)

EVENT/STATUS: dad: going to work
--------little-john observation(dad:going to work)
ACTION: little-john: unsubscribing from dad

little-john unsubscribed to dad

little-john subscribed to mom

big-sam subscribed to mom

EVENT/STATUS: mom: brush_teeth
--------baby-sally observation(mom:brushing teeth)
-------- baby-sally has no action for:(brushing teeth)
--------little-john observation(mom:brushing teeth)
-------- little-john has no action for:(brushing teeth)
--------big-sam observation(mom:brushing teeth)
-------- big-sam has no action for:(brushing teeth)

EVENT/STATUS: mom: going to work
--------baby-sally observation(mom:going to work)
ACTION: baby-sally: unsubscribing from mom

baby-sally unsubscribed to mom
--------big-sam observation(mom:going to work)
ACTION: big-sam: unsubscribing from mom

big-sam unsubscribed to mom

little-john subscribed to elementary_teacher

big-sam subscribed to elementary_teacher

baby-sally subscribed to daycare_teacher

EVENT/STATUS: elementary_teacher: teach_subject-Math
--------little-john observation(elementary_teacher:teaching Math)
-------- little-john has no action for:(teaching Math)
--------big-sam observation(elementary_teacher:teaching Math)
-------- big-sam has no action for:(teaching Math)

EVENT/STATUS: daycare_teacher: teach_subject-Reading
--------baby-sally observation(daycare_teacher:teaching Reading)
-------- baby-sally has no action for:(teaching Reading)

little-john unsubscribed to elementary_teacher

big-sam unsubscribed to elementary_teacher

baby-sally unsubscribed to daycare_teacher

little-john subscribed to dad

big-sam subscribed to dad

baby-sally subscribed to dad

EVENT/STATUS: dad: picking up kids
--------big-sam observation(dad:picking up kids)
-------- big-sam has no action for:(picking up kids)
--------little-john observation(dad:picking up kids)
-------- little-john has no action for:(picking up kids)
--------baby-sally observation(dad:picking up kids)
-------- baby-sally has no action for:(picking up kids)

little-john subscribed to mom

big-sam subscribed to mom

baby-sally subscribed to mom

EVENT/STATUS: dad: eating dinner
--------big-sam observation(dad:eating dinner)
-------- big-sam has no action for:(eating dinner)
--------little-john observation(dad:eating dinner)
-------- little-john has no action for:(eating dinner)
--------baby-sally observation(dad:eating dinner)
-------- baby-sally has no action for:(eating dinner)

EVENT/STATUS: mom: eating dinner
--------little-john observation(mom:eating dinner)
-------- little-john has no action for:(eating dinner)
--------big-sam observation(mom:eating dinner)
-------- big-sam has no action for:(eating dinner)
--------baby-sally observation(mom:eating dinner)
-------- baby-sally has no action for:(eating dinner)

EVENT/STATUS: dad: going to sleep
--------big-sam observation(dad:going to sleep)
ACTION: big-sam: unsubscribing from dad

big-sam unsubscribed to dad
--------baby-sally observation(dad:going to sleep)
ACTION: baby-sally: unsubscribing from dad

baby-sally unsubscribed to dad

EVENT/STATUS: mom: going to sleep
--------little-john observation(mom:going to sleep)
ACTION: little-john: unsubscribing from mom

little-john unsubscribed to mom
--------baby-sally observation(mom:going to sleep)
ACTION: baby-sally: unsubscribing from mom

baby-sally unsubscribed to mom
</pre>

<hr>
<h6>Section 1.6.3</h6>

# Wow, what now?

Isn't this a cool way to communicate between objects?  Now lets look at how this might apply to networks.

Reference: https://docs.python.org/3/howto/sockets.html
 
We will cover some ready-to-use WEB API frameworks in later topics.

I started working on a low level controller/client(observable/observer) framework for concept example.

Check out these files(*INCOMPLETE):

1. controller_observable.py
1. controller_observer.py






