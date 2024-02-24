from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *
from mptt.admin import DraggableMPTTAdmin


# Register your models here.

admin.site.register(
    Rubric,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)