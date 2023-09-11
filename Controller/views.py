from django.shortcuts import render
from django.http import HttpResponse
from .forms import GeeksForm
from notices.models import Notices

def homePage1(request):
    return render(request, "templates/template1/index.html")


def aboutPage(request):
    data = {
        'static_link': '/static/template1_src',
        'name': 'Rustam Ali Ahmed',
    }
    return render(request, "templates/template1/about.html", data)

def notices(request):
    noticesData=Notices.objects.all().order_by('id')
    data = {
        'static_link': '/static/template1_src',
        'name': 'Rustam Ali Ahmed',
        'noticesData': noticesData,
    }
    return render(request, "templates/template1/notices.html", data)


def contactPage(request):
    django_form=GeeksForm()
    try:
        name = request.GET['name']
        email = request.GET['email']
        subject = request.GET['subject']
        message = request.GET['message']
        print(name)
        print(request.GET)
    except:
        pass
    data = {
        'static_link': '/static/template1_src/',
        'name': 'Rustam Ali Ahmed',
        'django_form':django_form,
    }
    return render(request, "templates/template1/contact.html", data)


def contactPageSubmit(request):
    if request.method == "POST":
        try:
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            print(name)
            print(request.POST)
            data = {
                'static_link': '/static/template1_src/',
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
                'posted_data': request.POST,
            }
            return render(request, "templates/template1/contactPageSubmit.html", data)
        except:
            pass

    data = {
        'static_link': '/static/template1_src/',
        'name': 'Rustam Ali Ahmed',
        'posted_data': 'Nill',
    }
    return render(request, "templates/template1/contactPageSubmit.html", data)


def testPage(request):
    data = {
        'title': 'its title',
        'name': 'Rustam Ali Ahmed',
        'email': 'ahmed.rustam77@gmail.com',
        'clist': [
            'abcd', 'asfsdf', 'sdfsdfsd',
        ],
        'student_list': [
            {'rollno': 1, 'name': 'abcd1 xyz'},
            {'rollno': 2, 'name': 'abcd2 xyz'},
            {'rollno': 3, 'name': 'abcd3 xyz'},
            {'rollno': 4, 'name': 'abcd4 xyz'},
        ],
    }
    return render(request, "templates/template1/test1.html", data)


def test1(request):
    return HttpResponse("Hello world! from controller-views test1")


def test2(request):
    return HttpResponse("Hello world! from controller-views test2")


def course(request, course):
    return HttpResponse(course)
