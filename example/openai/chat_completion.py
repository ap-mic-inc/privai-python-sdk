from privai import AuthenticatedClient
from privai.api.openai.chat_completions import sync
from privai.models import ChatRequest, Message, MessageRole

def main():
    # 建立已驗證的 API Client
    client = AuthenticatedClient(
        base_url="<privai-base-url>",
        token="<privai-token>"
    )

    # 將所有請求欄位封裝到 ChatRequest (或 dict) 中
    request_body = ChatRequest(
        model="azure-gpt-4o",
        messages=[
            Message(role=MessageRole.USER, content="請問資安法第一條內容？")
        ],
        stream=False,
        search_kwargs={          # 這裡可以直接給 dict，SDK 會自動轉成 ChatRequestSearchKwargsType0
            "search_type": "similarity",
            "k": 3
        },
        prompt_id="<prompt-id>",  # 如果有使用 Prompt ID
        fileset_id="<fileset-id>",  # 如果有指定 Fileset ID
        temperature=0
    )

    full_response = sync(client=client, body=request_body)

    # 假設 full_response 是 dict
    answer = full_response["choices"][0]["message"]["content"]
    print("Answer: \n\n" + answer)

if __name__ == "__main__":
    main()
