from django.shortcuts import redirect
from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # posts est le nom de notre QuerySet
    return render(request, 'blog/post_list.html', {'posts':posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) 
    # le premier pk est le nom du champ dans la base de donn�es (pk : primary key)
    # le deuxi�me est la valeur pass�e � la fonction 'post_detail, obtenue � partir de l'URL captur�e par Django
    # Django cherche alors dans la table correspondante au mod�le 'Post' une entr�e dont la cl� primaire ('pk') est �gale � 3 par exemple
    # Si un tel objet est trouv�, il est retourn� et utilis� dans la vue, si aucun objet n'est trouv�, Django g�n�re une erreur HTTP 404 indiquant qu'aucun objet n'a �t� 
    # trouv� avec cette cl� primaire
    return render(request, 'blog/post_detail.html', {'post' : post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})



def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})