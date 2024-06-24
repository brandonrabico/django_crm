from django.urls import path
from . import views

urlpatterns = [
    path('', views.LeadListView.as_view(), name='leads'),
    path('<int:pk>/', views.LeadDetailView.as_view(), name='lead_detail'),
    path('create/', views.LeadCreateView.as_view(), name='lead_create'),
    path('<int:pk>/update/', views.LeadUpdateView.as_view(), name='lead_update'),
    path('<int:pk>/delete/', views.LeadDeleteView.as_view(), name='lead_delete'),
    path('<int:pk>/assign-agent/', views.AssignAgentView.as_view(), name='assign_agent'),
     path('<int:pk>/category/', views.LeadCategoryUpdateView.as_view(), name='lead-category-update'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    ]
