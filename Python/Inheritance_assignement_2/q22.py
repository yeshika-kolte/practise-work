from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send_notification(self):
        pass

class EmailNotification(Notification):
    def send_notification(self):
        print("Notification sent using Email")

class SMSNotification(Notification):
    def send_notification(self):
        print("Notification sent using SMS")

class PushNotification(Notification):
    def send_notification(self):
        print("Notification sent using Push Notification")


obj1 = EmailNotification()
obj1.send_notification()

obj2 = SMSNotification()
obj2.send_notification()

obj3 = PushNotification()
obj3.send_notification()