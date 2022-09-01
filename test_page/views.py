# test_page/views.py
# django imports
from django.shortcuts import render
from django.views.generic import TemplateView, View
# local namespace imports

# Create your views here.


def test_page(request):
    return render(request, 'test_view.html', {})
    # return render_template(


class HomepageView(TemplateView):
    template_name = 'homepage.html'
