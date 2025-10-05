from django.urls import path
from .views import FranchiseListView, FranchiseDetailView

urlpatterns = [
    path('', FranchiseListView.as_view()),
    path('<int:pk>/', FranchiseDetailView.as_view())
]