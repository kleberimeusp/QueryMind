import pytest
from src.nlp_to_sql import convert_nlp_to_sql

@pytest.mark.parametrize(
    "nlp_query, expected_sql",
    [
        ("Which clients bought a Notebook?", "SELECT DISTINCT c.name, c.email FROM clients c JOIN transactions t ON c.id = t.client_id JOIN products p ON t.product_id = p.id WHERE p.name ILIKE '%Notebook%';"),
        ("How much has each client spent in total?", "SELECT c.name, SUM(t.amount) AS total_spent FROM clients c JOIN transactions t ON c.id = t.client_id GROUP BY c.name ORDER BY total_spent DESC;"),
        ("Who has enough balance to buy a Smartphone?", "SELECT c.name, c.balance FROM clients c JOIN products p ON p.name ILIKE '%Smartphone%' WHERE c.balance >= p.price;")
    ]
)
def test_nlp_to_sql(nlp_query, expected_sql):
    generated_sql = convert_nlp_to_sql(nlp_query)
    assert generated_sql.strip().lower() == expected_sql.strip().lower()
