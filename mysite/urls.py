from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path,include
from django.conf.urls import url
from mysite.core import views


urlpatterns = [
    path('',views.home,name='home'),
    path('json/',views.json,name='json'),
    path('signup/',views.signup,name='signup'),
    path('create_blog/',views.create_blog,name='create_blog'),
    path('list_blog/', views.list_blog,name='list_blog' ),
    path('update_blog/<int:id>/',views.update_blog,name='update_blog'),
    path('delete_blog/<int:id>/',views.delete_blog,name='delete_blog'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
