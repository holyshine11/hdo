from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .models import Station
from .serializers import StationSerializer
from rest_framework.pagination import PageNumberPagination

class StationPageNumberPagination(PageNumberPagination):
    page_size = 2

class StationList(APIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    pagination_class = StationPageNumberPagination
    
    def get(self, request):
        station = Station.objects.all()
        serializer = StationSerializer(station, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = StationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StationDetail(RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    
    def get_object(self, pk):
        station = get_object_or_404(Station, pk=pk)  # Model name corrected
        return station

    def get(self, request, pk):
        station = self.get_object(pk)
        serializer = StationSerializer(station)
        return Response(serializer.data)

    def patch(self, request, pk):
        station = self.get_object(pk)
        serializer = StationSerializer(station, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer)
