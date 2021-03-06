from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.
from blog.models import Blog, BlogType


def blog_list(request):
    context = {'blogs': Blog.objects.all(),
               # 'blogs_length': Blog.objects.all().count(),
               'blog_types': BlogType.objects.all()
               }
    return render_to_response('blog/blog_list.html', context)


def blog_detail(request, blog_pk):
    context = {'blog': get_object_or_404(Blog, pk=blog_pk)}
    return render_to_response('blog/blog_detail.html', context)


def blogs_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    context = {'blogs': Blog.objects.filter(blog_type=blog_type),
               'blog_type': blog_type,
               'blog_types': BlogType.objects.all(),
               }
    return render_to_response('blog/blogs_with_type.html', context)
