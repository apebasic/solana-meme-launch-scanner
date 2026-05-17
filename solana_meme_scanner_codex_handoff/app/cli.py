"""Typer CLI entrypoint for the scanner."""

from __future__ import annotations

import typer
from sqlalchemy import inspect

from app.config import get_settings
from app.database.session import create_all_tables, get_engine

app = typer.Typer(help="Solana meme launch scanner CLI.")
db_app = typer.Typer(help="Database utilities.")
app.add_typer(db_app, name="db")


@db_app.command("init")
def db_init() -> None:
    """Create all database tables from SQLAlchemy metadata."""
    create_all_tables()
    typer.echo("Database tables created.")


@db_app.command("status")
def db_status() -> None:
    """Show configured DB URL and current table list."""
    settings = get_settings()
    engine = get_engine()
    table_names = inspect(engine).get_table_names()

    typer.echo(f"DATABASE_URL={settings.database_url}")
    typer.echo(f"tables={','.join(table_names) if table_names else '(none)'}")


if __name__ == "__main__":
    app()
