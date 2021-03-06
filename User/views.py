from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.csrf import csrf_exempt
from User.form import CreationForm


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'User/login.html'
    redirect_authenticated_user = False


class UserLogoutView(LogoutView):
    template_name = 'User/login.html'
    next_page = '/login'


@csrf_exempt
def add_user_view(request):
    template_name = 'User/sign-up.html'
    context = {
        "add_form": CreationForm(),
    }
    if request.method == "GET":
        return render(request, template_name, context)
    if request.method == "POST":
        add_form = CreationForm(request.POST)
        if add_form.is_valid():
            if add_form.CheckUsername():
                add_form.save(commit=True)
                return redirect("/")

        return render(request, template_name, {"add_form": add_form})

