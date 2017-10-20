import django.core.exceptions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from public.models.Content import Content


class ContentAPI(viewsets.ViewSet):
    @csrf_exempt
    def uploadText(self, request):
        txt = request.POST.get("txt", "").strip()
        if not txt or len(txt) > 50:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            Content(txt=txt).save()
        except Exception as ex:
            print("Exception %s", type(ex))
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"success": True})

    @csrf_exempt
    @method_decorator(login_required)
    def removeText(self, request):
        if "list_txt" not in request.POST or request.POST.get("list_txt", None) is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        import json
        try:
            for l in json.loads(request.POST['list_txt']):
                Content(id=l).delete()
        except django.core.exceptions.ObjectDoesNotExist as ex:
            print("Exception %s", type(ex))
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as ex:
            print("Exception %s", type(ex))
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"success": True})

    @csrf_exempt
    @method_decorator(login_required)
    def getText(self, request):
        return Response({"txt_list": Content.objects.all().values("id", "txt")})
