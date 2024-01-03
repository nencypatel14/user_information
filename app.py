from fastapi import FastAPI

from src.route.router import router

app = FastAPI(title="User Information")

app.include_router(router)

@app.get("/")
async def index():
    return "User Information"
