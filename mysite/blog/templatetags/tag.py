from django import template
from django.template.defaultfilters import stringfilter
from ..models import Post

register = template.Library()

@register.simple_tag
def hello_world():
    s = Post.objects.all().last()
    s1=s.given_text
    s2=s.automated_text
    s1=s1.split()
    s2=s2.split()

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return (distances[-1]/len(s1))*100
