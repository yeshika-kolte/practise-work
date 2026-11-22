'''28. Authentication System

Abstract:

Authentication

Derived:

OTPAuth
GoogleAuth
FacebookAuth'''
from abc import ABC, abstractmethod


class Authentication(ABC):

    @abstractmethod
    def login(self):
        pass

class OTPAuth(Authentication):

    def login(self):
        print("Login successful using OTP Authentication")


class GoogleAuth(Authentication):

    def login(self):
        print("Login successful using Google Authentication")


class FacebookAuth(Authentication):

    def login(self):
        print("Login successful using Facebook Authentication")


o1 = OTPAuth()
o1.login()
g1 = GoogleAuth()
g1.login()
f1 = FacebookAuth()
f1.login()


