from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        "1",
        "name",
        "brand",
        "01-02-2023",
        "01-02-2024",
        "1",
        "storage"
    )

    assert product.id == "1"
    assert product.nome_do_produto == "name"
    assert product.nome_da_empresa == "brand"
    assert product.data_de_fabricacao == "01-02-2023"
    assert product.data_de_validade == "01-02-2024"
    assert product.numero_de_serie == "1"
    assert product.instrucoes_de_armazenamento == "storage"
