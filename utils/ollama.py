import subprocess

def generate_text_with_ollama(prompt: str) -> str:
    """
    Calls Ollama CLI LLM to generate text from prompt.
    Returns the generated text as string.
    """
    result = subprocess.run(
        ['ollama', 'run', 'llama3.2', prompt],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()
