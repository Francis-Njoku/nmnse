from django.urls import path
from . import views


urlpatterns = [
    path('image/', views.GalleryAPIView.as_view(), name="post-image"),
    path('image/<int:id>', views.GalleryUDAPIView.as_view(), name="update-image"),
    path('investment/', views.InvestmentListAPIView.as_view(),
         name="investment-list"),
    path('investor/returns/', views.TotalReturnsAPIView.as_view(),
         name="investment-returns"),
    path('investor/amounts/', views.TotalReturnsAPIView.as_view(),
         name="investment-returns"),
    path('investment/room/<slug:slug>', views.RoomInvestmentListAPIView.as_view(),
         name="investment-list"),
    path('approve/<int:id>', views.ApproveInvestmentAPIView.as_view(),
         name="approve-investment"),
    path('close/<int:id>', views.CloseInvestmentAPIView.as_view(),
         name="close-investment"),
    path('dealtype/', views.DealTypeListAPIView.as_view(),
         name="list-dealtype"),
    path('dealtype/create/', views.DealTypeAListAPIView.as_view(),
         name="create-dealtype"),
    path('dealtype/<int:id>', views.DealTypeAPIView.as_view(),
         name="update-dealtype"),
    path('currency/', views.CurrencyListAPIView.as_view(),
         name="list-currency"),
    path('currency/create/', views.CurrencyAListAPIView.as_view(),
         name="create-currency"),
    path('currency/<int:id>', views.CurrencyAPIView.as_view(),
         name="update-currency"),
    path('invest/', views.InvestmentAPIView.as_view(),
         name="post-investment"),
    path('invest/<int:id>', views.InvestmentUDAPIView.as_view(),
         name="update-investment"),
    path('invest/room/', views.InvestmentRoomAPIView.as_view(),
         name="room-investment"),
    path('portfolio/<slug:slug>', views.InvestmentDetailAPIView.as_view(),
         name="investment-portfolio"),
    path('mainroom/', views.MainRoomListAPIView.as_view(),
         name="main-category-list"),
    path('mainroom/<int:id>', views.MainRoomDetailAPIView.as_view(),
         name="category-detail"),
    path('mainroom/all/', views.MainRoomAllListAPIView.as_view(),
         name="all-main-category"),
    path('room/', views.CategoryListAPIView.as_view(), name="main-category-list"),
    path('room/<int:id>', views.CategoryDetailAPIView.as_view(),
         name="category-detail"),
    path('room/all/', views.CategoryAllListAPIView.as_view(), name="all-category"),
    path('total/investment/', views.TotalInvesmentAmountAPIView.as_view(),
         name="total-investment"),
    path('total/investment/verified/', views.TotalVerifiedInvesmentAmountAPIView.as_view(),
         name="total-verified-investment"),
    path('total/investment/not-verified/', views.TotalNVerifiedInvesmentAmountAPIView.as_view(),
         name="total-notverified-investment"),
    path('total/investment/raise/', views.TotalAmountRaiseAPIView.as_view(),
         name="total-raise"),
    path('total/amount/received/', views.TotalAmountReceivedAPIView.as_view(),
         name="total-received"),
    path('verified/', views.TotalVerifiedInvesmentsAPIView.as_view(),
         name="verified-investment"),
    path('not-verified/', views.TotalNVerifiedInvesmentsAPIView.as_view(),
         name="verified-investment"),
    path('verify/', views.TotalNVerifiedInvesmentsAPIView.as_view(),
         name="verified-investment"),
    path('count/users/', views.UserInvestmentListAPIView.as_view(),
         name="users-investment"),
    path('admin/export/', views.AdminExportInvestmentAPIView.as_view(),
         name="admin-export-investments"),
]
