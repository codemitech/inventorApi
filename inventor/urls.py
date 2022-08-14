from django.urls import path
from . views import  AllInvestmentView, CustomAuthToken,AllInventionsView, InventorUpdateView, InvestorUpdateView,Investorsignup, Inventorsignup,LogOutView,InventorOnly,InvestorOnly,InventionsDetail
from inventor import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('', views.allroutes, name="allroutes"),
    path('signup/inventors/', Inventorsignup.as_view()),
    path('signup/investors/', Investorsignup.as_view()),
    path('login/', CustomAuthToken.as_view(), name="auth_token"),
    path('logout/', LogOutView.as_view(), name="logout"),
    path('inventor-dash/', InventorOnly.as_view(), name="inventor-view"),
    path('investor-dash/', InvestorOnly.as_view(), name="investor-view"),
    path('investment-view/', AllInvestmentView.as_view(), name='all_investments'),#all investments
    path('all-inventions/', AllInventionsView.as_view(), name='all_inventions'),#all inventions view
    path('investor-update/<int:pk>/', InvestorUpdateView.as_view(), name='investor_update'),#update investor
    path('inventor-update/<int:pk>/', InventorUpdateView.as_view(), name='inventor_update'),#update inventor
    path('invention-detail/<int:pk>/', InventionsDetail.as_view(), name='trimmed_inventions')
    
] 
