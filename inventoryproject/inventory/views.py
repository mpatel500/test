from django.views.generic import TemplateView
<<<<<<< HEAD
from django.http.response import Http404, HttpResponseRedirect
from inventory.models import Webserver
from inventory.form import WebserverForm
from django.urls.base import reverse
=======
from django.http.response import Http404
from inventory.models import Webserver, Database, Host
>>>>>>> 156fd15fb7dae9c2929daf9264cd8362f532ac7e

class AllWebservers(TemplateView):
    template_name = 'inventorypages/all_webservers.html'
    
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
<<<<<<< HEAD

class AddWebserverView(TemplateView):
    template_name = 'inventorypages/add_webserver.html'

    def get(self, request):
        form = WebserverForm()
        return self.render_to_response({'form':form})
    
    def post(self, request, response):
        form = WebserverForm(data = request.POST)
        if not form.is_valid():
            return self.render_to_response({'errors':form.errors})
        webserver = form.save(commit = False)
        webserver.in_use = False
        webserver.save()
        return HttpResponseRedirect(reverse('all_webservers'))
 
=======
    
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
>>>>>>> 156fd15fb7dae9c2929daf9264cd8362f532ac7e
