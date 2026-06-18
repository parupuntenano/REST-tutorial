# 1. URLを定義するためのpathを読み込む
from django.urls import path

# 2. format suffix を使うために読み込む
#    /snippets.json のようなURLを使えるようにする
from rest_framework.urlpatterns import format_suffix_patterns

# 3. 同じアプリ内のviews.pyを読み込む
from snippets import views


# 4. URLとViewを結びつける
urlpatterns = [
    # 5. /snippets/ にアクセスされたとき
    #    SnippetListクラスをViewとして実行する
    path("snippets/",views.SnippetList.as_view()),
    # 6. /snippets/1/ のようにアクセスされたとき
    #    SnippetDetailクラスをViewとして実行する
    #    <int:pk> の pk が views.py の get(self, request, pk, ...) に渡る
    path("snippets/<int:pk>/",views.SnippetDetail.as_view()),
]
# 7. /snippets.json や /snippets/1.json を使えるようにする
urlpatterns = format_suffix_patterns(urlpatterns)