from django.shortcuts import render
from django.http import HttpResponse


def test1(request):
    return HttpResponse("Hello world! from test1(request)")
