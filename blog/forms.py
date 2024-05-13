
from django import forms

from .models import Post

class PostForm(forms.ModelForm): # PostForm est le nom de notre formulaire
    
    class Meta:
        model = Post # On précise à Django quel modèle il doit utiliser pour créer le formulaire
        fields = ('title', 'text') # Enfin on précise les champs qui doivent figurer dans notre formulaire