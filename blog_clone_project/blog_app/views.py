from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy, reverse
from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from blog_app import models, forms
# Create your views here.


class PostListView(ListView):

    model = models.UserPostModel
    context_object_name = 'post_list'
    template_name = 'blog_app/post_list.html'

    def get_quryset(self):
        return models.UserPostModel.objects.filter(post_published_date__lte=timezone.now()).order_by('-post_published_date')


class PostDetailView(DetailView):

    model = models.UserPostModel
    context_object_name = 'post_detail'
    template_name = 'blog_app/post_detail.html'


class PostCreateView(CreateView):

    form_class = forms.UserPostForm
    template_name = 'blog_app/post_create_update.html'

    redirect_field_name = 'blog_app:post_detail'


class PostUpdateView(UpdateView):

    form_class = forms.UserPostForm
    template_name = 'blog_app/post_create_update.html'

    redirect_field_name = 'blog_app:post_detail'


class PostDeleteView(DeleteView):

    model = models.UserPostModel
    context_object_name = 'post_delete'
    template_name = 'blog_app/post_delete.html'

    success_url = reverse_lazy('blog_app:post_list')


class PostListDraftView(ListView):

    model = models.UserPostModel
    context_object_name = 'post_list_draft'
    template_name = 'blog_app/post_list_draft'

    def get_queryset(self):
        return models.UserPostModel.objects.filter(post_published_date__isnull=True).order_by('-post_created_date')


def post_publish(request, pk):
    post_object = get_object_or_404(models.UserPostModel, pk=pk)
    post_object.publish_post()
    return redirect(reverse('blog_app:post_detail'), pk=models.UserPostModel.pk)

#######################################
#############__COMMENTS__##############
#######################################


def comment_add(request, pk):

    post_object = get_object_or_404(models.UserPostModel, pk=pk)
    if request.method == 'POST':
        comment_form = forms.UserCommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.save(commit=False)
            comment_form.post_object = post_object
            comment_form.save()
            return redirect('blog_app:comment_add', pk=post_object.pk)

    comment_form = forms.UserPostForm(data=request.POST)
    return render(request, template_name='blog_app/comment_add.html', context={'comment_form': comment_form})


def comment_approve(request, pk):

    comment_object = get_object_or_404(models.UserCommentModel, pk=pk)
    comment_object.comment_approve()
    return redirect('blog_app:comment_detail', pk=comment_object.pk)


def comment_delete(request, pk):

    post_pk = models.UserPostModel.pk
    comment_object = get_object_or_404(models.UserCommentModel, pk=pk)
    comment_object.delete()
    return redirect(reverse('blog_app:post_detail'), pk=post_pk)
