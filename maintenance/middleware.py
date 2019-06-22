from django.conf import settings
from django.shortcuts import redirect
from django.urls import resolve

"""
List url that won't be redirected to maintenance page
You can add other URL in settings.py
ex.
EXCLUDE_URLS = ['login', 'accounts:login']
"""
EXCLUDE_URLS = ["admin:login", "admin:index", "maintenance:maintenance"]

class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        """
        check and get attribute from settings.py
        """
        self.url_maintenance = getattr(settings, "URL_MAINTENANCE", "maintenance:maintenance")
        self.maintenance = getattr(settings, 'MAINTENANCE', False)

        if hasattr(settings, 'EXCLUDE_URLS'):
            self.exclude_urls = EXCLUDE_URLS + settings.EXCLUDE_URLS
        else:
            self.exclude_urls = EXCLUDE_URLS

        if hasattr(settings, 'URL_MAINTENANCE'):
            self.exclude_urls.append(settings.URL_MAINTENANCE)

    def __call__(self, request):
        """
        check the exclude urls doesn't redirect to the maintenance page
        """
        path_info = resolve(request.path_info)

        """
        redirect to home if MAINTENANCE False and app name
        and namespace is 'maintenance
        """
        if not self.maintenance and 'maintenance' in path_info.app_names \
                and 'maintenance' in path_info.namespaces:
            return redirect("/")

        """
        return self.get_response if match app name and namescape
        """
        for url in self.exclude_urls:
            exclude_url = self._get_path_info(url)

            if exclude_url['app_name'] in path_info.app_names \
                    and path_info.url_name == exclude_url['url_name']:
                return self.get_response(request)
            elif not exclude_url['app_name'] and not path_info.app_names \
                    and path_info.url_name == exclude_url['url_name']:
                return self.get_response(request)

        """
        redirect to maintenance page if MAINTENANCE True and user not authenticated
        """
        if self.maintenance and not request.user.is_authenticated:
            return redirect(self.url_maintenance)
        else:
            return self.get_response(request)

    def _get_path_info(self, url):
        """
        to parse app_name and url_name and return to dict
        """
        url_info = url.split(":")
        if len(url_info) > 1:
            return {'app_name': url_info[0], 'url_name': url_info[1]}
        else:
            return {'app_name': '', 'url_name': url_info[0]}
