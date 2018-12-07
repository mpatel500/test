from inventory.models import Webserver, Database, Host 


Webserver.objects.all().delete()
Database.objects.all().delete()
Host.objects.all().delete()

x = 0
patchlvl=0
release_year = 2013
while x < 20:
    name = 'Webserver_{id}'.format(id=str(x))
    if x < 5:
        vendor = 'Apache'
        patch = 'A{patch_level}-{patch_year}'.format(patch_level=str(patchlvl),patch_year=str(release_year))
    elif x < 10:
        vendor = 'Microsoft'
        patch = 'M{patch_level}-{patch_year}'.format(patch_level=str(patchlvl),patch_year=str(release_year))
    elif x < 15:
        vendor = 'NGINX, Inc.'
        patch = 'N{patch_level}-{patch_year}'.format(patch_level=str(patchlvl),patch_year=str(release_year))
    elif x < 20:
        vendor = 'Google'
        patch = 'G{patch_level}-{patch_year}'.format(patch_level=str(patchlvl),patch_year=str(release_year))

    if x % 5 == 0:
        release_year = 2013
    if x % 4 ==0:
        use = True 
    else:
        use = False 
    Webserver.objects.create(name=name, vendor=vendor, patch_level=patch,in_use=use)
    x +=1
    patchlvl +=1
    release_year +=1  

x =0 
patchlvl = 16 
while x < 20:
    name = 'Database_{id}'.format(id=str(x))

    if x < 5:
        vendor = 'Oracle'
    elif x < 10:
        vendor = 'Sybase'
        patchlvl = 18.0
    elif x < 15: 
        vendor = 'vendor 3'
        patchlvl = 17.0
    else:
        vendor = 'vendor 4'
        patchlvl = 15.0

    if x % 3 == 0:
        use = True
    else:
        use = False 

    Database.objects.create(name=name, vendor=vendor, patch_level=patchlvl, in_use=use)
    x +=1 
    patchlvl += 0.1

x=0 
patchlvl = 0
release_year = 2013
while x < 20:
    name = 'host{id}.jpmchase.net'.format(id=str(x))
    if x < 5:
        os_type = 'Redhat'
        patch = 'R{patch_level}-{patch_year}'.format(patch_level=str(patchlvl),patch_year=str(release_year))
    elif x < 10:
        os_type = 'Oracle Linux'
        patch = 'OL{patch_level}-{patch_year}'.format(patch_level=str(patchlvl),patch_year=str(release_year))
    elif x < 15:
        os_type = 'AIX'
        patch = 'A{patch_level}-{patch_year}'.format(patch_level=str(patchlvl),patch_year=str(release_year))
    elif x < 20:
        os_type = 'Gento'
        patch = 'G{patch_level}-{patch_year}'.format(patch_level=str(patchlvl),patch_year=str(release_year))

    if x % 5 == 0:
        release_year = 2013

    if x % 2 ==0:
        use = True 
    else:
        use = False 
    Host.objects.create(name=name, vendor=vendor, patch_level=patch,in_use=use)
    x +=1
    patchlvl +=1
    release_year +=1  

