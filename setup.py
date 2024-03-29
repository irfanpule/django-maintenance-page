import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-maintenance-page',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Simple create maintenance page and block access url then redirect to maintenance page.',
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/irfanpule/django-maintenance-page",
    author='irfanpule',
    author_email='irfan.pule2@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.x',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
