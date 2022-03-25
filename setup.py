from setuptools import setup, find_packages
import os
 
VERSION = '0.0.1'
DESCRIPTION = 'A python Serials system for licensing your programs'

# Setting up
setup(
    name="serialspkg",
    version=VERSION,
    author="DbomDev (Dbom Dev)",
    author_email="<dbomdev2020@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['random', 'pyautogui', 'pyaudio'],
    keywords=['python', 'serials', 'generator', 'key gen'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
