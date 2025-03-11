from django.contrib import admin
from django.contrib.auth.models import User, Group

# some dashboard customization
admin.site.site_header = "Launchpad Admin"
admin.site.site_title = "Launchpad Admin"
admin.site.index_title = "Welcome to LaunchPad"

# Register default models with basic config.
admin.site.register(User)
admin.site.register(Group)


