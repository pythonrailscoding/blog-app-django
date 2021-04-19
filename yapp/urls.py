from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogUserListView, BlogReply, FeedBackUserList, BlogReplyCreateView, BlogCommentCreateView, FeedBackCreate, FeedBackList, NoteUserCreate, NoteUserList, NoteUserDetailView, NoteUserDeleteView, NoteUserUpdateView
from . import views

urlpatterns = [
    path('', BlogListView.as_view(), name="index"),
    path('user-list/', BlogUserListView.as_view(), name="user"),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name="detail"),
    path('create/', BlogCreateView.as_view(), name="create"),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name="delete"),
    path('detail/<int:pk>/comment', BlogCommentCreateView.as_view(), name="comment"),
    #path('register/', BlogUserCreateView.as_view(), name="register"),
    #path('login/', views.BlogUserLoginView, name="login"),
    #path('like/<int:pk>', LikeView, name='like_post'),
    path('serach', views.search, name='search'),
    path('search_user/user_post/', views.search_user, name='user_search'),
    path('feedback/', FeedBackList.as_view(), name='feedbacklist'),
    path('feedback/create', FeedBackCreate.as_view(), name='feedbackcreate'),
    path('feedback/current_user/', FeedBackUserList.as_view(), name='userfeed'),
    path('add/reply/<int:pk>', BlogReplyCreateView.as_view(), name='reply'),
    #path('view_reply/<int:pk>/', BlogReplyListView.as_view(), name='reply_list'),
    path('detail/<int:pk>', BlogReply.as_view(), name='reply_list'),
    path('search/', views.search_feedback, name='search_feed'),
    path('your/feedback/', views.BlogParticularUserFeed, name='specific_feed'),
    path('create/notes/', NoteUserCreate.as_view(), name='note_create'),
    path('list/notes/', NoteUserList.as_view(), name='note_list'),
    path('detail/notes/<int:pk>/', NoteUserDetailView.as_view(), name='note_detail'),
    path('delete/notes/<int:pk>/', NoteUserDeleteView.as_view(), name='note_delete'),
    path('update/notes/<int:pk>/', NoteUserUpdateView.as_view(), name='note_update'),
    path('search/notes/', views.NoteSearchListView, name='note_search'),
]
