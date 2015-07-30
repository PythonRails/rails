# Python on Rails

Why not to create Python on Rails? Why Ruby on Rails can do something that isn't possible on Python? We can do the web framework that will be better and easier to build first-class websites.

Some ideas
---

- [ ] **Simplify project structure** compared to Django. Somwtimes we don;t know in what app we need to create new model. With flat project structure we can create model in one `models` folder and save the time.
- [ ] **Templates in python style**. It will be good to create templates without closing tags in hierarchical structure, like we do in Python code or in YAML.
- [ ] **No routers**. With routers we can overlap some urls and have problems with accessing desired url. In our case we have simple mapping between url address and controller name. Access to `/users/details/15` will call controller `controllers.users.Details` with argument `15`. The default controller names `Index` and can be used to render homepage in this way `controlers.index.Index`.
- [ ] **Middleware as expected**. When we need to do something before and after call the desired controller - we use middleware.
- [ ] **Auth out of the box**. Don't lose your time. Create new project and focus on new project logic. You can login via external websites (facebook, twitter) in one click as well as registration via email.
- [ ] ... and something else

**Have an idea?** Create Pull Request or Create New Issue.
