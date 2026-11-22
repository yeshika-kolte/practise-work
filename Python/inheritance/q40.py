from abc import ABC, abstractmethod

class AIChatbot(ABC):
    @abstractmethod
    def reply(self):
        pass

class SupportBot(AIChatbot):
    def reply(self):
        print("Hello SupportBot")

class SalesBot(AIChatbot):
    def reply(self):
        print("Hello SalesBot")

obj1 = SupportBot()
obj1.reply()
obj2 = SalesBot()
obj2.reply()