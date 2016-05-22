from django.contrib import admin
from persistence.models import *

from django.contrib import admin 
 

class ItemAdmin(admin.ModelAdmin):
	fields = ('nombre', )


class LugarAdmin(admin.ModelAdmin):
	fields = ('nombre', 'direccion')


class DonativoAdmin(admin.ModelAdmin):
	fields = ('direccion', 'geo_ubicacion', 'usuario')


class DonativoDetAdmin(admin.ModelAdmin):
	fields = ('cantidad', 'item')


admin.site.register(Item, ItemAdmin)
admin.site.register(Lugar, LugarAdmin)
admin.site.register(Donativo, DonativoAdmin)
admin.site.register(DonativoDetalle, DonativoDetAdmin)

# Register your models here.



