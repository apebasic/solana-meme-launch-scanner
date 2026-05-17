from __future__ import annotations

from pathlib import Path

from sqlalchemy import inspect

from app.database.models import Base
from app.database.session import create_all_tables, get_engine


EXPECTED_TABLES = {
    "tokens",
    "pools",
    "ohlcv_candles",
    "launch_metrics",
    "phase_labels",
    "backtest_results",
    "holder_snapshots",
    "wallet_events",
}


def test_create_all_tables(tmp_path: Path) -> None:
    db_path = tmp_path / "test.db"
    database_url = f"sqlite:///{db_path}"

    create_all_tables(database_url=database_url)

    inspector = inspect(get_engine(database_url=database_url))
    assert EXPECTED_TABLES.issubset(set(inspector.get_table_names()))


def test_ohlcv_unique_constraints_present(tmp_path: Path) -> None:
    db_path = tmp_path / "constraints.db"
    database_url = f"sqlite:///{db_path}"
    engine = get_engine(database_url=database_url)
    Base.metadata.create_all(engine)

    uniques = inspect(engine).get_unique_constraints("ohlcv_candles")
    unique_names = {item["name"] for item in uniques}

    assert "uq_ohlcv_token_tf_ts" in unique_names
    assert "uq_ohlcv_pool_tf_ts" in unique_names
