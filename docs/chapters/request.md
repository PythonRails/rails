Request
===


**Request** - is a class that represent user request. It contain query string, request method (get, post, put, delete) and more.


Methods
---

- **get_controller_name()** `-> string`. Return controller name based on query string. If controller isn't given it return 'index'. 

- **get_action_name()** `-> string`. Return action name based on query string. If action name isn't given it return 'index'.

- **get_url_params()** `-> list`. Return all parameters that placed after controller and action name in query string. Return a list of strings.