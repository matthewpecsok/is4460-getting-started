from django.shortcuts import render


def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)


def south_korea(request):
    context = {
        "title": "A Food-Filled Day in South Korea",
    }
    return render(request, "south_korea.html", context)


def japan(request):
    context = {
        "title": "A Quiet Morning in Kyoto",
    }
    return render(request, "japan.html", context)
