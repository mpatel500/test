import pytest 
from inventory.models import Webserver
from inventory.views import AllWebservers
import unittest
from sample_data import WebserverData

class Test_Webserver_Model:

    @pytest.mark.django_db
    def test_webserver_data_is_saved(self):
        webserver =  Webserver.objects.create(name="webserver_1", vendor="Apache", patch_level="Q2-2016",in_use=False)
        assert webserver.name == "webserver_1"
        assert webserver.vendor == "Apache"
        assert webserver.patch_level == "Q2-2016"
        assert webserver.in_use == False


class Test_Sample_Data:

    @pytest.mark.django_db(transaction=True)
    def test_twenty_webserver_objects_are_saved(self):
        wd = WebserverData()
        wd.create_webserver_objects()
        num_of_objects = Webserver.objects.all()
        assert num_of_objects == 20 

