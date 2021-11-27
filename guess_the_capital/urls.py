from django.urls import path
from guess_the_capital.views import CapitalQuizView


urlpatterns = [
    path('get-quiz', CapitalQuizView.as_view(), name='get-capital-quiz'),
]