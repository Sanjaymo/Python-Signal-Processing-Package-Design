# File: setup.py
"""
Setup configuration for signal_ICT_abhinaychoudhari_92400133174 package

This file configures the package for distribution on PyPI/TestPyPI
Author: Abhinay Choudhari
Contact: 92400133174
"""

from setuptools import setup, find_packages

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="signal-ICT-abhinaychoudhari-92400133174",
    version="1.0.0",
    author="Abhinay Choudhari",
    author_email="abhinaychoudhari@example.com",  # Replace with your actual email
    description="A comprehensive signal processing package for generating and manipulating signals",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abhinaychoudhari/signal_ICT_abhinaychoudhari_92400133174",  # Replace with your GitHub URL
    project_urls={
        "Bug Tracker": "https://github.com/abhinaychoudhari/signal_ICT_abhinaychoudhari_92400133174/issues",
        "Documentation": "https://github.com/abhinaychoudhari/signal_ICT_abhinaychoudhari_92400133174#readme",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.19.0",
        "matplotlib>=3.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black",
            "flake8",
        ],
        "docs": [
            "sphinx",
            "sphinx-rtd-theme",
        ],
    },
    entry_points={
        "console_scripts": [
            "signal-demo=signal_ICT_abhinaychoudhari_92400133174.main:main",
        ],
    },
    keywords="signal processing, digital signal processing, signals and systems, ICT, engineering",
    include_package_data=True,
    zip_safe=False,
)