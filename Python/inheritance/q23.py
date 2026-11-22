'''23. Notification System

Abstract:

Notification

Derived:

EmailNotification
SMSNotification
PushNotification'''

class Notification:

    def notification(self):
        pass

class EmailNotification(Notification):

    def notification(self):
        print("You received an Email notification ")

class SMSNotification(Notification):

    def notification(self):
        print("You received a SMS notification ")

class PushNotification(Notification):

    def notification(self):
        print("You received a notification ")


email = EmailNotification()
email.notification()

sms = SMSNotification()
sms.notification()

push = PushNotification()
push.notification()