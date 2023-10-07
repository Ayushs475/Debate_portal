from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('logout/', views.UserLogoutView.as_view(), name='user-logout'),
    path('api/ban_user/<str:username>/', views.BanUserView.as_view(), name='ban-user'),
    path('api/assign_moderator_role/<str:username>/', views.AssignModeratorRoleView.as_view(), name='assign-moderator-role'),
    path('api/report_user_infraction/<str:username>/', views.ReportUserInfractionView.as_view(), name='report-user-infraction'),
    path('api/debate/create/', create_debate_view, name='create-debate'),
    path('api/debate/list/', list_debates_view, name='list-debates'),
    path('api/debate/<int:debate_id>/', debate_detail_view, name='debate-detail'),
    path('api/debate/<int:debate_id>/close/', close_debate_view, name='close-debate'),
    path('api/debate/<int:debate_id>/vote/up/', upvote_debate_view, name='upvote-debate'),
    path('api/debate/<int:debate_id>/vote/down/', downvote_debate_view, name='downvote-debate'),


]

urlpatterns = format_suffix_patterns(urlpatterns)
