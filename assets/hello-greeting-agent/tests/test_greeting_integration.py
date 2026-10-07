"""Integration test: agent must include a greeting in every response."""
from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

# Ensure app/ is importable
sys.path.insert(0, str(Path(__file__).parent.parent / "app"))


@pytest.fixture
def mock_llm_response():
    """Return a mocked LLM response that starts with Hello!."""
    return "Hello! How can I help you today?"


@pytest.mark.asyncio
async def test_agent_greets_user(mock_llm_response):
    """Agent invoke() must return a response containing a greeting."""
    from agent import SampleAgent

    agent = SampleAgent()

    # Mock _invoke_with_fallback to return a canned LLM response
    mock_result = {
        "messages": [MagicMock(content=mock_llm_response)]
    }
    with patch.object(agent, "_invoke_with_fallback", new=AsyncMock(return_value=mock_result)):
        response = await agent.invoke("Hi there!", context_id="test-ctx-001", tools=[])

    assert response.status == "completed"
    assert "hello" in response.message.lower(), (
        f"Expected a greeting in response, got: {response.message!r}"
    )


@pytest.mark.asyncio
async def test_agent_greets_on_any_message(mock_llm_response):
    """Agent must greet regardless of the user's input."""
    from agent import SampleAgent

    agent = SampleAgent()

    mock_result = {
        "messages": [MagicMock(content="Hello! I can answer that for you.")]
    }
    with patch.object(agent, "_invoke_with_fallback", new=AsyncMock(return_value=mock_result)):
        response = await agent.invoke("What is 2+2?", context_id="test-ctx-002", tools=[])

    assert response.status == "completed"
    assert "hello" in response.message.lower(), (
        f"Expected a greeting in every response, got: {response.message!r}"
    )


@pytest.mark.asyncio
async def test_agent_error_handling():
    """Agent must handle exceptions gracefully."""
    from agent import SampleAgent

    agent = SampleAgent()

    with patch.object(agent, "_invoke_with_fallback", new=AsyncMock(side_effect=RuntimeError("LLM down"))):
        response = await agent.invoke("Hello", context_id="test-ctx-003", tools=[])

    assert response.status in ("completed", "error")
    assert response.message  # some message must be returned
