from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, Session
import datetime

# Database setup (SQLite for Phase 1)
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class CalculationLog(Base):
    __tablename__ = "calculations"
    id = Column(Integer, primary_key=True, index=True)
    expression = Column(String, index=True)
    result = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Will restrict this via environment variables in the K8s phase
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/calculate/")
def calculate(expression: str, db: Session = Depends(get_db)):
    try:
        # Basic eval for demonstration; in a real app, use a safe math parser
        result = float(eval(expression)) 
        
        log = CalculationLog(expression=expression, result=result)
        db.add(log)
        db.commit()
        db.refresh(log)
        
        return {"expression": expression, "result": result, "id": log.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid mathematical expression")

@app.get("/history/")
def get_history(limit: int = 10, db: Session = Depends(get_db)):
    return db.query(CalculationLog).order_by(CalculationLog.timestamp.desc()).limit(limit).all()