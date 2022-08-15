# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world. You're at the qquiet index.")


from rest_framework import viewsets, views

from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser
from rest_framework.response import Response

from .serializers import LocationSerializer
from .models import Location
from .s3 import S3Storage

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('id')
    serializer_class = LocationSerializer

class FileUploadView(views.APIView):
    # parser_classes = [FileUploadParser]
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        # print(request.FILES)


        # if 'file' not in request.FILES:
        #     raise ParseError("Empty content")

        file_obj = request.FILES['file']
        print(file_obj)


        # temp_file = BytesIO()
        # temp_file.write(index_top.encode('utf-8'))
        # temp_file.seek(0)
        # print(temp_file.getvalue())


        uploader = S3Storage()

        import pdb; pdb.set_trace()

        uploader.put(file_obj, 'audio-01.m4a')
        # uploader.upload(request.FILES.get('file'), 'audio-01.m4a')

        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=202)
