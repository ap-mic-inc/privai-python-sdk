# PrivAI Python SDK

## 專案概述

`privai-python-sdk` 是由 OpenAPI Generator 自動產出的 Python 客戶端函式庫，可協助開發者透過 Lance API 進行檔案管理、Prompt 最佳化與問答生成等操作。設計上兼顧同步與非同步使用場景。

## 功能特色

* **同步/非同步** API 呼叫支援
* **檔案管理**：上傳、下載、查詢、刪除
* **Prompt 自動化**：建議最佳化與自訂優化
* **問答生成（QA）**：基於 API 回傳產出問題與回答
* **連線設定**：自訂標頭、Cookie、憑證驗證、超時、重試等參數
* **輕量依賴**：`httpx`、`attrs`、`python-dateutil`

## 安裝方式

```bash
git clone https://github.com/ap-mic-inc/privai-python-sdk.git
python setup.py sdist bdist_wheel
pip install ./dist/privai-<VERSION>-py3-none-any.whl
```

## 基本用法

### 建立認證客戶端

```python
from privai import AuthenticatedClient

  # 建立已驗證的 API Client
  client = AuthenticatedClient(
      base_url="<privai-base-url>",
      token="<privai-token>"
  )
```

### 範例

> 詳細使用方法，可見 [example](./example/) 資料夾。

```python
# 列出所有檔案
from privai.api.files.list_files import sync as list_files

response = list_files(client=client)
print(response)
```

## 授權條款

本專案採用 MIT License，詳見 [LICENSE](LICENSE)。
