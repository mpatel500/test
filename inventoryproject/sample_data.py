from inventory.models import Webserver, Database, Host, HostApplications

Webserver.objects.all().delete()
Database.objects.all().delete()
Host.objects.all().delete()
HostApplications.objects.all().delete()

x = 0
patchlvl = 0
release_year = 2013
while x < 20:
    name = 'webserver_{id}'.format(id=str(x))
    if x < 5:
        vendor = 'Apache'
        patch = 'A{lvl}-{yr}'.format(lvl=str(patchlvl), yr=str(release_year))
    elif x < 10:
        vendor = 'Microsoft'
        patch = 'M{lvl}-{yr}'.format(lvl=str(patchlvl), yr=str(release_year))
    elif x < 15:
        vendor = 'NGINX, Inc.'
        patch = 'N{lvl}-{yr}'.format(lvl=str(patchlvl), yr=str(release_year))
    elif x < 20:
        vendor = 'Google'
        patch = 'G{lvl}-{yr}'.format(lvl=str(patchlvl), yr=str(release_year))
    if x % 5 == 0:
        patchlvl = 0
        release_year = 2013
    if x < 15:
        use = True
    else:
        use = False
    Webserver.objects.create(name=name, vendor=vendor, patch_level=patch, in_use=use)
    x += 1
    patchlvl += 1
    release_year += 1

x = 0
patchlvl = 16.0
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
    elif x < 20:
        vendor = 'vendor 4'
        patchlvl = 15.0
    if x < 15:
        use = True
    else:
        use = False
    Database.objects.create(name=name, vendor=vendor, patch_level=patchlvl, in_use=use)
    x += 1
    patchlvl += 1
    release_year += 1

x = 0
patchlvl = 0
release_year = 2013
while x < 20:
    fqdn = 'host{id}.jpmchase.net'.format(id=str(x))
    if x < 5:
        os_type = 'Redhat'
        os_patch_level = 'R{lvl}-{yr}'.format(lvl=str(patchlvl), yr=str(release_year))
    elif x < 10:
        os_type = 'Oracle Linux'
        os_patch_level = 'OL{lvl}-{yr}'.format(lvl=str(patchlvl), yr=str(release_year))
    elif x < 15:
        os_type = 'AIX'
        os_patch_level = 'A{lvl}-{yr}'.format(lvl=str(patchlvl), yr=str(release_year))
    elif x < 20:
        os_type = 'Gento'
        os_patch_level = 'G{lvl}-{yr}'.format(lvl=str(patchlvl), yr=str(release_year))
    if x % 5 == 0:
        release_year = 2013
        patchlvl = 0
    if x % 2 == 0:
        environment = 'Production'
    else:
        environment = 'Development'
    host = Host.objects.create(fqdn=fqdn, os_type=os_type, os_patch_level=os_patch_level, environment=environment)
    host.save()
    x += 1
    patchlvl += 1
    release_year += 1

x = 0 
while x < 9:
    used_webservers = Webserver.objects.filter(in_use=True)
    used_databases = Database.objects.filter(in_use=True)
    production_hosts = Host.objects.filter(environment='Production')
    for used in used_webservers[:5]:
        HostApplications.objects.create(host_id=production_hosts[x].id,webserver_ids=(used.id,),database_ids=((),))
        x += 1 
    for used in used_databases[:5]:
        HostApplications.objects.create(host_id=production_hosts[x].id,webserver_ids=((),),database_ids=(used.id,))
        x += 1 


used_webservers = Webserver.objects.filter(in_use=True)
used_webservers = used_webservers[5:]
used_databases = Database.objects.filter(in_use=True)
used_databases = used_databases[5:]
development_hosts = Host.objects.filter(environment='Development')
x = 0 
for dev in development_hosts:
    HostApplications.objects.create(host_id=dev.id,webserver_ids=(str(used_webservers[x].id),),database_ids=(str(used_databases[x].id),))
    x += 1 


