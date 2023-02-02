from inventory_report.reports.simple_report import SimpleReport
# from collections import Counter


class CompleteReport:
    @classmethod
    def generate(cls, inventory_list):
        simple_report = SimpleReport.generate(inventory_list)
        company_counts = dict()
        for item in inventory_list:
            company_name = item["nome_da_empresa"]
            if company_name in company_counts:
                company_counts[company_name] += 1
            else:
                company_counts[company_name] = 1
        company_stock = ""
        for company, count in company_counts.items():
            company_stock += f"- {company}: {count}\n"
        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{company_stock}\n"
        )
