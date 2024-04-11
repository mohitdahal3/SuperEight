from django.contrib import admin

# Register your models here.
from webapp.models import Row

class RowAdmin(admin.ModelAdmin):
    list_display = ('get_custom_index', 'column1', 'column2', 'column3', 'column4', 'column5' , 'column6' , 'column7')
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.order_by('id')
    
    def get_custom_index(self, obj):
        # Get all ids of rows in ascending order
        all_ids = list(Row.objects.values_list('id', flat=True))
        # Find index of current row's id within all_ids list
        try:
            index = all_ids.index(obj.id) + 1  # Adding 1 to start indexing from 1
        except ValueError:
            index = None
        return index

    get_custom_index.short_description = 'Index'

admin.site.register(Row , RowAdmin)