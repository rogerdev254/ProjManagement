from setuptools import setup, find_packages

with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name='projectmanagement',
    version="0.0.1",
    author='Roger Brian',
    author_email='rogerbrian.mutua@gmail.com',
    description='a simple project management tool',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/rogerdev254/ProjManagement',
    packages=find_packages(),
    install_requirement=requirements,
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ]
)
