import ollama
from ollama import ChatResponse, ListResponse


class OllamaService:
    def __init__(self):
        self.current_model = "deepseek-r1"

    def list_models(self) -> ListResponse:
        return ollama.list()

    def switch_model(self, model_name: str):
        pass

    def download_model(self, model_name: str):
        pass

    def chat(self, message: str):
        stream: ChatResponse = ollama.chat(
            model=self.current_model,
            messages=[
                {
                    # FIXME: hardcoded role
                    "role": "user",
                    "content": message,
                },
            ],
            stream=True,
        )

        for chunk in stream:
            print(chunk["message"]["content"], end="", flush=True)
