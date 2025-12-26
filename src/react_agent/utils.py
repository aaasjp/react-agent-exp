"""Utility & helper functions."""

from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI


def get_message_text(msg: BaseMessage) -> str:
    """Get the text content of a message."""
    content = msg.content
    if isinstance(content, str):
        return content
    elif isinstance(content, dict):
        return content.get("text", "")
    else:
        txts = [c if isinstance(c, str) else (c.get("text") or "") for c in content]
        return "".join(txts).strip()


def load_chat_model(fully_specified_name: str) -> BaseChatModel:
    """Load a chat model from a fully specified name.

    Args:
        fully_specified_name (str): String in the format 'provider/model'.
    """

    """
    provider, model = fully_specified_name.split("/", maxsplit=1)
    return init_chat_model(model, model_provider=provider)
    """
    model = ChatOpenAI(
        model="qwen3-235b-a22b",  # Specify a model available on OpenRouter
        api_key="sk-IrTGDWBvflR3iKCr127449E60119437589937d077bE3B31b",
        base_url="https://mgallery.haier.net/v1",
        #extra_body={"reasoning": {"enabled": False}}
        extra_body={"chat_template_kwargs": {"enable_thinking": False}}
    )
    return model