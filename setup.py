from setuptools import setup, find_packages

# User defines the location of the script output, and which method is being used.

#Version of the test suite used
__version__ = 0.1

setup(
    name = 'cask',
    version = __version__,
    description = 'Planewave DFT code',
    author = 'Nick Woods',
    author_email = 'nw361@cam.ac.uk',
    url = "http://www.tcm.phy.cam.ac.uk/profiles/nw361/",
    packages = find_packages(),
    entry_points={ 'console_scripts': 'cask = cask.cli.main:main' },
)