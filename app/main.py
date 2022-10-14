from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import produtos
from app.database.config import criar_bd

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

criar_bd()

app.include_router(produtos.router)