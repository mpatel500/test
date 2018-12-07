import pytest 
from inventory.models import Webserver, Database, Host
from inventory.views import AllWebservers
import unittest
from django.test import RequestFactory

class TestWebserverModel:

    @pytest.mark.django_db
    def test_webserver_data_is_saved(self):
        webserver =  Webserver.objects.create(name="webserver_1", vendor="Apache", patch_level="Q2-2016",in_use=False)
        assert webserver.name == "webserver_1"
        assert webserver.vendor == "Apache"
        assert webserver.patch_level == "Q2-2016"
        assert webserver.in_use == False 

class TestDatabaseModel:

    @pytest.mark.django_db
    def test_database_data_is_saved(self):
        database = Database.objects.create(name="database_1", vendor="Oracle", patch_level="18.1", in_use=False)
        assert database.name == "database_1"
        assert database.vendor == "Oracle"
        assert database.patch_level == "18.1"
        assert database.in_use == False

class TestHostModel:
    
    @pytest.mark.django_db
    def test_host_data_is_saved(self):
        host = Host.objects.create(fqdn="host0.jpmchase.net", os_type="Redhat", os_patch_level="Q1-2017", environment="Production")
        assert host.fqdn == "host0.jpmchase.net"
        assert host.os_type == "Redhat"
        assert host.os_patch_level == "Q1-2017"
        assert host.environment == "Production"


class TestAllWebserversView:

    @pytest.mark.django_db
    def test_all_wevserver_view_gives_200_response_code(self):
        self.factory = RequestFactory()
        self.request = self.factory.get(path='webservers/')
        self.response = AllWebservers.as_view()(self.request)
        assert self.response.status_code == 200