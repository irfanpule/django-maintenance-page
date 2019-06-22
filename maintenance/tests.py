from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User

from .middleware import MaintenanceMiddleware


class TestMiddleware(TestCase):

    def setUp(self):
        self.default_middleware = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]
        self.use_middlware_maintenance = self.default_middleware + ['maintenance.middleware.MaintenanceMiddleware']

    def test_redirect(self):
        # case: MAINTENANCE True, MIDDLEWARE Maintenance installed
        # goal: success access url
        with self.settings(MAINTENANCE=True), \
                self.settings(MIDDLEWARE=self.use_middlware_maintenance):
            response = self.client.get("/")
            self.assertRedirects(response, '/maintenance', status_code=302, target_status_code=200)

    def test_no_redirect_maintenance_true(self):
        # case: MAINTENANCE False, MIDDLEWARE Maintenance installed
        # goal: success access url
        with self.settings(MAINTENANCE=False), \
                self.settings(MIDDLEWARE=self.use_middlware_maintenance):
            response = self.client.get("/")
            self.assertEqual(response.status_code, 200)

    def test_no_redirect_default_middl(self):
        # case: MAINTENANCE True, MIDDLEWARE Maintenance not installed
        # goal: success access url
        with self.settings(MAINTENANCE=True), \
                self.settings(MIDDLEWARE=self.default_middleware):
            response = self.client.get("/")
            self.assertEqual(response.status_code, 200)

    def test_no_redirect_is_authenticated(self):
        # case: MAINTENANCE True, MIDDLEWARE Maintenance installed, user is authenticated
        # goal: success access url
        passwd = 'adminyeyelala123'
        admin = User.objects.create_superuser('admin', 'admin@test.com', passwd)
        self.client.login(username=admin.username, password=passwd)

        with self.settings(MAINTENANCE=True), \
                self.settings(MIDDLEWARE=self.use_middlware_maintenance):
            response = self.client.get("/")
            self.assertEqual(response.status_code, 200)

    def test_no_redirect_default_exclude_url(self):
        # case: MAINTENANCE True, MIDDLEWARE Maintenance installed
        # goal: success access url
        with self.settings(MAINTENANCE=True), \
                self.settings(MIDDLEWARE=self.use_middlware_maintenance):
            response = self.client.get("/admin/")
            self.assertRedirects(response, '/admin/login/?next=/admin/', status_code=302, target_status_code=200)

            response = self.client.get("/admin/login/")
            self.assertEqual(response.status_code, 200)

            response = self.client.get("/maintenance")
            self.assertEqual(response.status_code, 200)

    def test_redirect_home(self):
        # case: MAINTENANCE True, MIDDLEWARE Maintenance installed, access maintenance url
        # goal: redirect to home
        with self.settings(MAINTENANCE=False), \
                self.settings(MIDDLEWARE=self.use_middlware_maintenance):
            response = self.client.get("/maintenance")
            self.assertRedirects(response, '/', status_code=302, target_status_code=200)
