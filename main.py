import os
import uvicorn

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from routes.api import router as api_router

load_dotenv(".env")

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", log_level="info", reload=True)
    print("running")