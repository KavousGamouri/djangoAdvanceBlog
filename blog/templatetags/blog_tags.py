from django import template
from blog.models import Comment, Post, Category

register = template.Library()


@register.simple_tag(name="comments_count")
def function(pk):
    return Comment.objects.filter(post=pk, approved=True).count()



