from ollama_client.ollama_service import OllamaService


def main() -> None:
    client = OllamaService()

    print(client.list_models())
