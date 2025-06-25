# -*- coding: utf-8 -*-
import os
from privai import AuthenticatedClient
from privai.api.files import create_file, delete_file, get_file
from privai.models.body_create_file_v1_files_post import BodyCreateFileV1FilesPost
from privai.types import File
from privai.models.file_resp import FileResp
from privai.models.http_validation_error import HTTPValidationError

def main():
    client = AuthenticatedClient(
        base_url="<privai-base-url>",
        token="<privai-token>"
    )

    file_path = "./file/test.pdf"
    filename = os.path.basename(file_path)

    with open(file_path, "rb") as fp:
        upload_file = File(
            payload=fp,
            file_name=filename,
            mime_type="application/pdf",
        )
        body = BodyCreateFileV1FilesPost(file=upload_file)
        result = create_file.sync(
            client=client,
            body=body,
            purpose="user_data",
        )

    if isinstance(result, FileResp):
        print(f"上傳成功，檔案 ID：{result.id}")
    elif isinstance(result, HTTPValidationError):
        print("驗證錯誤：", result.json())
    else:
        print("發生未預期錯誤。")

    # 獲取檔案示範
    file_id = result.id if isinstance(result, FileResp) else None
    if file_id:
        file_info = get_file.sync(client=client, file_id=file_id)
        if isinstance(file_info, FileResp):
            print(f"檔案資訊：ID={file_info.id}, 名稱={file_info.filename}, 目的={file_info.purpose}, 創建時間={file_info.created_at}")
        else:
            print("獲取檔案資訊失敗。")

    # 刪除示範
    if isinstance(result, FileResp):
        del_res = delete_file.sync(client=client, file_id=result.id)
        print("刪除結果：", "成功" if del_res.deleted else f"失敗，{del_res.error_message}")

if __name__ == "__main__":
    main()
