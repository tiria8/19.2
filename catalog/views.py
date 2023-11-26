from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.cache import cache
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, BlogForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Blog, Version, Category
from config import settings


class ProductsListView(ListView):

    model = Product
    extra_context = {
        'title': 'Магазин мебели'
    }


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    permission_required = ["catalog.set_published", "catalog.change_category", "catalog.change_description"]

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.creator != self.request.user and not self.request.user.has_perms(self.permission_required):
            raise Http404

        return self.object

    def get_form_class(self):
        if self.request.user.has_perms(self.permission_required):
            return ProductModeratorForm

        return ProductForm

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


class BlogsListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Блог'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_viewable=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('catalog:blogs')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'description', 'preview', 'is_viewable')

    def get_success_url(self):
        return reverse('catalog:blog', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blogs')


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {phone}: {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'catalog/contacts.html', context)


def get_cached_categories():
    if settings.CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
            return category_list
        return category_list

