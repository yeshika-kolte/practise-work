from abc import ABC, abstractmethod

class ChatBot(ABC):
    @abstractmethod
    def reply(self):
        pass

class SupportBot(ChatBot):
    def reply(self):
        print("Hello from SupportBot")

class SalesBot(ChatBot):
    def reply(self):
        print("Hello from SalesBot")

class FAQBot(ChatBot):
    def reply(self):
        print(" Hello from FAQBot")

obj1 = SupportBot()
obj1.reply()

obj2 = SalesBot()
obj2.reply()

obj3 = FAQBot()
obj3.reply()