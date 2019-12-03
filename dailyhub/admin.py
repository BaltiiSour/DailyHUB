from dailyhub.models import Contacto 
from django.contrib import admin

class ContactoAdmin(admin.ModelAdmin):
    # define which columns displayed in changelist
    list_display = ('nombre', 'apellido', 'email', 'direccion','preferencia')
    # add filtering by date
    list_filter = ('nombre','apellido','email','direccion','preferencia')
    # add search field 
    search_fields = ['nombre', 'apellido','email']

admin.site.register(Contacto, ContactoAdmin)
#admin.site.register(Contacto)