from fastapi import APIRouter, HTTPException, Path, Query
from fastapi_sqlalchemy import db
from typing import Optional
from sqlalchemy import text, and_

class DataNotFoundError(Exception):
    pass