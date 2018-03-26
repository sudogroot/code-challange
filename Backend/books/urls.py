from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = [
    url(r'^books/$', views.BookList.as_view(), name='all-books'),
    url(r'^books/(?P<isbn>[^/]+)/$', views.BookDetails.as_view(), name='book-details'),
    url(r'^books/(?P<isbn>[^/]+)/comments/$', views.CommentsPost.as_view(), name='book-comment'),
    url(r'^books/(?P<isbn>[^/]+)/stars/$', views.StarsPost.as_view(), name='book-stars'),
    url(r'^user/books/$', views.UserBooks.as_view(), name='user-books'),
    url(r'^user/activities/comments/$', views.UserComments.as_view(), name='user-comments'),
    url(r'^user/activities/stars/$', views.UserStars.as_view(), name='user-stars'),
    url(r'^user/$', views.User.as_view(), name='user'),
    url(r'^user/reviews/comments/$', views.CommentsReviews.as_view(), name='log-comments'),
    url(r'^user/reviews/stars/$', views.StarsReviews.as_view(), name='log-stars'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
