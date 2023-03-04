from django.contrib import admin
from .models import jobPost,accepted,deleted
# from hire.models import jobPost

admin.site.register(jobPost)
admin.site.register(accepted)
admin.site.register(deleted)