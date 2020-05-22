from django.contrib import admin

# Register your models here.
from .models import Reunion, Historial, Sala

class ReunionAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(ReunionAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(autor=request.user)

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)

    list_filter = ['horario','activa']

    search_fields = ['id','cedula','nombre','razon_social','correo']

    list_display = ('id','horario','autor','cedula','nombre','razon_social','correo','activa')

class HistorialAdmin(admin.ModelAdmin):

    list_filter = ['ingreso','create_at']

    # search_fields = ['cedula','nombre','razon_social','correo']

    list_display = ('reunion','ingreso','create_at')


admin.site.register(Sala)
admin.site.register(Reunion, ReunionAdmin)
admin.site.register(Historial, HistorialAdmin)
