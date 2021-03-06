
from setuptools import setup, find_packages
import sys, os

setup(name='myapp',
    version='1.0',
    description="none",
    long_description="none",
    classifiers=[],
    keywords='',
    author='none',
    author_email='none',
    url='none',
    license='none',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        ### Required to build documentation
        # "Sphinx >= 1.0",
        ### Required for testing
        # "nose",
        # "coverage",
        ### Required to function
        'cement',
        ],
    setup_requires=[],
    entry_points="""
        [console_scripts]
        myapp = myapp.cli.main:main
    """,
    namespace_packages=[],
    )
