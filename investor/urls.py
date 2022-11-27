from django.urls import path
from . import views


urlpatterns = [
    path('period/', views.PeriodListAPIView.as_view(), name="period-list"),
    path('period/<int:id>', views.PeriodDetailAPIView.as_view(),
         name="period-detail"),
    path('period/all/', views.PeriodAllListAPIView.as_view(), name="all-period"),
    path('risk/', views.RiskListAPIView.as_view(), name="risk-list"),
    path('risk/<int:id>', views.RiskDetailAPIView.as_view(),
         name="risk-detail"),
    path('risk/all/', views.RiskAllListAPIView.as_view(), name="all-risk"),
    path('size/', views.SizeListAPIView.as_view(), name="size-list"),
    path('size/<int:id>', views.SizeDetailAPIView.as_view(),
         name="size-detail"),
    path('size/all/', views.SizeAllListAPIView.as_view(), name="all-size"),
    path('interest/', views.InterestListAPIView.as_view(), name="interest-list"),
    path('interest/<int:id>', views.InterestDetailAPIView.as_view(),
         name="interest-detail"),
    path('interest/all/', views.InterestAllListAPIView.as_view(),
         name="interest-risk"),
    path('investment/<int:id>', views.InvestmentAPIView.as_view(),
         name="create-investment"),
    path('list/investment/', views.InvestorListAPIView.as_view(),
         name="list-investment"),
    path('approve/<int:id>', views.ApproveInvestmentAPIView.as_view(),
         name="approve-investment"),
    path('close/<int:id>', views.CloseInvestmentAPIView.as_view(),
         name="close-investment"),
]
