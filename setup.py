from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='hr',
    version='1.0.0',
    description='Command line user export utility',
    long_description=readme,
    author='Rolando Sotelo',
    author_email='rola@hey.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)