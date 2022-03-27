"""Configuration of the admin interface for microblogs."""
from django.contrib import admin
from .models import Post, User, Comment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for users."""

    list_display = [
        'username', 'first_name', 'last_name', 'email', 'is_active',
    ]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for posts."""

    list_display = [
        'get_author', 'text', 'created_at',
    ]

    def get_author(self, post):
        """Return the author of a given post."""
        return post.author.username

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for comments."""

    list_display = [
        'post', 'name', 'body', 'created_at',
    ]

    def get_author(self, post):
        """Return the author of a given post."""
        return post.author.username