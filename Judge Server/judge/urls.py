from django.urls import path
# from .views import problem
from .views import ProblemListView
from . import views

urlpatterns = [
    path('',views.judge,name='judge'),
    
    path('problems/',ProblemListView.as_view(),name='problem'),
    path('problems/order/',views.orderproblem,name='order'),
    path('problems/get_data',views.get_data,name='get-data'),
    path('problems/filter_tags/',views.filter_tags,name='filter_tags'),
    path('problems/filter_difficulty/<str:diff>/',views.filter_difficulty,name='filter-difficulty'),
    path('ide/',views.ide,name='ide'),
    path('ide/runcode/',views.runcode,name='runcode'),
    path('addproblem/',views.addproblem,name='addproblem'),
    path('addproblem/save/',views.save,name='save'),
    path('detail/<int:pid>/',views.detail,name='detail'),
    path('detail/<int:pid>/submit/',views.submit,name='submit'),
    path('detail/<int:pid>/submit/viafile/',views.viafile,name='viafile'),
    path('detail/<int:pid>/submit/viacode/',views.viacode,name='viacode')
]