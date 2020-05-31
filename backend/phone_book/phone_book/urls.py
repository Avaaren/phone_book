from django.contrib import admin
from django.urls import path, incldue

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', incldue('book.urls'))
]
