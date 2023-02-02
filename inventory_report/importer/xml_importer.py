from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(path) as xml_file:
            data = xmltodict.parse(xml_file.read())
            return data["dataset"]["record"]
