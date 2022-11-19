from django.urls import path
from . import views


urlpatterns = [
    path('image/', views.GalleryAPIView.as_view(), name="post-image"),
    path('image/<int:id>', views.GalleryUDAPIView.as_view(), name="update-image"),
    path('room/', views.CategoryListAPIView.as_view(), name="category-list"),
    path('investment/', views.InvestmentListAPIView.as_view(),
         name="investment-list"),
    path('invest/', views.InvestmentAPIView.as_view(),
         name="post-investment"),
    path('invest/<int:id>', views.InvestmentUDAPIView.as_view(),
         name="update-investment"),
    path('invest/room/', views.InvestmentRoomAPIView.as_view(),
         name="room-investment"),
    path('portfolio/<slug:slug>', views.InvestmentDetailAPIView.as_view(),
         name="investment-portfolio"),
    path('room/<int:id>', views.CategoryDetailAPIView.as_view(),
         name="category-detail"),
    path('room/all/', views.CategoryAllListAPIView.as_view(), name="all-category"),
    path('total/investment/', views.TotalInvesmentAmountAPIView.as_view(),
         name="total-investment"),
    path('total/investment/verified/', views.TotalVerifiedInvesmentAmountAPIView.as_view(),
         name="total-verified-investment"),
    path('total/investment/not-verified/', views.TotalNVerifiedInvesmentAmountAPIView.as_view(),
         name="total-notverified-investment"),
    path('verified/', views.TotalVerifiedInvesmentsAPIView.as_view(),
         name="verified-investment"),
    path('not-verified/', views.TotalNVerifiedInvesmentsAPIView.as_view(),
         name="verified-investment"),
]
