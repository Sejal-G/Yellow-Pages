from django.contrib import admin

# Register your models here.
from .models import Server
from .models import Carpenter
from .models import Plumber
from .models import Mason,Driver
from .models import User

class  ServerModelAdmin(admin.ModelAdmin):
    list_display=["profession"]
    list_display_links=["profession"]
    search_fields=["profession"]
    class Meta:
        model=Server
admin.site.register(Server,ServerModelAdmin)

class  CarpenterModelAdmin(admin.ModelAdmin):
    list_display=["name","contact"]
    list_display_links=["name"]
    search_fields=["name"]
    list_editable=["contact"]
    class Meta:
        model=Carpenter

admin.site.register(Carpenter,CarpenterModelAdmin)

class  PlumberModelAdmin(admin.ModelAdmin):
    list_display=["name","contact"]
    list_display_links=["name"]
    search_fields=["name"]
    list_editable=["contact"]
    class Meta:
        model=Plumber

admin.site.register(Plumber,PlumberModelAdmin)

class  MasonModelAdmin(admin.ModelAdmin):
    list_display=["name","contact"]
    list_display_links=["name"]
    search_fields=["name"]
    list_editable=["contact"]
    class Meta:
        model=Mason

admin.site.register(Mason,MasonModelAdmin)


class  DriverModelAdmin(admin.ModelAdmin):
    list_display=["name","contact"]
    list_display_links=["name"]
    search_fields=["name"]
    list_editable=["contact"]
    class Meta:
        model=Driver

admin.site.register(Driver,DriverModelAdmin)



class  UserModelAdmin(admin.ModelAdmin):
    # list_display=["name"]

    class Meta:
        model=User
admin.site.register(User,UserModelAdmin)
