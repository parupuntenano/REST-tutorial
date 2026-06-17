from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.decorators import api_view


# GETとPOSTを受け付けるAPI
@api_view(["GET", "POST"])
def snippet_list(request, format=None):

    # 一覧取得
    if request.method == "GET":

        # DBから全Snippetを取得
        snippets = Snippet.objects.all()

        # 複数件なので many=True
        serializer = SnippetSerializer(
            snippets,
            many=True
        )

        # JSONレスポンス返却
        return Response(serializer.data)

    # 新規作成
    elif request.method == "POST":

        # リクエストデータをSerializerへ渡す
        serializer = SnippetSerializer(
            data=request.data
        )

        # バリデーション
        if serializer.is_valid():

            # DB保存
            serializer.save()

            # 作成成功(201)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        # 入力エラー(400)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# GET・PUT・DELETEを受け付けるAPI
@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk, format=None):

    # 指定されたpkのSnippetを1件取得
    try:
        snippet = Snippet.objects.get(pk=pk)

    # 見つからなければ404
    except Snippet.DoesNotExist:
        raise Http404

    # 1件取得
    if request.method == "GET":

        # 1件なので many=True は不要
        serializer = SnippetSerializer(snippet)

        # JSONレスポンス返却
        return Response(serializer.data)

    # 更新
    elif request.method == "PUT":

        # 更新対象snippetをrequest.dataの内容で更新する準備
        serializer = SnippetSerializer(
            snippet,
            data=request.data
        )

        # バリデーション
        if serializer.is_valid():

            # DB更新
            serializer.save()

            # 更新後データを返却
            return Response(serializer.data)

        # 入力エラー
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # 削除
    elif request.method == "DELETE":

        # DBから削除
        snippet.delete()

        # 削除成功。返す中身はなし
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )