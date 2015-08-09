# Python on Rails

Why not to create Python on Rails? Why Ruby on Rails can do something that isn't possible on Python? We can do the web framework that will be better and easier to build first-class websites.


Our goals
---

- [x] **Simplify project structure** compared to Django. Sometimes we don't know in what app we need to create new ORM model. With flat project structure we can create model in one `models` folder and save the time. The same for project controllers.
- [x] **No routers**. With routers we can overlap some urls and have problems with accessing desired url. In our case we have simple mapping between url address and controller name. Access to `/users/details/15` will call controller `controllers.users.Users.details()` with argument `15`. The default controller name is `Index` and can be used to render homepage in this way `controlers.index.Index.index()`.
- [ ] **Templates in python style**. It will be good to create templates without closing tags in hierarchical structure, like we do in Python code or in YAML.
- [ ] **Middleware as expected**. When we need to do something before and after call the desired controller - we use middleware.
- [ ] **Auth out of the box**. Don't lose your time. Create new project and focus on project logic. You can login via external websites (facebook, twitter) in one click as well as via email.
- [ ] ... and something else

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

