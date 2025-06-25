#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from privai import AuthenticatedClient
from privai.api.prompt.list_prompts import sync as list_prompts

def export_prompts_to_csv(output_path: str = "./result/privai_prompts.csv"):
    """
    依 limit 參數分頁讀取 Prompt，轉成 DataFrame 後匯出 CSV。
    """
    # 1. 建立已驗證的 API Client
    client = AuthenticatedClient(
        base_url="<privai-base-url>",
        token="<privai-token>"
    )

    # 2. 列出 Prompt（此處一次最多抓 100 筆，可搭配 after/before 分頁）
    response = list_prompts(client=client, limit=100)
    if not hasattr(response, "data"):
        raise RuntimeError(f"列出提示詞失敗: {response}")

    # 3. 轉為 DataFrame
    records = [item.to_dict() for item in response.data]
    df = pd.DataFrame(records)

    # 4. 匯出為 CSV（UTF-8 with BOM，方便 Excel 開啟）
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"已將 {len(df)} 筆 Prompt 匯出至 {output_path}")

def main():
    # 未來可導入 argparse 以接收 CLI 參數，例如 --output
    export_prompts_to_csv()

if __name__ == "__main__":
    main()
