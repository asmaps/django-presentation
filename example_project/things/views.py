from django.views.generic import CreateView
from .models import Thing

class CreateThingView(CreateView):
    model = Thing
