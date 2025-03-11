from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import create_tables, get_db
from src.sql_agent import SQLAgent
from src.seed import seed_database

app = FastAPI()

@app.post("/query")
def query_database(request: dict, db: Session = Depends(get_db)):
    question = request.get("question")
    if not question:
        raise HTTPException(status_code=400, detail="Missing question")

    sql_agent = SQLAgent(db)
    result = sql_agent.process_query(question)

    return {"status": "success", "data": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



    

