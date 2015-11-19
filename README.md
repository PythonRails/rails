Rails - Python web framework
===

**Rails on Python** is a web framework with an idea to simplify web development. It's not a clone of **Ruby on Rails**. This project created for write less code, and this code should be good structured in small and big projects.


Quick start
---

- create new [virtual env](https://bitbucket.org/dhellmann/virtualenvwrapper) for test project: `mkvirtualenv test_project`
- install Rails with [pip](https://pypi.python.org/pypi/Rails): `pip install Rails`
- clone our [test project](https://github.com/PythonRails/examples): `git clone git@github.com:PythonRails/examples.git`
- open a test project and run it: `cd examples && python blog/app.py`
- check how it works, open: [127.0.0.1:8800](http://127.0.0.1:8800)



Project features
---

- [x] **Simple project structure**. When you need to create new controller or model - just do it. No worry about "in what app I need to place this code" *(if we talk about Django)*. All project models place in `models` folder and all controllers create in `controllers` folder.
- [x] **No routers**. With routers we can overlap some urls and have problems with accessing desired url. In our case we have simple mapping between url address and controller name and action. Access to `/users/details/15` calls a controller `Users` and an action `details()` with argument `15`. The main project controller is `Index` and can be used to render homepage with action `index()`.
- [x] **Less magic**. All work as expected without overcomplecated magic. We use magic only when it is natural and easy to understand.
- [ ] **Middlewares**. When we need to do something before and after call the desired controller - we use middleware.
- [ ] **Templates in python style**. It will be good to create templates without closing tags in hierarchical structure, like we do in Python code or in YAML.
- [ ] **Auth out of the box**. Focus on coding new logic. You have out-of-the-box ability to login via external websites *(facebook, twitter)* in one click as well as via email + password.
- [ ] *[and something else](docs/chapters/features.md)*


Development
---

**Have an idea?** [Create Pull Request](https://github.com/PythonRails/pythonrails/pulls) or [Create New Issue](https://github.com/PythonRails/pythonrails/issues). Also join to us on [facebook](https://www.facebook.com/PythonRails),


Documentation
---

Read [full documentation](docs) to get started.
