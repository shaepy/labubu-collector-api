from django.urls import path
from .views import FranchiseListView

urlpatterns = [
    path('', FranchiseListView.as_view()),
]