# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ""
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, "README.rst")
if os.path.exists(readme_path):
    with open(readme_path, "rb") as stream:
        readme = stream.read().decode("utf8")


setup(
    long_description=readme,
    name="netbox-routeros",
    version="0.1.0",
    description="Configure Mikrotik RouterOS devices using Netbox",
    python_requires="==3.*,>=3.8.0",
    project_urls={"repository": "https://github.com/gardunha/netbox-routeros"},
    author="Adam Charnock",
    author_email="adam.charnock@gardunha.net",
    license="MIT",
    packages=[
        "netbox_routeros",
        "netbox_routeros.migrations",
        "netbox_routeros.tests",
        "netbox_routeros.utilities",
    ],
    package_dir={"": "."},
    package_data={
        "netbox_routeros": [
            "static/netbox_routeros/*.css",
            "templates/routeros/*.html",
            "templates/routeros/bases/*.html",
        ]
    },
    install_requires=["jinja2==2.*,>=2.11.3"],
)
