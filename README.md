# Get Started

Dependencies:
* [cookiecutter](https://github.com/audreyr/cookiecutter)

Steps:
* Clone or download this repository then:

```bash
$ bash marcs-django-rest-cookie-cutter/setup.sh
```
* And you're off!

# Features


#### Create a Rest App
```bash
$ ./manage.py startrestapp <app_name>
```
###### Creates django app with following app structure
#
```
app_name
│   factories
│   migrations    
└───v1
│   │   urls.py
│   │   serializers.py
│   │   views.py
│   admin.py
│   apps.py
│   models.py
```

