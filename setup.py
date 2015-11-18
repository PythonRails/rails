"""
Rails - a python web framework
====================

This project designed for web developers who want to do more for less time.
Create new project in few minutes.
User registration and authentication system ready to use.


Quick start
-------------

Clone and run example application. Don't forget to switch to your project's virtualenv.

.. code:: shell

   git clone git@github.com:pythonrails/examples.git
   cd examples/
   pip install -r requirements.txt
   # run server on 127.0.0.1:8000
   python app.py


Development
-------------

You can install development version by clone `git repository <https://github.com/pythonrails/pythonrails>`_::

    git clone git@github.com:pythonrails/pythonrails.git


Links
-------

* `project website <https://github.com/pythonrails/pythonrails>`_
* `documentation <https://github.com/pythonrails/docs>`_
* `sample applications <https://github.com/pythonrails/examples>`_
* `follow us on facebook <https://www.facebook.com/pythonrails>`_

"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


version = '0.0.1'


setup(
    name='Rails',
    version=version,
    url='https://github.com/pythonrails/pythonrails',
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
