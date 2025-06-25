#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
from setuptools import setup, find_packages

# 讀取 README 作為 long_description
with io.open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="privai",  # 發行套件名稱
    version="v0.0.2",  # 建議改回符合 PEP440 的版本格式，如 0.1.0
    description="A client library for accessing lance-api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="APMIC, Simon Liu",  # 填入作者或維護者
    url="",     # 填入專案首頁或原始碼倉庫
    packages=find_packages(include=["privai", "privai.*"]),
    include_package_data=True,
    package_data={
        "privai": ["py.typed"],
    },
    install_requires=[
        "httpx>=0.23.0,<0.29.0",
        "attrs>=22.2.0",
        "python-dateutil>=2.8.0",
    ],
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    project_urls={
        "Changelog": "CHANGELOG.md",
    },
)
