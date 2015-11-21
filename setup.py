"""
Rails
====================

**Python on Rails** is a web framework with an idea to simplify web development.
It's not a clone of **Ruby on Rails**. This project created for for less code,
and this code should be good structured in small and big projects.


Quick start
-------------

Read `Quick Start <https://github.com/pythonrails/rails>`_ on GitHub.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


version = '0.0.5'


setup(
    name='Rails',
    version=version,
    url='https://github.com/pythonrails/rails',
    license='MIT',
    author='Anton Danilchenko',
    author_email='anton@danilchenko.me',
    description='Rails - python web framework',
    keywords='rails web framework development',
    long_description=__doc__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=['rails', 'rails.controllers', 'rails.models', 'rails.views'],
    install_requires=['webob'],
    include_package_data=True,
    zip_safe=False,
    platforms='any'
)
