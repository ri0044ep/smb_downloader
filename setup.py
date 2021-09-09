from setuptools import setup
import os

version = '1.0.0'

install_requires = [
    "setuptools",
    "pysmb"
]

setup(
    name="smb_downloader",
    version=version,
    description="Utility class to donwload files from SMB server",
    long_description="README.md",
    long_description_content_type="markdown",
    author="Kota Yoshida",
    author_email="ri0044ep@ed.ritsumei.ac.jp",
    url="",
    license="MIT License",
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
)
