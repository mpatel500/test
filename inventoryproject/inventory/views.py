from django.views.generic import TemplateView
from django.http.response import Http404
from inventory.models import Webserver

class AllWebservers(TemplateView):
    template_name = 'inventorypages/all_webservers.html'
    # def get(self, response):
    #     webservers = Webserver.objects.all()

    
    