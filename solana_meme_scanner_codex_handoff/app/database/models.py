"""SQLAlchemy models for milestone 1 schema."""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import (
    JSON,
    Boolean,
    CheckConstraint,
    DateTime,
    Float,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Base declarative model class."""


class Token(Base):
    __tablename__ = "tokens"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    chain: Mapped[str] = mapped_column(String(32), default="solana", nullable=False)
    mint_address: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    symbol: Mapped[str | None] = mapped_column(String(32))
    name: Mapped[str | None] = mapped_column(String(128))
    description: Mapped[str | None] = mapped_column(Text)
    created_at_detected: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    launch_timestamp_estimated: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), index=True)
    source: Mapped[str | None] = mapped_column(String(64))
    pumpfun_url: Mapped[str | None] = mapped_column(String(512))
    dexscreener_url: Mapped[str | None] = mapped_column(String(512))
    geckoterminal_url: Mapped[str | None] = mapped_column(String(512))
    first_seen_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    metadata_json: Mapped[dict | None] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    pools: Mapped[list[Pool]] = relationship(back_populates="token")

    __table_args__ = (Index("ix_tokens_symbol", "symbol"),)


class Pool(Base):
    __tablename__ = "pools"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    token_id: Mapped[int] = mapped_column(ForeignKey("tokens.id"), nullable=False, index=True)
    pool_address: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    dex: Mapped[str | None] = mapped_column(String(64), index=True)
    quote_token: Mapped[str | None] = mapped_column(String(128))
    base_token: Mapped[str | None] = mapped_column(String(128))
    created_at_detected: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    first_seen_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    liquidity_usd_initial: Mapped[float | None] = mapped_column(Float)
    liquidity_usd_latest: Mapped[float | None] = mapped_column(Float)
    fdv_latest: Mapped[float | None] = mapped_column(Float)
    market_cap_latest: Mapped[float | None] = mapped_column(Float)
    source: Mapped[str | None] = mapped_column(String(64))
    metadata_json: Mapped[dict | None] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    token: Mapped[Token] = relationship(back_populates="pools")


class OhlcvCandle(Base):
    __tablename__ = "ohlcv_candles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    token_id: Mapped[int] = mapped_column(ForeignKey("tokens.id"), nullable=False)
    pool_id: Mapped[int] = mapped_column(ForeignKey("pools.id"), nullable=False)
    timeframe: Mapped[str] = mapped_column(String(16), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    open: Mapped[float] = mapped_column(Float, nullable=False)
    high: Mapped[float] = mapped_column(Float, nullable=False)
    low: Mapped[float] = mapped_column(Float, nullable=False)
    close: Mapped[float] = mapped_column(Float, nullable=False)
    volume: Mapped[float | None] = mapped_column(Float)
    volume_usd: Mapped[float | None] = mapped_column(Float)
    tx_count: Mapped[int | None] = mapped_column(Integer)
    buy_count: Mapped[int | None] = mapped_column(Integer)
    sell_count: Mapped[int | None] = mapped_column(Integer)
    buy_volume: Mapped[float | None] = mapped_column(Float)
    sell_volume: Mapped[float | None] = mapped_column(Float)
    source: Mapped[str | None] = mapped_column(String(64))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    __table_args__ = (
        UniqueConstraint("token_id", "timeframe", "timestamp", name="uq_ohlcv_token_tf_ts"),
        UniqueConstraint("pool_id", "timeframe", "timestamp", name="uq_ohlcv_pool_tf_ts"),
    )


class LaunchMetric(Base):
    __tablename__ = "launch_metrics"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    token_id: Mapped[int] = mapped_column(ForeignKey("tokens.id"), unique=True, nullable=False)
    pool_id: Mapped[int | None] = mapped_column(ForeignKey("pools.id"))
    timeframe: Mapped[str | None] = mapped_column(String(16))
    launch_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    first_trade_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    first_ath_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), index=True)
    first_ath_price: Mapped[float | None] = mapped_column(Float)
    first_ath_market_cap: Mapped[float | None] = mapped_column(Float)
    first_ath_volume_window: Mapped[float | None] = mapped_column(Float)
    time_to_first_ath_minutes: Mapped[float | None] = mapped_column(Float)
    pump_return_from_launch: Mapped[float | None] = mapped_column(Float)
    max_slope_pre_ath: Mapped[float | None] = mapped_column(Float)
    green_candle_ratio_pre_ath: Mapped[float | None] = mapped_column(Float)
    volume_expansion_ratio_pre_ath: Mapped[float | None] = mapped_column(Float)
    first_dump_low_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    first_dump_low_price: Mapped[float | None] = mapped_column(Float)
    retrace_from_ath_pct: Mapped[float | None] = mapped_column(Float, index=True)
    time_from_ath_to_dump_low_minutes: Mapped[float | None] = mapped_column(Float)
    dump_speed_pct_per_min: Mapped[float | None] = mapped_column(Float)
    red_candle_ratio_dump: Mapped[float | None] = mapped_column(Float)
    volume_retention_dump: Mapped[float | None] = mapped_column(Float)
    first_bounce_start_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    first_bounce_high_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    first_bounce_high_price: Mapped[float | None] = mapped_column(Float)
    bounce_from_dump_low_pct: Mapped[float | None] = mapped_column(Float, index=True)
    bounce_reclaim_of_ath_loss_pct: Mapped[float | None] = mapped_column(Float)
    time_to_bounce_minutes: Mapped[float | None] = mapped_column(Float)
    bounce_volume_ratio: Mapped[float | None] = mapped_column(Float)
    second_ath_made_boolean: Mapped[bool | None] = mapped_column(Boolean)
    second_ath_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    second_ath_price: Mapped[float | None] = mapped_column(Float)
    max_price_after_bounce: Mapped[float | None] = mapped_column(Float)
    max_return_after_bounce: Mapped[float | None] = mapped_column(Float)
    died_after_first_dump_boolean: Mapped[bool | None] = mapped_column(Boolean)
    terminal_liquidity_loss_boolean: Mapped[bool | None] = mapped_column(Boolean)
    analysis_status: Mapped[str | None] = mapped_column(String(64))
    analysis_notes: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


class PhaseLabel(Base):
    __tablename__ = "phase_labels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    token_id: Mapped[int] = mapped_column(ForeignKey("tokens.id"), nullable=False)
    pool_id: Mapped[int | None] = mapped_column(ForeignKey("pools.id"))
    timeframe: Mapped[str | None] = mapped_column(String(16))
    phase_name: Mapped[str] = mapped_column(String(32), nullable=False)
    start_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    end_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    start_price: Mapped[float | None] = mapped_column(Float)
    end_price: Mapped[float | None] = mapped_column(Float)
    high_price: Mapped[float | None] = mapped_column(Float)
    low_price: Mapped[float | None] = mapped_column(Float)
    volume_sum: Mapped[float | None] = mapped_column(Float)
    confidence_score: Mapped[float | None] = mapped_column(Float)
    method_version: Mapped[str | None] = mapped_column(String(32))
    metadata_json: Mapped[dict | None] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    __table_args__ = (
        CheckConstraint(
            "phase_name IN ('launch','first_pump','first_ath','first_dump','dead_cat_bounce','post_bounce_dump','second_leg','accumulation','death','unknown')",
            name="ck_phase_labels_phase_name",
        ),
    )


class BacktestResult(Base):
    __tablename__ = "backtest_results"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    token_id: Mapped[int] = mapped_column(ForeignKey("tokens.id"), nullable=False, index=True)
    strategy_name: Mapped[str] = mapped_column(String(64), nullable=False)
    strategy_version: Mapped[str] = mapped_column(String(32), nullable=False)
    candidate_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    entry_price: Mapped[float | None] = mapped_column(Float)
    entry_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    exit_price: Mapped[float | None] = mapped_column(Float)
    exit_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    stop_price: Mapped[float | None] = mapped_column(Float)
    take_profit_price: Mapped[float | None] = mapped_column(Float)
    max_favorable_excursion_pct: Mapped[float | None] = mapped_column(Float)
    max_adverse_excursion_pct: Mapped[float | None] = mapped_column(Float)
    result_pct: Mapped[float | None] = mapped_column(Float)
    win_boolean: Mapped[bool | None] = mapped_column(Boolean)
    reason_entered: Mapped[str | None] = mapped_column(Text)
    reason_exited: Mapped[str | None] = mapped_column(Text)
    metadata_json: Mapped[dict | None] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    __table_args__ = (Index("ix_backtest_strategy_name_version", "strategy_name", "strategy_version"),)


class HolderSnapshot(Base):
    __tablename__ = "holder_snapshots"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    token_id: Mapped[int] = mapped_column(ForeignKey("tokens.id"), nullable=False)
    snapshot_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    holder_count: Mapped[int | None] = mapped_column(Integer)
    top_10_supply_pct: Mapped[float | None] = mapped_column(Float)
    top_20_supply_pct: Mapped[float | None] = mapped_column(Float)
    top_50_supply_pct: Mapped[float | None] = mapped_column(Float)
    dev_supply_pct: Mapped[float | None] = mapped_column(Float)
    bundle_supply_pct: Mapped[float | None] = mapped_column(Float)
    sniper_supply_pct: Mapped[float | None] = mapped_column(Float)
    insider_supply_pct: Mapped[float | None] = mapped_column(Float)
    source: Mapped[str | None] = mapped_column(String(64))
    raw_json: Mapped[dict | None] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    __table_args__ = (Index("ix_holder_snapshots_token_snapshot", "token_id", "snapshot_time"),)


class WalletEvent(Base):
    __tablename__ = "wallet_events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    token_id: Mapped[int] = mapped_column(ForeignKey("tokens.id"), nullable=False)
    wallet_address: Mapped[str] = mapped_column(String(128), nullable=False)
    event_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    event_type: Mapped[str | None] = mapped_column(String(64))
    amount_token: Mapped[float | None] = mapped_column(Float)
    amount_sol: Mapped[float | None] = mapped_column(Float)
    amount_usd: Mapped[float | None] = mapped_column(Float)
    supply_pct: Mapped[float | None] = mapped_column(Float)
    is_dev: Mapped[bool | None] = mapped_column(Boolean)
    is_sniper: Mapped[bool | None] = mapped_column(Boolean)
    is_bundle: Mapped[bool | None] = mapped_column(Boolean)
    is_top_holder: Mapped[bool | None] = mapped_column(Boolean)
    source: Mapped[str | None] = mapped_column(String(64))
    tx_signature: Mapped[str | None] = mapped_column(String(128), unique=True)
    raw_json: Mapped[dict | None] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    __table_args__ = (
        Index("ix_wallet_events_token_wallet", "token_id", "wallet_address"),
        Index("ix_wallet_events_token_event_time", "token_id", "event_time"),
    )
