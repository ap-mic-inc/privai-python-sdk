from privai import AuthenticatedClient
from privai.api.filesets.create_fileset import sync as create_fileset
from privai.api.filesets.update_fileset import sync as update_fileset
from privai.api.filesets.get_fileset import sync as get_fileset
from privai.api.filesets.delete_fileset import sync as delete_fileset
from privai.models.fileset_create import FilesetCreate
from privai.models.fileset_update import FilesetUpdate
import uuid
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="PrivAI Fileset Flow: Create → Update → Commit → Get → Delete"
    )
    parser.add_argument(
        "--project", required=True,
        help="Metadata project name"
    )
    parser.add_argument(
        "--owner", required=True,
        help="Metadata owner"
    )
    parser.add_argument(
        "--file-ids", required=True,
        help="Comma-separated list of file UUIDs"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # 解析輸入的 file IDs
    file_ids = [uuid.UUID(fid.strip()) for fid in args.file_ids.split(",")]

    # 建立已驗證的 API Client
    client = AuthenticatedClient(
        base_url="<privai-base-url>",
        token="<privai-token>"
    )

    # Flow 1: Create → Update → Commit → Get → Delete
    # 1. Create Fileset
    create_body = FilesetCreate(
        id=None,
        metadata={"project": args.project, "owner": args.owner},
        file_ids=file_ids,
    )
    fs = create_fileset(client=client, body=create_body)
    fs_id = fs.id
    print(f"已建立 fileset，ID = {fs_id}")

    # # 2. Update Fileset
    # update_body = FilesetUpdate(
    #     metadata={"owner": f"{args.owner}-updated"},
    #     file_ids=None,
    # )
    # updated_fs = update_fileset(filesets_id=fs_id, client=client, body=update_body)
    # print(f"已更新 metadata = {updated_fs.metadata}")

    # 4. Get Fileset
    fs_get = get_fileset(filesets_id=fs_id, client=client)
    print(f"取得 fileset：{fs_get}")

    # 5. Delete Fileset
    del_resp = delete_fileset(filesets_id=fs_id, client=client)
    print(f"刪除結果：{del_resp.detail}")

if __name__ == "__main__":
    main()

# Example usage:
# python create_update_commit_get_delete_fileset.py \
#   --project test-sdk \
#   --owner team-sdk \
#   --file-ids 11111111-2222-3333-4444-555555555555,66666666-7777-8888-9999-000000000000
