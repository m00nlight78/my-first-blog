"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # importe la configuration de l'administration Django qui fournit une interface pr�te � l'emploi pour g�rer le contenu de mon site
from django.urls import path, include # importe la fonction 'path' qui est utilis�e pour associer une URL � une vue

urlpatterns = [ # d�finit une liste de chemins (URL patterns) que Django utilisera pour diriger les requ�tes entrantes vers les bonnes vues
    path('admin/', admin.site.urls),  # Cette ligne signifie que pour toutes les URL commen�ant par admin/, Django trouvera une vue correspondante
    path('',include('blog.urls')), # Cette ligne signifie que toutes les URLs d�finies dans le fichier 'blog/urls.py' seront ajout�es � la racine du site
]
