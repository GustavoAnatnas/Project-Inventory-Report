class SimpleReport:
    @classmethod
    def generate(cls, inventory: list):
        manufacturing_date = cls.manufacturer_date(inventory)
        expiration_date = cls.get_expiration_date(inventory)
        bigger_company = cls.get_bigger_company(inventory)

        return (
            f"Data de fabricação mais antiga: {manufacturing_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com mais produtos: {bigger_company}"
        )

    @staticmethod
    def manufacturer_date(inventory):
        return min([inven["data_de_fabricacao"] for inven in inventory])

    @staticmethod
    def get_expiration_date(inventory):
        return min([inven["data_de_validade"] for inven in inventory])

    @staticmethod
    def get_bigger_company(inventory):
        companies = [inven["nome_da_empresa"] for inven in inventory]
        return max(set(companies), key=companies.count)
