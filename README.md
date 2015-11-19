Rails - Python web framework
===

**Python on Rails** is a web framework with an idea to simplify web development. It's not a clone of **Ruby on Rails**. This project created for write less code, and this code should be good structured in small and big projects.


Quick start
---

- create new [virtual env](https://bitbucket.org/dhellmann/virtualenvwrapper) for test project: `mkvirtualenv test_project`
- install Rails with [pip](https://pypi.python.org/pypi/Rails): `pip install Rails`
- clone our [test project](https://github.com/PythonRails/examples): `git clone git@github.com:PythonRails/examples.git`
- open a test project and run it: `cd examples && python blog/app.py`
- check how it works, open: [127.0.0.1:8800](http://127.0.0.1:8800)

Continue to read [documentation](docs) to get started.


Project features
---

- [x] **Flat project structure**. When you need to create new controller or model - just do it. No worry about *"In which file do I need to place this code?"*. All models place in `models` folder and all controllers create in `controllers` folder.
- [x] **No routers**. With routers we can overlap some urls and have problems with accessing desired url. In our case we have simple mapping between url address and controller name and action. Access to `/users/details/15` calls a controller `Users` and an action `details()` with argument `15`. The main project controller is `Index` and can be used to render homepage with action `index()`.
- [ ] **Less coupling**. You can choose any **Model backend** *(like [SQL Alchemy](http://www.sqlalchemy.org), [SQLObject](http://www.sqlobject.org), [PonyORM](https://ponyorm.com))* and any **View backend** *([Jinja2](http://jinja.pocoo.org), [Mako](http://www.makotemplates.org), [Chameleon](http://chameleon.readthedocs.org/en/latest/))*. It configurable in the project settings file.
- [ ] **Middlewares**. When we need to do something before and after a call to a desired controller - we use middleware.
- [ ] **Auth out of the box**. Focus on coding a new logic. You have out-of-the-box ability to login via external websites *(facebook, twitter)* in one click as well as via email + password.
- [ ] *[and something else](docs/chapters/features.md)*


Development
---

**Have an idea?** [Create Pull Request](https://github.com/PythonRails/rails/pulls) or [Create New Issue](https://github.com/PythonRails/rails/issues).

Like us on [facebook](https://www.facebook.com/PythonRails).
