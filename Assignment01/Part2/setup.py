from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Topsis-Akshat-102303730",  # Change this to make it unique
    version="1.0.0",
    author="Akshat Kakkar",
    author_email="akakkar_be23@thapar.edu",  # Add your email
    description="A Python package for TOPSIS multi-criteria decision analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akshatkakkar1/-UCS654",  # Your repo URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
    ],
    entry_points={
        'console_scripts': [
            'topsis=Topsis.topsis:main',
        ],
    },
)
