# 1. URLを定義するためのpathを読み込む
from django.urls import path, include

# 2. format suffix を使うために読み込む
#    /snippets.json のようなURLを使えるようにする
from rest_framework.urlpatterns import format_suffix_patterns

# 3. 同じアプリ内のviews.pyを読み込む
from snippets import views
# ① Routerを使うため
from rest_framework.routers import DefaultRouter


# 4. URLとViewを結びつける
router = DefaultRouter()
router.register(r"snippets", views.SnippetViewSet, basename="snippet")
router.register(r"users", views.UserViewSet, basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]