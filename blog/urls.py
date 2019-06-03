from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.post_list,name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^drafts/$',views.post_draft_list,name='post_draft_list'),
	path('post/<int:pk>/publish',views.post_publish,name='post_publish'),
	path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),

	path('post/<int:pk>/comment',views.add_comment_to_post,name='add_comment_to_post'),
	path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
	path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

	] 