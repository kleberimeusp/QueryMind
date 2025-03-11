from sqlalchemy.orm import Session
from sqlalchemy import text

class SQLAgent:
    def __init__(self, db: Session):
        self.db = db

    def process_query(self, question: str):
        """Simula um agente que transforma linguagem natural em SQL."""
        # Mapeamento fixo de perguntas para SQL
        query_map = {
            "Which clients bought a Notebook?": 
                "SELECT DISTINCT c.name FROM clients c "
                "JOIN transactions t ON c.id = t.client_id "
                "JOIN products p ON t.product_id = p.id WHERE p.name = 'Notebook';",
            
            "How much has each client spent in total?": 
                "SELECT c.name, SUM(t.total_price) AS total_spent FROM clients c "
                "JOIN transactions t ON c.id = t.client_id GROUP BY c.id;",

            "Who has enough balance to buy a Smartphone?": 
                "SELECT c.name FROM clients c "
                "WHERE c.balance >= (SELECT price FROM products WHERE name = 'Smartphone');"
        }

        # Obter a query correspondente
        sql_query = query_map.get(question)
        if not sql_query:
            return {"error": "Query not supported"}

        try:
            # Executar a query no banco
            result = self.db.execute(text(sql_query))
            rows = result.fetchall()
            
            # Converter resultado para dicionário (corrigindo erro de conversão)
            return [dict(zip(result.keys(), row)) for row in rows]

        except Exception as e:
            return {"error": f"SQL execution failed: {str(e)}"}
