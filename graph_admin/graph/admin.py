from django.contrib import admin
from .models import *
from . import models

from django.db.models import Count
from django.db.models.functions import TruncDay

@admin.register(EmailSubscriber)
class EmailSubscriberAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "created_at") # display these table columns in the list view
    ordering = ("-created_at",) 
    date_hierarchy = "created_at"
    #____________________ROUTE POUR AVOIR ACCES A LA PARTIE ADMIN_________________________#
    change_list_template = 'pages/admin/change_list_dataemail.html'
    
    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data = EmailSubscriber.objects.annotate(date=TruncDay("created_at")).values("date").annotate(nbemail=Count("id")).order_by("-date")
            
            
            
        data = {
            'chart_data':chart_data,
            'nom':'samake',
        }
        extra_context = extra_context or data

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)# vim: set fileencoding=utf-8 :


class AuthorAdmin(admin.ModelAdmin):

    list_display = ('name', 'age', 'status', 'date_add', 'date_udp')
    list_filter = (
        'status',
        'date_add',
        'date_udp',
        'name',
        'age',
    )
    search_fields = ('name',)


class PublisherAdmin(admin.ModelAdmin):

    list_display = ('name', 'status', 'date_add', 'date_udp')
    list_filter = (
        'status',
        'date_add',
        'date_udp',
        'name',
    )
    search_fields = ('name',)


class BookAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'pages',
        'price',
        'rating',
        'publisher',
    )
    list_filter = (
        'publisher',
        'status',
        'date_add',
        'date_udp',
        'name',
        'pages',
        'price',
        'rating',
        'publisher',
    )
    raw_id_fields = ('authors',)
    search_fields = ('name',)


class StoreAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'status', 'date_add', 'date_udp')
    list_filter = (
        'status',
        'date_add',
        'date_udp',
        'name',
    )
    raw_id_fields = ('books',)
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Author, AuthorAdmin)
_register(models.Publisher, PublisherAdmin)
_register(models.Book, BookAdmin)
_register(models.Store, StoreAdmin)
