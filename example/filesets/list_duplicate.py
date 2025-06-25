from privai import AuthenticatedClient
from privai.api.filesets.list_filesets import sync as list_filesets
from privai.api.filesets.duplicate_fileset import sync as duplicate_fileset

def main():
    # 建立已驗證的 API Client
    client = AuthenticatedClient(
        base_url="<privai-base-url>",
        token="<privai-token>"
    )

    # Flow 2: List → Duplicate → List
    # 1. List Filesets（第一次）
    list_resp1 = list_filesets(client=client, limit=10)
    ids = [item.id for item in list_resp1.data]
    print(f"目前 fileset 清單：{ids}")
    print("====")

    if not ids:
        print("目前無可複製的 fileset，流程結束。")
        return

    # 2. Duplicate 第一筆 Fileset
    source_id = ids[0]
    dup_id = duplicate_fileset(fileset_id=source_id, client=client)
    print(f"複製 {source_id} → 新 ID = {dup_id}")
    print("====")

    # 3. List Filesets（第二次）
    list_resp2 = list_filesets(client=client, limit=10)
    ids_after = [item.id for item in list_resp2.data]
    print(f"複製後 fileset 清單：{ids_after}")
    print("====")

if __name__ == "__main__":
    main()
