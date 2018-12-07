from django.views.generic import TemplateView
from django.http.response import Http404
from inventory.models import Webserver

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
    