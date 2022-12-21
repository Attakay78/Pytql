from setuptools import setup, find_packages

VERSION = "0.0.3"
DESCRIPTION = "Python Table Data Type with some SQL-like operations."

# Setting up
setup(
    name="pytql",
    version=VERSION,
    author="AT_Khay (Richard Quaicoe)",
    author_email="<richardquaicoe78@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open("README.md", "r").read(),
    packages=find_packages(),
    install_requires=[],
    url="https://github.com/Attakay78/Pytql",
    setup_requires=["wheel"],
    keywords=["python", "table", "sql", "query", "filter"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
