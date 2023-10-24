from .models import Post, Category


def recent_post(request):
    recent_posts = Post.objects.order_by('-id')[:5]
    return {"recent_posts": recent_posts}


def post_categories(request):
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}
