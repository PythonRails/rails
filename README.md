Rails - Python web framework
===

**Rails on Python** is a web framework with an idea to simplify web development. It's not a clone of **Ruby on Rails**. This project created for write less code, and this code should be good structured in small and big projects.


Quick start
---

- create new [virtual env](https://bitbucket.org/dhellmann/virtualenvwrapper) for test project: `mkvirtualenv test_project`
- install Rails with [pip](https://pypi.python.org/pypi/Rails): `pip install Rails`
- clone our test project with `git clone git@github.com:PythonRails/examples.git rails_examples`
- open a test project and run it: `cd rails_examples && python blog/app.py`
- open web browser [127.0.0.1:8800](http://127.0.0.1:8800)



Project features
---

- [x] **Simple project structure**. When you need to create new controller or model - just do it. No worry about "in what app I need to place this code" *(if we talk about Django)*. All project models place in `models` folder and all controllers create in `controllers` folder.
- [x] **No routers**. With routers we can overlap some urls and have problems with accessing desired url. In our case we have simple mapping between url address and controller name and its action. Access to `/users/details/15` will call controller `Users` and its action `details()` with argument `15`. The main project controller is `Index` and can be used to render homepage in with call its action `index()`.
- [x] **Less magic**. All work as expected without overcomplecated magic. We use magic only when it is natural and easy to understand.
- [ ] **Middleware as expected**. When we need to do something before and after call the desired controller - we use middleware.
- [ ] **Templates in python style**. It will be good to create templates without closing tags in hierarchical structure, like we do in Python code or in YAML.
- [ ] **Auth out of the box**. Don't lose your time. Create new project and focus on project logic. You can login via external websites (facebook, twitter) in one click as well as via email.
- [ ] ... [and something else](docs/chapters/features.md)

**Have an idea?** [Create Pull Request](https://github.com/PythonRails/pythonrails/pulls) or [Create New Issue](https://github.com/PythonRails/pythonrails/issues). Also join to us on [facebook](https://www.facebook.com/PythonRails),


Documentation
---

Read [full documentation](docs) to get started.
