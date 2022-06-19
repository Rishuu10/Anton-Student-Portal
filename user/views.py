from user.decorators import student_required
from django.shortcuts import render, reverse
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic.base import RedirectView
from .forms import UserLoginForm, UserSignUpForm
from .constants import UserTypes, GenderTypes, USER_APP_MAPPING

class LandingView(View):
    template_name = "user/index.html"

    def get(self, request):
        return render(request, self.template_name)

class LoginView(View):
    template_name = "user/login.html"
    form_class = UserLoginForm

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        userLoginForm = self.form_class(request.POST)
        if userLoginForm.login_user(request):
            next = request.GET.get("next")
            if next:
                return HttpResponseRedirect(next)
            return HttpResponseRedirect(reverse(f"{USER_APP_MAPPING.get(request.user.user_type)}:dashboard"))
        else:
            kwargs = {"form": userLoginForm}
            return render(request, self.template_name, kwargs)


class SignUpView(View):
    template_name = "user/signup.html"
    form_class = UserSignUpForm
    extra_kwargs = {
        'gender_choices': GenderTypes.choices(),
        'user_choices': UserTypes.choices(),
    }

    def get(self, request):
        return render(request, self.template_name, self.extra_kwargs)

    def post(self, request):
        userSignUpForm = self.form_class(request.POST)
        if userSignUpForm.signUpUser(request):
            print(request.user.user_type)
            return HttpResponseRedirect(reverse(f"{USER_APP_MAPPING.get(request.user.user_type)}:dashboard"))
        else:
            kwargs = {"form": userSignUpForm}
            return render(request, self.template_name, {**kwargs, **self.extra_kwargs})

class LogoutView(RedirectView):
    permanent = False
    pattern_name = "user:login"

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
