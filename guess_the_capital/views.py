from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
import requests
import pandas as pd
import random


# Create your views here.
class CapitalQuizView(TemplateView):
    url = 'https://countriesnow.space/api/v0.1/countries/capital'
    r = requests.get(url)
    data = r.json()['data']
    df = pd.DataFrame(data)
    #Remove countries with empty strings/null as capitals
    df = df[df['capital'].astype(bool)]

    def get(self, request):
        try:
            rand_int = random.randint(0, self.df.shape[0])
            return JsonResponse(
                data={'country': self.df.iloc[rand_int]['name'],
                      'capital': self.df.iloc[rand_int]['capital']},
                status=200)
        except Exception:
            return HttpResponse(status=500)
