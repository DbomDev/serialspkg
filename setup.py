from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A python serials system'
LONG_DESCRIPTION = 'A package that allows you to generate fast random Serials.'

setup(
    name="serialspkg",
    version=VERSION,
    author="DbomDev (Dbom Dev)",
    author_email="<dbomdev2020@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['random', 'time', 'json', 'pathlib'],
    keywords=['python', 'serials', 'generator', 'key gen', 'licensing'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)