from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings


@login_required(login_url=settings.LOGIN_PAGE)
def index_view(request):
    return render(request, 'manager/index_tmpl.html', {})
