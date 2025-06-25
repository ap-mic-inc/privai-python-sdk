import os
from uuid import UUID
from privai import AuthenticatedClient
from privai.api.qa.generate_qa import sync as generate_qa
from privai.api.files.download_file import sync as download_file
from privai.models.generate_qa_req import GenerateQaReq
from privai.models.file_resp import FileResp
from privai.models.http_validation_error import HTTPValidationError


def main():
    # 建立已驗證的 API Client
    client = AuthenticatedClient(
        base_url="<privai-base-url>",
        token="<privai-token>"
    )

    # 已上傳檔案的 fileset ID
    fileset_id = UUID("<uuid>")

    # 建立 Generate QA 請求
    request = GenerateQaReq(
        model_name="azure-gpt-4o",
        extract_model_name="azure-gpt-4o",
        temperature=0.7,
        target_amount=1
    )

    # 呼叫 API 產生 QA，回傳檔案資訊
    response = generate_qa(
        client=client,
        body=request,
        fileset_id=fileset_id
    )

    # 處理回應
    if isinstance(response, FileResp):
        print(response)
        print(f"檔案已建立: {response.filename} (ID: {response.id})")

        # 下載檔案內容
        file_content = download_file(
            file_id=response.id,
            client=client
        )

        # 檢查下載結果
        if file_content is None:
            print("下載失敗：未收到檔案內容。")
        elif isinstance(file_content, HTTPValidationError):
            print("下載失敗：", file_content)
        else:
            # 確保結果資料夾存在
            output_dir = "./result"
            os.makedirs(output_dir, exist_ok=True)
            # 組合檔案輸出路徑
            output_path = os.path.join(output_dir, response.filename)
            # 將檔案寫入指定資料夾
            with open(output_path, "wb") as f:
                f.write(file_content)
            print(f"檔案已下載至 {output_path}")
    else:
        # API 呼叫失敗時，印出錯誤
        print("API 產生失敗：", response)


if __name__ == "__main__":
    main()
