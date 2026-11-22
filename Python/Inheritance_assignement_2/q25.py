from abc import ABC, abstractmethod

class WorkReport(ABC):
    @abstractmethod
    def submit_report(self):
        pass

class DeveloperReport(WorkReport):
    def submit_report(self):
        print("Developer submitted report")

class TesterReport(WorkReport):
    def submit_report(self):
        print("Tester submitted report")

class ManagerReport(WorkReport):
    def submit_report(self):
        print("Manager submitted report")

obj1 = DeveloperReport()
obj1.submit_report()

obj2 = TesterReport()
obj2.submit_report()

obj3 = ManagerReport()
obj3.submit_report()