import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-issuetracking",
    version = __import__('issuetracking').get_version(),
    author = "Philipp Bosch",
    author_email = "hello@pb.io",
    description = "A simple issue tracking app for Django",
    license = "MIT",
    keywords = "django issuetracking issues ticketing bugtracker",
    url = "http://github.com/philippbosch/django-issuetracking/",
    packages=find_packages(),
    package_data={
        'tellafriend': [
            'templates/issuetracking/*.html',
            'templates/issuetracking/*.txt',
            'locale/*/LC_MESSAGES/*',
        ],
    },
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
    ],
)
