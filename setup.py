from setuptools import setup, find_packages

with open("README.md","r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "motor_transmissao" ,
    version = "0.0.1",
    author = "Wilian Oliveira de Jesus",
    author_email = "wilian.galter@gmail.com",
    description = "Modulo para simular um sistema de transmissão mecânica",
    long_description = page_description,
    long_description_content_type = "text/markdown",
    url = "",
    packages = find_packages(),
    install_requires = requirements,
    python_requires = ">=3.8",
    )
