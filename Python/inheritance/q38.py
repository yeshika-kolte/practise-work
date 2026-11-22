from abc import ABC, abstractmethod

class CompressionTool(ABC):
    @abstractmethod
    def compress(self):
        pass

class ZIPCompression(CompressionTool):
    def compress(self):
        print("ZIP Compression")

class RARCompression(CompressionTool):
    def compress(self):
        print("RAR Compression")


obj1 = ZIPCompression()
obj1.compress()
obj2 = RARCompression()
obj2.compress()