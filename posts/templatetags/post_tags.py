from django import template
from posts.models import PostLikes

register = template.Library()

@register.simple_tag
def likes_count(post_id): 
    return PostLikes.objects.filter(post_id=post_id).count()