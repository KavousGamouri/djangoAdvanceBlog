from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, ContactForm, CommentForm, UpdatePostForm, NewsletterForm


class IndexView(View):
    template_name = 'blog/index_view.html'
    paginate_by = 2

    def get(self, request, cat_name=None, author_id=None):
        posts = Post.objects.filter(status=True)
        if cat_name:
            posts = Post.objects.filter(category__name=cat_name)
        if author_id:
            posts = Post.objects.filter(author=self.request.user, status=True)

        paginator = Paginator(posts, self.paginate_by)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {'posts': page_obj}
        return render(request, self.template_name, context)

    def post(self, request):
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
        return render(request, self.template_name, {"form": form})


class PostDetailView(View):
    template_name = "blog/post_detail.html"
    model = Post

    def get(self, request, pk):
        form = CommentForm()
        post = get_object_or_404(self.model, id=pk)
        comments = Comment.objects.filter(post=post.id, approved=True).order_by('-created_date')
        context = {"post": post, "comments": comments, "form": form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = get_object_or_404(self.model, id=pk)
        comments = Comment.objects.filter(post=post.id, username=post.author.id, approved=True).order_by('-created_date')
        context = {"post": post, "comments": comments, "form": form}
        if form.is_valid():
            form.save()
            return render(request, self.template_name, context)
        return render(request, self.template_name, context)


class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_create.html"
    form_class = PostForm
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = "blog/post_update.html"
    success_url = reverse_lazy("blog:index")

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(author=self.request.user)


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("blog:index")

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(author=self.request.user)


class ContactVIew(View):
    def get(self, request):
        form = ContactForm()
        return render(request, "blog/contact.html", {"form": form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Your message sent"
            context = {"form": form, "message": message}
            return render(request, "blog/contact.html", context)
        message = "Your message did not send"
        context = {"form": form, "message": message}
        return render(request, "blog/contact.html", context)


class SearchView(View):
    posts = Post.objects.filter(status=True)

    def get(self, request):
        if s := request.GET.get('s'):
            filters = Q(body__contains=s) | Q(title__contains=s) & Q(status=True)
            posts = self.posts.filter(filters)
            return render(request, "blog/index_view.html", {'posts': posts})
