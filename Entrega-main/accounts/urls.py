

from django.urls import path, include

from accounts.views import cerrar, iniciar, signup, profile, editar_perfil

urlpatterns = [
    path('profile', profile),
    path('profile/editar', editar_perfil),
    path('signup', signup),
    path('iniciar', iniciar),
    path('cerrar', cerrar),
]
