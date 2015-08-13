Python on Rails
===

Why not to create Python on Rails? Why Ruby on Rails can do something that isn't possible on Python? We can do the web framework that will be better and easier to build first-class websites.


Project features
---

- [x] **Simple project structure**. When you need to create new controller or model - just do it. No worry about "in what app I need to place this code" *(if we talk about Django)*. All project models place in `models` folder and all controllers create in `controllers` folder.
- [x] **No routers**. With routers we can overlap some urls and have problems with accessing desired url. In our case we have simple mapping between url address and controller name and its action. Access to `/users/details/15` will call controller `Users` and its action `details()` with argument `15`. The main project controller is `Index` and can be used to render homepage in with call its action `index()`.
- [x] **Less magic**. All work as expected without overcomplecated magic. We use magic only when it is natural and easy to understand.
- [ ] **Middleware as expected**. When we need to do something before and after call the desired controller - we use middleware.
- [ ] **Templates in python style**. It will be good to create templates without closing tags in hierarchical structure, like we do in Python code or in YAML.
- [ ] **Auth out of the box**. Don't lose your time. Create new project and focus on project logic. You can login via external websites (facebook, twitter) in one click as well as via email.
- [ ] ... [and something else](docs/chapters/features.md)

**Have an idea?** [Create Pull Request](https://github.com/PythonRails/pythonrails/pulls) or [Create New Issue](https://github.com/PythonRails/pythonrails/issues).


Quick start
---

You can find our [test project](test_projects/blog) to find how it organized.

- Clone this project `cd ~/myprojects && git clone git@github.com:PythonRails/pythonrails.git`
- Create virtualenv for the project with virtualenvwrapper: `mkvirtualenv pythonrails`
- `cd ~/.virtualenvs/pythonrails/lib/python2.7/site-packages/`
- `ln -s ~/myprojects/pythonrails/pythonrails` (link to package inside project dir)
- `cd ~/myprojects/pythonrails/test_projects/blog`
- `pip install -r requirements.txt`
- run web server `python app.py`
- open web browser [127.0.0.1:8500](http://127.0.0.1:8500)


Documentation
---

Read [full documentation](docs) to get started.

