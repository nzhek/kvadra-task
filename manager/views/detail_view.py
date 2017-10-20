from django.shortcuts import render


def detail_view(request, element_code):
    return render(request, 'manager/detail_tmpl.html', {"txt":""})
