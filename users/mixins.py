# permissions.py
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from profiles.models import Profile

class PosterRequiredMixin(LoginRequiredMixin):
    """Verify that the current user is a poster or show message and redirect."""
    
    def dispatch(self, request, *args, **kwargs):
        # First check if user is authenticated
        if not request.user.is_authenticated:
            return self.handle_no_permission()
            
        # Then check if user is a poster
        if not self.is_poster(request.user):
            messages.error(request, "Only job posters can create new job listings")
            return self.handle_not_poster(request)
            
        return super().dispatch(request, *args, **kwargs)
    
    def is_poster(self, user):
        """Check if user has poster role"""
        return hasattr(user, 'Profile') and user.Profile.role ==Profile.Role.poster
    
    def handle_not_poster(self, request):
        """Handle non-poster users"""
        # Try to get the referer, fallback to home page
        referer = request.META.get('HTTP_REFERER')
        redirect_url = referer if referer else reverse('home')  # Change 'home' to your desired fallback
        return redirect(redirect_url)