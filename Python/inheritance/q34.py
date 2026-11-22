from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def upload(self):
        pass

    @abstractmethod
    def download(self):
        pass

class GoogleDrive(CloudStorage):
    def upload(self):
        print("File uploaded to Google Drive")

    def download(self):
        print("File downloaded from Google Drive")


class Dropbox(CloudStorage):
    def upload(self):
        print("File uploaded to Dropbox")

    def download(self):
        print("File downloaded from Dropbox")

obj1 = GoogleDrive()
obj1.upload()
obj1.download()
obj2 = Dropbox()
obj2.upload()
obj2.download()