# -*- coding: utf-8 -*-
import pandas as pd
from privai import AuthenticatedClient
from privai.api.files import list_files

def main():
    # 建立已驗證的 API Client
    client = AuthenticatedClient(
        base_url="<privai-base-url>",
        token="<privai-token>"
    )

    # 列出所有檔案（Files）並存成 CSV
    files_result = list_files.sync(client=client)
    files_records = [item.to_dict() for item in files_result.data]
    files_df = pd.DataFrame.from_records(files_records)
    files_df.to_csv("./result/privai_files.csv", index=False, encoding="utf-8-sig")
    print("已儲存檔案清單至 privai_files.csv")

if __name__ == "__main__":
    main()
