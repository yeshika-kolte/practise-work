'''12. Authentication System
Problem Statement

Users can login using multiple methods.

Create:

abstract class Authentication

Child:

OTPAuth
GoogleAuth
FingerprintAuth'''

from abc import ABC, abstractmethod

class Authentication(ABC):

    @abstractmethod
    def login(self):
        pass


class OTPAuth(Authentication):

    def __init__(self, phone):
        self.phone = phone

    def login(self):
        print(f"Login successful using OTP sent to {self.phone}")


class GoogleAuth(Authentication):

    def __init__(self, email):
        self.email = email

    def login(self):
        print(f"Login successful using Google account {self.email}")


class FingerprintAuth(Authentication):

    def __init__(self, user_id):
        self.user_id = user_id

    def login(self):
        print(f"Login successful using fingerprint for user {self.user_id}")


o = OTPAuth("9876543210")
g = GoogleAuth("user@gmail.com")
f = FingerprintAuth("U101")

o.login()
g.login()
f.login()