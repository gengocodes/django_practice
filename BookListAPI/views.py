from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import MenuItem, Category
from .serializer import MenuItemSerializer, CategorySerializer

# Create your views here.
@api_view()
def books(request):
    return Response('list of the books', status=status.HTTP_200_OK)

class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if (author):
            return Response({'message': 'list of the books by ' + author}, status=status.HTTP_200_OK)
        
        return Response({'message': 'list of the books'}, status=status.HTTP_200_OK)
    
    def post(self, request):
        return Response({'title': request.data.get('title')}, status=status.HTTP_201_CREATED)

class Book(APIView):
    def get(self, request, pk):
        return Response({'message': 'single book with id ' + str(pk)}, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        return Response({'title': request.data.get('title')}, status=status.HTTP_200_OK)

class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['title']

class SingleMenuItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
