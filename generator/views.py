# -*- coding:utf-8 -*-

"""Controllers for project."""

from django.shortcuts import render
from generator.models import make_password


def home(request):
    """Controller for home page.

    Args:
        request: HTTP request
    Returns:
        render: HTML page
    """
    return render(request, "generator/home.html", {"password": "Qwerty1234"})


def password(request):
    """Controller for password page.

    Args:
        request: HTTP request
    Returns:
        render: HTML page
    """
    length = int(request.GET.get("length"))
    uppercase = False
    numbers = False
    special = False

    if request.GET.get("uppercase") == "on":
        uppercase = True
    if request.GET.get("numbers") == "on":
        numbers = True
    if request.GET.get("special") == "on":
        special = True
    return render(
        request,
        "generator/password.html",
        {"password": make_password(length, uppercase, special, numbers)},
    )


def about(request):
    return render(request, "generator/about.html")
