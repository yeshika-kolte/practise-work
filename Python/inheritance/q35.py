from abc import ABC, abstractmethod

class MessagingApp(ABC):
    @abstractmethod
    def send_message(self):
        pass

class WhatsApp(MessagingApp):
    def send_message(self):
        print("Message sent on WhatsApp")

class Telegram(MessagingApp):
    def send_message(self):
        print("Message sent on Telegram")

class Signal(MessagingApp):
    def send_message(self):
        print("Message sent on Signal")


obj1 = WhatsApp()
obj1.send_message()
obj2 = Telegram()
obj2.send_message()
obj3 = Signal()
obj3.send_message()