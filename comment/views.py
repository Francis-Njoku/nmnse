from django.shortcuts import render
from authentication.models import User
from .models import Comment
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework import filters, generics, status, views, permissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from authentication.utils import serial_investor
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.db.models import Sum, Aggregate, Avg
from django.http import JsonResponse, Http404, HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers
from investment.models import Investors
from .utils import transaction_generator
# Create your views here.


class CreateCommentAPIView(generics.GenericAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = User.objects.all().order_by('-created_at')
    permission_classes = (IsAuthenticated,)
    # parser_classes = [MultiPartParser, FormParser]
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    def get_object(self, id):
        try:
            return Investors.objects.get(id=id)
        except Investors.DoesNotExist:
            raise Http404

    def post(self, id, request):
        snippet = self.get_object(id)
        commentdata = {'investor': id,
                       'comment': request.data.get('comment'),
                       'is_closed': False,
                       'slug': str(transaction_generator())}
        in_serializer = self.serializer_class(data=commentdata)
        in_serializer.is_valid(raise_exception=True)
        in_serializer.save()
        return Response(commentdata, status=status.HTTP_201_CREATED)


class AdminCreateCommentAPIView(generics.GenericAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = User.objects.all().order_by('-created_at')
    permission_classes = (IsAuthenticated,)
    # parser_classes = [MultiPartParser, FormParser]
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['firstname', 'lastname', 'email']
    search_fields = ['firstname', 'lastname', 'email']

    def get_object(self, id):
        try:
            return Investors.objects.get(id=id)
        except Investors.DoesNotExist:
            raise Http404

    def post(self, id, request):
        snippet = self.get_object(id)
        commentdata = {'investor': id,
                       'comment': request.data.get('comment'),
                       'is_closed': True,
                       'responded_by': request.user,
                       'slug': str(transaction_generator())}
        in_serializer = self.serializer_class(data=commentdata)
        in_serializer.is_valid(raise_exception=True)
        in_serializer.save()
        return Response(commentdata, status=status.HTTP_201_CREATED)


class AdminUserCommentListAPIView(ListAPIView):
    serializer_class = serializers.UserInvestmentSerializer
    queryset = Investors.objects.all().order_by('-created_at')
    permission_classes = (IsAuthenticated, IsAdminUser,)
    # parser_classes = [MultiPartParser, FormParser]
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['serialkey']
    search_fields = ['serialkey']

    def get_queryset(self):
        return self.queryset.all()
