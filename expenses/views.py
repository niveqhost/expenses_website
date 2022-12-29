from django.shortcuts import render
from django.views import generic

# Create your views here.
class IndexView(generic.View):
    template_name = "expenses/index.html"

    def get(self, request):
        try:
            return render(request=request, template_name=self.template_name)
        except Exception as ex:
            print('INDEX VIEW GET REQUEST ERROR: ', ex)