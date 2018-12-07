from inventory.models import Webserver

class WebserverData:    
    def create_webserver_objects(self):
        Webserver.objects.all().delete()
        x = 0
        patchlvl = 0 
        release_year = 2013
        while x < 20:
            name = 'webserver_{id}'.format(id=str(x))
            if x < 5:
                vendor = 'Apache'
                patch = 'A{patch_level}-{patch_year}'.format(patch_level=str(patchlvl),patch_year=str(release_year))
            elif x < 10:
                patchlvl = 0 
                release_year = 2013
                vendor = 'Microsoft'
                patch = 'M{patch_level}-{patch_year}'.format(patch_level=str(patchlvl),patch_year=str(release_year))
            elif x < 15:
                vendor = 'NGINX, Inc.'
                patchlvl = 0 
                release_year = 2013
                patch = 'N{patch_level}-{patch_year}'.format(patch_level=str(patchlvl),patch_year=str(release_year))
            elif x < 20:
                vendor = 'Google'
                patchlvl = 0 
                release_year = 2013
                patch = 'G{patch_level}-{patch_year}'.format(patch_level=str(patchlvl),patch_year=str(release_year))
            
            if x % 4 ==0:
                use = True 
            else:
                use = False 
            Webserver.objects.create(name=name, vendor=vendor, patch_level=patch,in_use=use)
            x +=1
            patchlvl +=1
            release_year +=1  


