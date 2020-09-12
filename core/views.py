from django.views.generic import ListView
from .models import PremierLeague

class MainView(ListView):
    model = PremierLeague
    template_name = 'main.html'
    paginate_by = 5
    ordering = 'position'

