from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from .constants import UserTypes


def student_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):

    custom_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.user_type == UserTypes.STUDENT.value,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return custom_decorator(function)
    return custom_decorator


def teacher_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):

    custom_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.user_type == UserTypes.TEACHER.value,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return custom_decorator(function)
    return custom_decorator