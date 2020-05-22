from django.contrib import admin

# Register your models here.

from .models import Colaborador, Horario, Evaluacion, Ingreso


class ColaboradorAdmin(admin.ModelAdmin):

    list_filter = ('activo','saludable')

    search_fields = ['cedula','nombre','activo','saludable','horario']

    list_display = ('cedula','nombre','activo','saludable','horario')

class HorarioAdmin(admin.ModelAdmin):


    search_fields = ['nombre']

    list_display = ('nombre',
                    'lunes_entrada', 'lunes_salida',
                    )
    fields = ['nombre',
              ('lunes_entrada', 'lunes_salida'),
              ('martes_entrada','martes_salida'),
              ('miercoles_entrada', 'miercoles_salida'),
              ('jueves_entrada', 'jueves_salida'),
              ('viernes_entrada', 'viernes_salida'),
              ('sabado_entrada', 'sabado_salida'),
              ('domingo_entrada', 'domingo_salida')
              ]

    # fieldsets = (#('Informacion', {'fields': ('nombre')}),
    #     ('Lunes', {'fields': ('lunes_entrada', 'lunes_salida')}),
    #     ('Martes', {'fields': ('martes_entrada', 'martes_salida')}),
    #     ('Miercoles', {'fields': ('miercoles_entrada', 'miercoles_salida')}),
    #     ('Jueves', {'fields': ('jueves_entrada', 'jueves_salida')}),
    #     ('Viernes', {'fields': ('viernes_entrada', 'viernes_salida')}),
    #     ('Sabado', {'fields': ('sabado_entrada', 'sabado_salida')}),
    #     ('Domingo', {'fields': ('domingo_entrada', 'domingo_salida')})
    # )

class EvaluacionAdmin(admin.ModelAdmin):

    list_filter = ['saludable']

    search_fields = ['cedula','nombre']

    list_display = ('colaborador','cedula','saludable')

class IngresoAdmin(admin.ModelAdmin):

    list_filter = ['fecha','permitido']

    search_fields = ['fecha','cedula','nombre','temperatura']

    list_display = ('fecha','cedula','nombre','permitido','temperatura')

admin.site.register(Colaborador, ColaboradorAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Evaluacion, EvaluacionAdmin)
admin.site.register(Ingreso, IngresoAdmin)
