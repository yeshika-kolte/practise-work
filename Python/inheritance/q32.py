from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class MySQL(Database):
    def connect(self):
        print("MySQL Connected")

    def disconnect(self):
        print("MySQL Disconnected")

class MongoDB(Database):
    def connect(self):
        print("MongoDB Connected")

    def disconnect(self):
        print("MongoDB Disconnected")

class PostgreSQL(Database):
    def connect(self):
        print("PostgreSQL Connected")

    def disconnect(self):
        print("PostgreSQL Disconnected")


obj1 = MySQL()
obj1.connect()
obj1.disconnect()
obj2 = MongoDB()
obj2.connect()
obj2.disconnect()
obj3 = PostgreSQL()
obj3.connect()
obj3.disconnect()