from django import forms
from inventory.models import Webserver, Database, Host

class WebserverForm(forms.ModelForm):
    class Meta:
        model = Webserver
        fields = ['name','vendor','patch_level']
class DatabaseForm(forms.ModelForm):
    class Meta:
        model = Database
        fields = ['name','vendor','patch_level']

class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ['fqdn','os_type','os_patch_level','environment']

