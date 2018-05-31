# -*- coding: utf-8 -*-

import setuptools
import sys
import os

from aliyun_iot_device import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'paho-mqtt>=1.3.1',
]

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

setuptools.setup(
    name="yansongda-aliyun-iot-device",
    version=__version__,
    author="yansongda",
    author_email="me@yansongda.cn",
    description="aliyun iot device sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={
        '': ['LICENSE', 'NOTICE'],
        'aliyun_iot_device': ['*.cer']
    },
    url="https://github.com/yansongda/aliyun-iot-device-python",
    project_urls={
        'Source': 'https://github.com/yansongda/aliyun-iot-device-python',
        'Tracker': 'https://github.com/yansongda/aliyun-iot-device-python/issues',
    },
    packages=setuptools.find_packages(),
    python_requires=">=3.0, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=requires,
    keywords='yansongda aliyun iot device',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
