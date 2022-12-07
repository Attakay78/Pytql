from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Python Table Data Type with some SQL-like operations.'

# Setting up
setup(
    name="pytql",
    version=VERSION,
    author="AT_Khay (Richard Quaicoe)",
    author_email="<richardquaicoe78@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    setup_requires=['wheel'],
    keywords=['python', 'table', 'sql', 'query', 'filter'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)