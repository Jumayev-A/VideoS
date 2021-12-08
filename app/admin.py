from django.contrib import admin
from .models import Videos

# Register your models here.
@admin.register(Videos)
class CategoryModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Videos
        fields = '__all__'
