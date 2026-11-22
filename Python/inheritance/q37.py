from abc import ABC, abstractmethod

class SocialLogin(ABC):
    @abstractmethod
    def login(self):
        pass

class GoogleLogin(SocialLogin):
    def login(self):
        print("Google Login")

class GitHubLogin(SocialLogin):
    def login(self):
        print("GitHub Login")

class LinkedInLogin(SocialLogin):
    def login(self):
        print("LinkedIn Login")


obj1 = GoogleLogin()
obj1.login()
obj2 = GitHubLogin()
obj2.login()
obj3 = LinkedInLogin()
obj3.login()