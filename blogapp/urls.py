from django.urls import path
from .views import *


urlpatterns = [
    path( '', HomeView.as_view(), name='home' ),
    path( 'post/<slug:post_url>/', SinglePostView.as_view(), name='single_post' ),
    path( 'category/<slug:category_url>/', get_blog_by_category, name='single_category' ),
    # path( 'category/<slug:category_url>/', SingleCategoryView.as_view(), name='single_category' ),
    path('sign-up/', sign_up, name='sign-up'),   
    path('sign-in/', sign_in, name='sign-in'),   
    path('sign-out/', sign_out, name='sign-out'),   
    path('account/', Account, name='account'),   
    #essential pages
    path( 'about/', AboutView.as_view(), name='about' ),
    path( 'contact/', ContactView.as_view(), name='contact' ),
    path( 'disclaimer/', DisclaimerView.as_view(), name='disclaimer' ),
    path( 'terms-conditions/', TCView.as_view(), name='termsconditions' ),

]

