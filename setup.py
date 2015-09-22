import os
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    long_description = f.read()


setup(
    name='tusclient',
    version='0.2.1',
    description='python client for tus protocol 1.0.0',
    long_description=long_description,
    url='https://github.com/everydo/tusclient',
    author='easydo.cn',
    author_email='info@easydo.cn',
    keywords='tus client',
    license='MIT',

    py_modules=['tusclient'],
    install_requires=['requests'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: MIT License',
    ],
)
