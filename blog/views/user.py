from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from blog.models import User
from blog.forms import CustomUserForm, UserProfileUpdateForm
from django.contrib import messages

from django.http import JsonResponse, HttpResponseRedirect


@login_required(login_url="account_login")
def retrieve(request, username):
    users = User.objects.prefetch_related('interests')
    user = get_object_or_404(users, username=username)

    full_name = user.get_full_name() or "-"
    birthday = user.birthday or "-"
    gender = user.get_gender_display() or "-"
    marital_status = user.get_marital_status_display() or "-"
    educational_status = user.get_educational_status_display() or "-"
    profession = user.get_profession_display() or "-"
    interests = ", ".join(
        [interest.name for interest in user.interests.all()]) or "-"
    phone_number = user.phone_number or "-"

    context = {
        'username': user.username,
        'full_name': full_name,
        'birthday': birthday,
        'gender': gender,
        'marital_status': marital_status,
        'educational_status': educational_status,
        'profession': profession,
        'interests': interests,
        'phone_number': phone_number
    }

    return render(request, 'user/retrieve.html', context=context)


@login_required(login_url="account_login")
def updateUser(request, username):
    users = User.objects.prefetch_related('interests')
    user = get_object_or_404(users, username=username)
    #user = get_object_or_404(User, username=username)
    form = CustomUserForm(request.POST or None,
                          request.FILES or None, instance=user)
    if form.is_valid():
        user = form.save()
        user.save()
        messages.success(request, "Profile Updated Successfully")
        return HttpResponseRedirect(reverse('retrieve', kwargs={'username': user.username}))
        # return redirect("retrieve", username=username)
    return render(request, "user/updateprofile.html", {"form": form})


# olmadı
# @login_required(login_url="account_login")
# def user_upload_photo(request):
#     #user = get_object_or_404(users, username=username)
#     if request.method == "POST":
#         form = UserProfileUpdateForm(
#             instance=request.user.profile_image.url, data=request.POST, files=request.FILES or None)
#         if form.is_valid():
#             user = form.save(commit=True)
#             data = {'is_valid': True, 'image-url': user.profile_image.url,
#                     'success': 'Profile Foto Updated Successfully'}
#         else:
#             data = {'is_valid': False}
#         return JsonResponse(data)
#     else:
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
