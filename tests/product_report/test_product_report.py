from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        "1",
        "Farinha",
        "Farinini",
        "01-02-2023",
        "02-02-2024",
        "12345",
        "em local fresco e seco",
    )

    assert (product.__repr__()) == (
        "O produto Farinha"
        " fabricado em 01-02-2023"
        " por Farinini com validade"
        " até 02-02-2024"
        " precisa ser armazenado em local fresco e seco."
    )
