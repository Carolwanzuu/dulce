from hostels.models import Hostels
from hostels.forms import HostelForm, RegistrationForm, UpdateProfileForm, UserUpdateForm, profileForm
from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    host_items=Hostels.objects.all()
    return render(request, 'index.html', {'host_items':host_items})

def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        procForm=profileForm(request.POST, request.FILES)
        if form.is_valid() and procForm.is_valid():
            username=form.cleaned_data.get('username')
            user=form.save()
            profile=procForm.save(commit=False)
            profile.user=user
            profile.save()

            # messages.success(request, f'Successfully created Account!.You can now login as {username}!')
        return redirect('login')
    else:
        form= RegistrationForm()
        prof=profileForm()
    params={
        'form':form,
        'profForm': prof
    }
    return render(request, 'registration/signup.html', params)

def hostels(request, id):
    host = Hostels.objects.get(id=id)
    return render(request,'hostel.html',{'hostels':host})

def profile(request):
    
    return render(request, 'profile.html')

def edit_Profile(request):
    user= request.user
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return render(request, 'editprofile.html')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UpdateProfileForm()
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'editprofile.html', context)

def book_hostel(request):
    if request.method == 'POST':
        form = HostelForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hostel')
    else:
        form = HostelForm()
        return render(request, 'book.html', {'form': form})