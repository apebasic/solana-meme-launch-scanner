"""Database engine and session helpers."""

from __future__ import annotations

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from app.config import get_settings
from app.database.models import Base



def get_engine(database_url: str | None = None) -> Engine:
    settings = get_settings()
    db_url = database_url or settings.database_url

    if db_url.startswith("sqlite:///"):
        db_file = Path(db_url.replace("sqlite:///", ""))
        if db_file.parent and str(db_file.parent) != ".":
            db_file.parent.mkdir(parents=True, exist_ok=True)

    return create_engine(db_url, future=True)



def session_factory(database_url: str | None = None) -> sessionmaker:
    engine = get_engine(database_url=database_url)
    return sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)



def create_all_tables(database_url: str | None = None) -> None:
    engine = get_engine(database_url=database_url)
    Base.metadata.create_all(bind=engine)
