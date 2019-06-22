# Django Maintenance Page

Django Maintenance Page is a simple to create maintenance page and block access url then redirect to maintenance page.
You can custom title, description etc or change design maintenance page you wish.

## Quick start
Add 'maintenance' to your INSTALLED_APPS setting like this:
```python
INSTALLED_APPS = [
    ...
    'maintenance',
]
```

Add url maintenance on your project `urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    ...
    path('maintenance', include('maintenance.urls')),
]
```

Add Middleware `maintenance.middleware.MaintenanceMiddleware` in `settings.py`
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...

    'maintenance.middleware.MaintenanceMiddleware'
]
```

Add `MAINTENANCE = True` on your `settings.py` to activate maintenance page
![maintenance page](https://raw.githubusercontent.com/irfanpule/django-maintenance-page/master/screenshot/default-maintenance-page.png)

## Customize page information
You can custom information `title`, `description` and `signature` by adding `MAINTENANCE_TEMPLATE_DATA` in `settings.py`. It's support html writing.
```python
MAINTENANCE_TEMPLATE_DATA = {
    "title": "Kami akan segera kembali",
    "description": "Maaf atas ketidaknyamanan ini tetapi kami sedang melakukan beberapa pemeliharaan saat ini. "
    "Anda dapat menghubungi kami <a href='mailto:'>disini</a>",
    "signature": "Tim Perawatan"
}
```
![customize page](https://raw.githubusercontent.com/irfanpule/django-maintenance-page/master/screenshot/customize-maintenante-page.png)

## Change maintenance page
You can change maintenance page by adding `URL_MAINTENANCE`. Fill in `"app_name:url_name"`
```
URL_MAINTENANCE = "buatin:maintenance"
```

## EXCLUDE URL
By default all urls will be redirected to the maintenance page except:
* `"admin:login"`
* `"admin:index"`
* `"maintenance:maintenance"`


You can add one or more exception urls so that the url is not redirected. Add `EXCLUDE_URLS` in `settings.py`
```python
EXCLUDE_URLS = ["accounts:login", "dashboard:login"]
```
