from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.db.database import lifespan
from app.api.router import router






app = FastAPI(
    title="Brandmize AI",
    version="1.0.0",
    lifespan=lifespan
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

app.include_router(prefix="/api/v1", router=router)
