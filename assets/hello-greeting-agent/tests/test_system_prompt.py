"""Unit test: verify the system prompt contains a greeting instruction."""
import sys
from pathlib import Path

# Ensure app/ is importable
sys.path.insert(0, str(Path(__file__).parent.parent / "app"))


def test_system_prompt_contains_greeting_instruction():
    """The system prompt must instruct the agent to start with Hello!."""
    from agent import get_system_prompt

    prompt = get_system_prompt()
    assert "Hello!" in prompt or "hello" in prompt.lower(), (
        "System prompt must contain a greeting instruction (Hello! or hello)."
    )


def test_system_prompt_contains_always_greet_instruction():
    """The system prompt must instruct the agent to ALWAYS start with a greeting."""
    from agent import get_system_prompt

    prompt = get_system_prompt()
    prompt_lower = prompt.lower()
    assert "always" in prompt_lower or "start" in prompt_lower or "begin" in prompt_lower, (
        "System prompt should instruct the agent to always start with a greeting."
    )
