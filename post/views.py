from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostList(generic.ListView):
    """
    View for displaying a list of posts
    """
    model = Post
    queryset = Post.objects.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    """
    View for displaying a selected post.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Retrieve and display a post.
        """
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Handle comments on posts and render the post_detail view.
        """
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email 
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()


        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

class PostLike(View):
    """
    View to toggle likes on posts.
    """
    
    def post(self, request, slug, *args, **kwargs):
        """
        Toggle likes on posts.
        """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostCreate(LoginRequiredMixin, CreateView):
    """
    View for creating a post
    """
    model = Post
    template_name = "post_create.html"
    form_class = PostForm
    success_url = "/posts/"

    def form_valid(self, form):
        """
        Adds logged in username as author for post
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    
class PostUpdate(LoginRequiredMixin, UpdateView):
    """
    View for updating a post
    """
    model = Post
    form_class = PostForm
    template_name = "post_update.html"
    

    # Code on url permission access validation is taken from
    # DamianJacob: https://github.com/Damianjacob/MS4_breadit/tree/main/breadit
    # def get(self, request, slug):
    #     """
    #     Check if logged in user is post author.
    #     """
    #     post = get_object_or_404(Post, slug=slug)
    #     user = request.user
    #     if str(user.username) != str(post.author):
    #         raise PermissionDenied
    #     else:
    #         return render(request, 'post_update.html', {
    #             'post': post,
    #             'slug': slug
    #         })
    

    def get_success_url(self):
        """
        Direct user to home page once post is updated successfully
        """
        return reverse('post_detail', kwargs={"slug": self.object.slug})
    

class PostDelete(LoginRequiredMixin, DeleteView):
    """
    View for deleting a post
    """
    model = Post
    success_url = reverse_lazy("home")


    # Code on url permission access validation is taken from
    # DamianJacob: https://github.com/Damianjacob/MS4_breadit/tree/main/breadit
    def get(self, request, slug):
        """
        Check if logged in user is post author.
        """
        post = get_object_or_404(Post, slug=slug)
        user = request.user
        if str(user.username) != str(post.author):
            raise PermissionDenied
        else:
            return render(request, 'post_confirm_delete.html', {
                'post': post,
                'slug': slug
            })


class CommentDelete(LoginRequiredMixin, DeleteView):
    """
    View for deleting a comment
    """
    model = Comment
    # template_name = "comment_confirm_delete.html"

    def get(self, request, pk):
        """
        Check if logged in user is comment author.
        """
        comment = get_object_or_404(Comment, id=pk)
        user = request.user
        if str(user.username) != str(comment.name):
            raise PermissionDenied
        else:
            return render(request, 'comment_confirm_delete.html', {
                'object': comment,
                
            })

    def get_success_url(self):
        #following code taken from Kim Bergstroem's PP4
        post_slug = self.object.post.slug
        return reverse("post_detail", kwargs={"slug": post_slug})

