from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from group_app import models as gr_models
from post_app import models as ps_models

from post_app import forms

# Create your views here.


def post_add(request, pk):

    group_object = get_object_or_404(gr_models.GroupModel, pk=pk)

    if request.method == 'POST':
        post_form = forms.PostForm(data=request.POST)

        if post_form.is_valid():
            post_to_group = post_form.save(commit=False)
            post_to_group.post_belong = group_object
            post_to_group.save()

            return redirect('group_app:group_detail', pk=group_object.pk)

    post_form = forms.PostForm()
    return render(request, template_name='post_app/post_add.html', context={'group_object': group_object,
                                                                            'post_form': post_form})

@login_required
def post_publish(request, pk):

    post_object = get_object_or_404(ps_models.PostModel, pk=pk)
    group_belong_pk = post_object.post_belong.pk
    post_object.post_approve()

    return redirect('group_app:group_detail', pk=group_belong_pk)

@login_required
def post_delete(request, pk):

    post_object = get_object_or_404(ps_models.PostModel, pk=pk)
    group_belong_pk = post_object.post_belong.pk
    post_object.delete()

    return redirect('group_app:group_detail', pk=group_belong_pk)


