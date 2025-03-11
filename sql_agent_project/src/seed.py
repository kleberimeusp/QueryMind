from src.database import SessionLocal, create_tables
from src.models import Client, Product, Transaction

# Create tables
create_tables()

def seed_database():
    session = SessionLocal()

    # Creating clients
    client1 = Client(name="Alice Johnson", email="alice@example.com", balance=1000)
    client2 = Client(name="Bob Smith", email="bob@example.com", balance=500)

    # Creating products
    product1 = Product(name="Notebook", price=800, stock=5)
    product2 = Product(name="Smartphone", price=600, stock=10)

    session.add_all([client1, client2, product1, product2])
    session.commit()

    # Creating transactions
    transaction1 = Transaction(client_id=client1.id, product_id=product1.id, amount=1, total_price=800)
    transaction2 = Transaction(client_id=client2.id, product_id=product2.id, amount=1, total_price=600)

    session.add_all([transaction1, transaction2])
    session.commit()
    
    session.close()
    print("Database successfully populated!")

if __name__ == "__main__":
    seed_database()
