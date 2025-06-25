from uuid import UUID
from http import HTTPStatus

from privai import AuthenticatedClient
from privai.api.files import download_file
from privai.models.file_type import FileType
from privai.models.http_validation_error import HTTPValidationError


def download_file_sync():
    # 1. 初始化已驗證的 API Client
    client = AuthenticatedClient(
        base_url="<privai-base-url>",
        token="<privai-token>",
    )

    # 2. 指定欲下載的檔案 ID 與格式
    file_id = UUID("<uuid>")
    file_type = FileType.RAW_FILE  # 或 FileType.OTHER_FORMAT

    # 3. 呼叫同步介面，取得完整 Response 物件
    response = download_file.sync_detailed(
        file_id=file_id,
        client=client,
        file_type=file_type,
    )

    # 4. 根據 HTTP 狀態碼與回傳內容做處理
    if response.status_code == HTTPStatus.OK:
        # response.content 是 bytes，直接寫入檔案
        output_path = "./result/downloaded_file.pdf"
        with open(output_path, "wb") as fp:
            fp.write(response.content)
        print(f"檔案下載成功：{output_path}")
    elif isinstance(response.parsed, HTTPValidationError):
        # 處理 422 驗證錯誤
        print("參數驗證失敗：", response.parsed.json())
    else:
        # 預期外的錯誤
        print(f"下載失敗，HTTP {response.status_code}：{response.content}")


async def download_file_async():
    # 1. 初始化已驗證的 API Client（非同步）
    client = AuthenticatedClient(
        base_url="<privai-base-url>",
        token="<privai-token>",
    )

    file_id = UUID("<uuid>")
    file_type = FileType.RAW_FILE

    # 2. 呼叫非同步介面
    response = await download_file.asyncio_detailed(
        file_id=file_id,
        client=client,
        file_type=file_type,
    )

    # 3. 同樣依狀態碼處理
    if response.status_code == HTTPStatus.OK:
        output_path = "./result/downloaded_file_async.pdf"
        with open(output_path, "wb") as fp:
            fp.write(response.content)
        print(f"[Async] 檔案下載成功：{output_path}")
    elif isinstance(response.parsed, HTTPValidationError):
        print("[Async] 參數驗證失敗：", response.parsed.json())
    else:
        print(f"[Async] 下載失敗，HTTP {response.status_code}：{response.content}")


if __name__ == "__main__":
    # 執行同步下載
    download_file_sync()

    # 若要執行非同步下載，可解除下列註解
    # import asyncio
    # asyncio.run(download_file_async())
