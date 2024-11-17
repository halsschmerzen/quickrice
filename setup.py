from setuptools import setup, find_packages
import pathlib


HERE = pathlib.Path(__file__).parent


long_description = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="quickrice",  
    version="1.0.2",  
    description="A simple CLI tool to manage your desktop themes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/halsschmerzen/quickrice",  
    author="halsschmerzen",  
    author_email="bastiansteampl@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "quickrice=quickrice.main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)