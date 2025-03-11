# 🚀 Intelligent SQL Agent

## 📌 Project Overview
This project implements an **Intelligent SQL Agent** that receives natural language (**NLP**) queries, automatically converts them into **SQL queries**, and executes them in a **PostgreSQL** database. The system interprets complex queries, supports **JOINs**, aggregations, and ensures query security against **SQL Injection**.

## 🛠 Project Requirements
- Set up a **PostgreSQL** database with relational tables.
- Implement an **SQL Agent** using **LangChain** to convert **NLP** into **SQL**.
- Create a **LangGraph** flow to process queries.
- Execute generated SQL queries and return formatted results.
- Ensure **query security** and performance optimization.

## 📂 Project Structure
```
sql-agent/
│── config/
│   ├── config.yaml                    # Configuration file for database & LangChain
│── data/
│   ├── init_db.sql                    # PostgreSQL database initialization script
│── migrations/
│   ├── env.py                         # PostgreSQL database apply database migrations and seed initial data
│── src/
│   ├── __init__.py
│   ├── database.py                    # Database connection with PostgreSQL
│   ├── models.py                      # Database models with table's mirror 
│   ├── nlp_to_sql.py                  # NLP to SQL conversion using LangChain
│   ├── query_validator.py             # SQL query validation to prevent SQL Injection
│   ├── response_formatter.py          # Formatting SQL results
│   ├── seed.py                        # Populare data in PostgreSQL tables 
│   ├── sql_agent.py                   # Execution flow of the agent using LangGraph
│── tests/
│   ├── test_nlp_to_sql.py             # Unit tests for NLP to SQL conversion
│   ├── test_database.py               # Database connection and query execution tests
│── .env                               # Environment variables alembic.ini
│── .gitignore                         # Folders and files ignored by Github
│── alembic.ini                        # Variables Alembic Project dependencies
│── docker-compose.yml                 # Container orchestration with PostgreSQL
│── Dockerfile                         # Dockerfile for deployment
│── main.py                            # Project entry point
│── requirements.txt                   # Project dependencies
│── README.md                          # Project documentation
```

## 📂 Database Schema
The database consists of three interrelated tables:
- **clients**: Stores customer information.
- **transactions**: Records purchases made by each client.
- **products**: Contains available products.

### 🔗 Table Relationships
- A client can have multiple transactions (**1-to-N**).
- Each transaction is linked to one product (**N-to-1**).

## ✅ Expected Queries
The SQL Agent should be able to handle queries such as:
- **Which clients bought a laptop?**
- **How much has each client spent in total?**
- **Who has enough balance to buy a smartphone?**

## 🚀 Execution Flow
1. The user submits a **natural language query**.
2. **LangChain** processes and converts it into an **SQL query**.
3. The query is **validated** and executed in **PostgreSQL**.
4. The results are **formatted** and returned to the user.

## 📌 Technologies Used
- **Python** (FastAPI, SQLAlchemy, psycopg2, LangChain)
- **PostgreSQL** (Database backend)
- **LangChain** (NLP → SQL conversion)
- **Docker** (Containerized deployment)
- **pytest** (Automated testing)
- **MLOps Deployment** (CI/CD with Docker & cloud services)

## 🔧 Setup Guide
### **1️⃣ Clone the Repository**
```sh
git clone <repository_url>
cd sql_agent_project
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Configure Environment Variables**
Create a **`.env`** file and configure it as follows:
```ini
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```

### **4️⃣ Initialize the Database**
Run the following command to set up PostgreSQL:
```sh
docker-compose up -d  # Starts PostgreSQL in a Docker container
```
Then, apply migrations using **Alembic**:
```sh
alembic upgrade head
```

### **5️⃣ Start the FastAPI Server**
```sh
uvicorn main:app --reload
```

### **6️⃣ Access API Documentation**
Go to: [Swagger UI](http://127.0.0.1:8000/docs)

## 📌 Running Tests
To run unit tests:
```sh
pytest tests/
```

## 🚀 Deploying to MLOps Pipeline

### **1️⃣ Containerize the Application with Docker**
#### **Create the Docker Image**
```sh
docker build -t sql-agent-app .
```

#### **Run the Application in a Container**
```sh
docker run -d -p 8000:8000 --env-file .env sql-agent-app
```

### **2️⃣ Deploy to Cloud (AWS/GCP/Azure)**
#### **Deploy with Kubernetes**
- Create a Kubernetes deployment YAML file:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sql-agent-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: sql-agent
  template:
    metadata:
      labels:
        app: sql-agent
    spec:
      containers:
      - name: sql-agent
        image: sql-agent-app:latest
        ports:
        - containerPort: 8000
```
- Apply deployment:
```sh
kubectl apply -f deployment.yaml
```

### **3️⃣ Continuous Integration & Continuous Deployment (CI/CD)**
#### **GitHub Actions Workflow Example**
Create `.github/workflows/deploy.yml`:
```yaml
name: Deploy SQL Agent

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v2
      - name: Build Docker Image
        run: docker build -t sql-agent-app .
      - name: Push to Docker Hub
        run: docker push <your-dockerhub-username>/sql-agent-app
      - name: Deploy to Kubernetes
        run: kubectl apply -f deployment.yaml
```

## 📌 Features
✔ Converts natural language queries to SQL using LangChain.
✔ Executes SQL queries securely in PostgreSQL.
✔ Uses LangGraph for query processing.
✔ Supports containerized deployment with Docker & Kubernetes.
✔ Integrates with MLOps CI/CD pipelines.

## 📌 Example Queries
- **"Which clients bought a laptop?"**
- **"How much has each client spent in total?"**
- **"Who has enough balance to buy a smartphone?"**

## 📜 License
My Test Kleber Santos.

🚀 **Ready to deploy an intelligent SQL Agent? Let’s go!**
