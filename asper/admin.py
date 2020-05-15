from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(UserDetail)
admin.site.register(FirstTask)
admin.site.register(Project)

admin.site.register(DesignAssignment)
admin.site.register(DesignSubmit)
admin.site.register(WebAssignment)
admin.site.register(WebSubmit)
admin.site.register(AppAssignment)
admin.site.register(AppSubmit)