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

class IndividualWebservers(TemplateView):
    template_name = 'inventroypages/individual_webservers.html'

    def get(self, response, id):
        webserver = Webserver.objects.get(id=id)
        response = [{
            'id': webserver.id,
            'name': webserver.name,
            'vendor': webserver.vendor,
            'patch_level': webserver.patch_level,
            'in_use': webserver.in_use
        }]
        return self.render_to_response({'webserver': response})

class IndividualDatabases(TemplateView):
    template_name = 'inventroypages/individual_databases.html'

    def get(self, response):
        database = Database.objects.get(id=id)
        response = [{
            'id': database.id,
            'name': database.name,
            'vendor': database.vendor,
            'patch_level': database.patch_level,
            'in_use': database.in_use
        }]
        return self.render_to_response({'database': response})

class IndividualHostForms(TemplateView):
    template_name = 'inventroypages/individual_hosts.html'

    def get(self, response):
        host = Host.objects.get(id=id)
        response = [{
            'id': host.id,
            'fqdn': host.fqdn,
            'os_type': host.os_type,
            'os_patch_level': host.os_patch_level,
            'environment': host.environment
        }]
        return self.render_to_response({'host': response})            
