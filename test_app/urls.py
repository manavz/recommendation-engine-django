from django.urls import path
from test_app import views


urlpatterns = [
    path("table/", views.table_view, name="get-relationships"),
    path('candidate/<int:candidate_id>/skills/', views.candidate_skills_view, name='candidate'),
    path('feature/<int:feature_id>/skills/', views.feature_skills_view, name='feature'),
    path('skill/<int:skill_id>/relations/', views.skill_detail_view, name='skill'),
]