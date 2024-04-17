from django.shortcuts import render, redirect
from .forms import ProfilePictureForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def views (request):
    user_profile = request.user.userprofile

# Create your views here.
def update_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page
    else:
        form = ProfilePictureForm(instance=request.user.userprofile)
    return render(request, 'update_profile_picture.html', {'form': form})
