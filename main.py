from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1 import api_router

app = FastAPI(
    title="Mecanizados Vinalopo",
    description="API para la gestión de Mecanizados Vinalopo",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Dominio de tu aplicación Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)