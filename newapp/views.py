from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from .models import Article,Reference,Image
from django.shortcuts import get_object_or_404


# Create your views here.
def show_login(request):
    return render(request, 'wikipedia_login.html')

def create_article_page(request):
    return render(request, 'Artilcle_create.html')

def view_all_articles(request):
    article_list = read_articles(request)
    return render(request, 'wikipedia.html', {
        'article_list': article_list,
    })


def create_user(request):
    user_name = request.POST.get('user_name')
    password = request.POST.get('password')

    User.objects.create(
        username = user_name,
        password = make_password(password))

def loginuser(request):
    if request.method == 'POST' :
        user_name =request.POST.get('user_name')
        password = request.POST.get('password')

        user = authenticate(username=user_name,password=password)
        if user is not None:
            login(request,user)
        return redirect('all_article_list')
def logoutuser(request):
    logout(request)

def create_article(request):
    article_id=Article.objects.create(
        user_id = request.user.id,
        title = request.POST.get("title"),
        content = request.POST.get("content"),
        date =request.POST.get("date")
    )
    Reference.objects.create(
        article = article_id,
        link = request.POST.get("link")
    )
    Image.objects.create(
        article = article_id,
        image_path = request.FILES["image"]
    )

    return redirect('create_articles')


def update_article(request, article_id):
    # Fetch the article with prefetch_related to optimize loading of references and images
    article = Article.objects.prefetch_related('references', 'images').get(id=article_id)

    # Update the article fields with new data
    article.title = request.POST.get("title")
    article.content = request.POST.get("content")
    article.date = request.POST.get("date")
    article.save()  # Save the updated article

    # Update existing reference(s)
    # Assuming only one reference per article (for this example)
    if article.references.exists():
        reference = article.references.first()  # Get the first reference
        reference.link = request.POST.get("link")
        reference.save()  # Save the updated reference
    else:
        # If no reference exists, create one
        Reference.objects.create(article=article, link=request.POST.get("link"))

    # Update existing image(s)
    if article.images.exists():
        image = article.images.first()  # Get the first image
        if 'image' in request.FILES:
            image.image_path = request.FILES['image']  # Update image if a new one is uploaded
            image.save()  # Save the updated image
    else:
        # If no image exists, create one
        if 'image' in request.FILES:
            Image.objects.create(article=article, image_path=request.FILES['image'])

def read_articles(request):
    articles = Article.objects.prefetch_related('references', 'images').all()
    return articles

def view_article(request, id):
    article = Article.objects.get(pk=id)

def delete_article(request,id):
    article = Article.objects.get(pk=id)
    article.delete()

