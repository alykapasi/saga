from django.contrib import admin
from .models import Story, UserPrompts, AiResponses

# Register your models here.
admin.site.register(Story)
admin.site.register(UserPrompts)
admin.site.register(AiResponses)