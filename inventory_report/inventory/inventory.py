from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        if path.endswith(".csv"):
            data = CsvImporter.import_data(path)
        elif path.endswith(".json"):
            data = JsonImporter.import_data(path)
        elif path.endswith(".xml"):
            data = XmlImporter.import_data(path)
        else:
            raise ValueError("Arquivo inválido")
        if report_type == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)
