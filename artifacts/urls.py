from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import artifact_list, artifact_create, artifact_update, artifact_delete, artifact_export_word, user_login, user_logout

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('artifact_list', login_required(artifact_list), name='artifact_list'),
    path('create/', login_required(artifact_create), name='artifact_create'),
    path('update/<int:pk>/', login_required(artifact_update), name='artifact_update'),
    path('delete/<int:pk>/', login_required(artifact_delete), name='artifact_delete'),
    path('artifac/<int:pk>/export_word/', login_required(artifact_export_word), name='artifact_export_word'),
]
