from django.contrib import admin
from .models import CustomUser, Debate, Vote

# Register the CustomUser model
admin.site.register(CustomUser)

# Register the Debate model
admin.site.register(Debate)

# Register the Vote model
admin.site.register(Vote)
