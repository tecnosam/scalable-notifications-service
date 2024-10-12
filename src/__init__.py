from fastapi import FastAPI 
from src.handlers.http import router


app = FastAPI()

app.include_router(router)

