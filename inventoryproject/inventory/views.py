from django.views.generic import TemplateView
from django.http.response import Http404
from inventory.models import Webserver, Database, Host

class AllWebservers(TemplateView):
    template_name = 'inventroypages/all_webservers.html'
    
    def get(self, response):
        webservers = Webserver.objects.all()
        response = [{
            'id': w.id,
            'name': w.name,
            'vendor': w.vendor,
            'patch_level': w.patch_level,
            'in_use': w.in_use
        } for w in webservers
        ]
        return self.render_to_response({'webservers': response})
    
class AllItems(TemplateView):
    template_name = 'inventroypages/all_items.html'

    def get(self, response):
        webserver_items = Webserver.objects.all()
        database_items = Database.objects.all()
        host_items = Host.objects.all()
        response = [{
            'id': i.id,
            'name': i.name,
            'vendor': i.vendor,
            'patch_level': i.patch_level,
            'in_use': i.in_use,
            'type': 'Webserver'
        } for i in webserver_items]
        response += [{
            'id': i.id,
            'name': i.name,
            'vendor': i.vendor,
            'patch_level': i.patch_level,
            'in_use': i.in_use,
            'type': 'Database'
        } for i in database_items]
        response += [{
            'id': i.id + len(webserver_items) + len(database_items),
            'fqdn': i.fqdn,
            'os_type': i.os_type,
            'os_patch_level': i.os_patch_level,
            'environment': i.environment,
            'type': 'Host'
        } for i in host_items]
        
        return self.render_to_response({'items': response})