from django.contrib import admin


from .models import Indexer
from .models import URL

class Indexview(admin.ModelAdmin):
    model = Indexer
    list_display = ['name', 'get_file_repr']

    def get_file_repr(self, obj):
        return obj.count_in_file_set.all()

admin.site.register(Indexer, Indexview)
admin.site.register(URL)
# Register your models here.
