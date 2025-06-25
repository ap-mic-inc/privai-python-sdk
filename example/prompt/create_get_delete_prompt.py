from privai import AuthenticatedClient
from privai.api.prompt.create_prompt import sync as create_prompt
from privai.api.prompt.auto_optimize_prompt import sync as auto_optimize_prompt
from privai.api.prompt.get_prompt import sync as get_prompt
from privai.api.prompt.delete_prompt import sync as delete_prompt
from privai.models.prompt_create import PromptCreate

def main():
    client = AuthenticatedClient(
        base_url="<privai-base-url>",
        token="<privai-token>"
    )

    prompt_body = PromptCreate(
        value="請以100字描述台灣文化特色",
        metadata=None
    )
    created = create_prompt(client=client, body=prompt_body)
    prompt_id = created.id
    print(f"已建立 Prompt，ID: {prompt_id}")

    optimized = auto_optimize_prompt(
        prompt_id=prompt_id,
        client=client
    )
    print(f"優化後內容: {optimized.value}")

    fetched = get_prompt(
        prompt_id=prompt_id,
        client=client
    )
    print(f"Prompt 最終內容: {fetched.value}（建立於 {fetched.created_at}）")

    result = delete_prompt(
        prompt_id=prompt_id,
        client=client
    )
    print(f"刪除結果: {result}")

if __name__ == "__main__":
    main()
