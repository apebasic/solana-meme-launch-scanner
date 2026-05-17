from setuptools import find_packages, setup

setup(
    name="solana-meme-launch-scanner",
    version="0.1.0",
    description="Local-first Solana meme launch scanner and backtest database",
    packages=find_packages(exclude=("tests",)),
    python_requires=">=3.11",
    install_requires=[
        "sqlalchemy>=2.0,<3.0",
        "typer>=0.12,<1.0",
        "python-dotenv>=1.0,<2.0",
    ],
    extras_require={"dev": ["pytest>=8.0,<9.0"]},
)
