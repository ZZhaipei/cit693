from django.urls import path

from .views import ServerListView, ServerAddView, ServerDetailView, ServerModifyView, ServerDeleteView, ServerExportView
from .views import TypeListView, TypeAddView, TypeDetailView, TypeModifyView

urlpatterns = [
    # 资产url
    path('server/list/', ServerListView.as_view(), name='server_list'),                       #资产列表
    path('server/add/', ServerAddView.as_view(), name='server_add'),                          #资产添加
    path('server/detail/<int:server_id>/', ServerDetailView.as_view(), name='server_detail'), #资产详情
    path('server/modify/', ServerModifyView.as_view(), name='server_modify'),                 #资产详情修改
    path('server/delete/<int:server_id>/', ServerDeleteView.as_view(), name='server_delete'), #资产记录删除
    path('server/export/', ServerExportView.as_view(), name='server_export'),

    # 资产类型url
    path('type/list/', TypeListView.as_view(), name='type_list'),                     #资产类型列表
    path('type/add/', TypeAddView.as_view(), name='type_add'),                        #资产类型添加
    path('type/detail/<int:type_id>/', TypeDetailView.as_view(), name='type_detail'), #资产类型详情
    path('type/modify/', TypeModifyView.as_view(), name='type_modify')                #资产类型修改
]
