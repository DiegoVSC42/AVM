
import re
from typing import List

def clean_text(text: str) -> str:
    # Limpeza simples para reduzir quebras e espaços
    text = text.replace('\r', ' ').replace('\n', ' ')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def pretty_sources(sources: List[str]) -> str:
    if not sources:
        return ""
    return "\n".join(f"- {s}" for s in sources)
