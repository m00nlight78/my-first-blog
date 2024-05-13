
from django import forms

from .models import Post

class PostForm(forms.ModelForm): # PostForm est le nom de notre formulaire
    
    class Meta:
        model = Post # On pr�cise � Django quel mod�le il doit utiliser pour cr�er le formulaire
        fields = ('title', 'text') # Enfin on pr�cise les champs qui doivent figurer dans notre formulaire