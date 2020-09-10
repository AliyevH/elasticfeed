from setuptools import setup, find_packages

setup(
    name="elasticfeed",
    version="1.0.2",
    include_package_data=True,
    packages=find_packages(),
    author="Hasan Aliyev",
    author_email="hasan.aliyev.555@gmail.com",
    description="Export csv data into Elasticsearch",
    license="MIT",
    url="https://github.com/AliyevH/elk_feeder",
    install_requires=["click", "elasticsearch"],
    entry_points = {
        'console_scripts': ['feeder=elastic_feeder.scripts.commands:command'],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)