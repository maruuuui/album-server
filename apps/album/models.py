from django.db import models
import uuid
from datetime import date
from django.db.models.signals import post_delete
from django.dispatch import receiver


def get_upload_path(instance, filename):
    """画像のアップロード先をアップロード時刻から決定する関数"""
    uploaded_at = date.today()
    file_dir_path = uploaded_at.strftime("%Y/%m/%d")
    image_uuid = instance.id
    return file_dir_path + "/" + str(image_uuid) + "/" + filename


class Image(models.Model):
    """アップロードされた画像"""

    id: models.UUIDField = models.UUIDField(
        "主キー", primary_key=True, editable=False, default=uuid.uuid4, help_text="主キー"
    )
    image: models.ImageField = models.ImageField(
        "画像ファイル", upload_to=get_upload_path, help_text="画像ファイル"
    )
    memo: models.CharField = models.CharField(max_length=255, blank=True, null=True)

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.name


# Imageモデル削除後に`image`を削除する。
@receiver(post_delete, sender=Image)
def delete_file(sender, instance, **kwargs):
    instance.image.delete(False)
