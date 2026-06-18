from rest_framework import renderers, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import IsOwnerOrReadOnly


# ① Snippet用ViewSet
# GET /snippets/
# POST /snippets/
# GET /snippets/{id}/
# PUT/PATCH /snippets/{id}/
# DELETE /snippets/{id}/
class SnippetViewSet(viewsets.ModelViewSet):

    # ② 操作対象のデータ
    queryset = Snippet.objects.all()

    # ③ 使用するSerializer
    serializer_class = SnippetSerializer

    # ④ 認証・所有者権限
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    # ⑤ /snippets/{id}/highlight/ を追加する
    @action(
        detail=True,
        renderer_classes=[renderers.StaticHTMLRenderer]
    )
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    # ⑥ POST時にownerを自動設定する
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# ⑦ User用ViewSet
# GET /users/
# GET /users/{id}/
class UserViewSet(viewsets.ReadOnlyModelViewSet):

    # ⑧ 操作対象のデータ
    queryset = User.objects.all()

    # ⑨ 使用するSerializer
    serializer_class = UserSerializer