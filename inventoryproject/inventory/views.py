from django.views.generic import TemplateView
from django.http.response import Http404, HttpResponseRedirect
from inventory.models import Webserver
from inventory.form import WebserverForm
from django.urls.base import reverse

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
 