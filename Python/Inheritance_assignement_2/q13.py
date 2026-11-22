'''13. File Export System
Problem Statement

Application exports files in multiple formats.

Create:

abstract class Exporter

Child:

PDFExporter
ExcelExporter
CSVExporter'''

from abc import ABC, abstractmethod

class Exporter(ABC):

    @abstractmethod
    def export(self):
        pass


class PDFExporter(Exporter):

    def export(self):
        print("File exported in PDF format")


class ExcelExporter(Exporter):

    def export(self):
        print("File exported in Excel format")


class CSVExporter(Exporter):

    def export(self):
        print("File exported in CSV format")


p = PDFExporter()
e = ExcelExporter()
c = CSVExporter()

p.export()
e.export()
c.export()