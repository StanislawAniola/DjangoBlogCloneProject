from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from django.utils import timezone

from group_app import models
from group_app import forms

# Create your views here.


class GroupListView(generic.ListView):

    model = models.GroupModel
    context_object_name = 'group_list'
    template_name = 'group_app/group_list.html'


class GroupDetailView(generic.DetailView):

    model = models.GroupModel
    context_object_name = 'group_detail'
    template_name = 'group_app/group_detail.html'


class GroupCreateView(generic.CreateView):

    form_class = forms.GroupForm
    template_name = 'group_app/group_create_update.html'

    redirect_field_name = 'group_app:group_detail'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.group_author = self.request.user
        self.object.save()
        return super().form_valid(form)


class GroupUpdateView(generic.UpdateView):

    #form_class = forms.GroupForm
    model = models.GroupModel
    form_class = forms.GroupForm
    template_name = 'group_app/group_create_update.html'

    redirect_field_name = 'group_app:group_detail'


class GroupDeleteView(generic.DeleteView):

    model = models.GroupModel
    context_object_name = 'group_delete'

    template_name = 'group_app/group_delete.html'

    success_url = reverse_lazy('group_app:group_list')


class GroupListDraftView(generic.ListView):

    model = models.GroupModel
    context_object_name = 'group_list_draft'

    template_name = 'group_app/group_list_draft.html'

    def get_queryset(self):
        return models.GroupModel.objects.filter(group_published_date=None, group_author=self.request.user).order_by('-group_creation_date')


def group_publish(request, pk):

    group_object = get_object_or_404(models.GroupModel, pk=pk)
    group_object.publish_group()
    return redirect('group_app:group_detail', pk=group_object.pk)
