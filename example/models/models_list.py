# -*- coding: utf-8 -*-
import pandas as pd
from privai import AuthenticatedClient
from privai.api.models import get_models

def main():
    # 建立已驗證的 API Client
    client = AuthenticatedClient(
        base_url="<privai-base-url>",
        token="<privai-token>"
    )

    # 取得所有模型（Models）並存成 CSV
    models_result = get_models.sync(client=client)
    models_records = [item.to_dict() for item in models_result.data]
    models_df = pd.DataFrame.from_records(models_records)
    models_df.to_csv("./result/privai_models.csv", index=False, encoding="utf-8-sig")
    print("已儲存模型清單至 privai_models.csv")

if __name__ == "__main__":
    main()
