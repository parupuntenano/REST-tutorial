# ① DRFのPermission基底クラスを使う
from rest_framework import permissions


# ② 作成者本人だけ編集可能にする権限
class IsOwnerOrReadOnly(
    permissions.BasePermission
):

    # ③ オブジェクト単位の権限チェック
    def has_object_permission(
        self,
        request,
        view,
        obj
    ):

        # ④ GET/HEAD/OPTIONS は誰でも許可
        if request.method in permissions.SAFE_METHODS:
            return True

        # ⑤ PUT/PATCH/DELETE は owner のみ許可
        return obj.owner == request.user