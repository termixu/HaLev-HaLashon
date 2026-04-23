from setuptools import setup, find_packages

setup(
    name="halevhalashon",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.30.0",
        "numpy>=1.24.0",
        "flask>=2.3.0",
        "click>=8.1.0",
    ],
    entry_points={
        "console_scripts": [
            "halev=src.cli.main:cli",
        ],
    },
)