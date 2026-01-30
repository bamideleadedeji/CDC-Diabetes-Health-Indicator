from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="diabetes-cdc-analysis",
    version="1.0.0",
    author="Your Name",
    author_email="bamideleadedeji2000@gmail.com",
    description="CDC Diabetes Health Indicators Analysis and Risk Assessment Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bamideleadedeji/diabetes-cdc-analysis",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    python_requires=">=3.9",
    install_requires=[
        "pandas>=2.1.0",
        "numpy>=1.24.0",
        "scikit-learn>=1.3.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "plotly>=5.17.0",
        "streamlit>=1.28.0",
        "ucimlrepo>=0.0.3",
        "imbalanced-learn>=0.11.0",
    ],
    extras_require={
        "dev": [
            "black>=23.9.0",
            "flake8>=6.1.0",
            "pytest>=7.4.0",
            "jupyter>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "diabetes-analysis=src.cli:main",
        ],
    },
)
