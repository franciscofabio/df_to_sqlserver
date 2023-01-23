from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()


setup(
    name='df_to_sqlserver',
    version='1.0.8',
    license='MIT License',
    author='Francisco Fabio de Almeida Ferreira',
    long_description=page_description,
    long_description_content_type="text/markdown",
    author_email="franciscofabio18@hotmail.com",
    keywords='df to sql',
    description=u"Test version - Dataframe to Script SQL. This project created to Francisco Fabio de A. Ferreira, Systems Analyst, Data Scientist. This package. E-mail:franciscofabio18@hotmail.com.",
    url="https://github.com/franciscofabio/df_to_sqlserver",
    packages=find_packages(),
    install_requires=['requests'],
    python_requires='>=3.8',
)
