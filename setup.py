"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""
from setuptools import setup

APP = ['automatic_class_registration.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['selenium']
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)