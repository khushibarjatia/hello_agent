# Specification: hello-greeting-agent

> **Guidelines**: Read all applicable guidelines before executing ANY tasks below:
> - [guidelines.md](../guidelines.md) — Universal execution rules
> - [guidelines-agent.md](../guidelines-agent.md) — Universal agent patterns
> - [guidelines-agent-python.md](../guidelines-agent-python.md) — Python implementation details
> - [guidelines-agent-skills.md](../guidelines-agent-skills.md) — Runtime skills patterns
> - [guidelines-agent-mcp.md](../guidelines-agent-mcp.md) — MCP integration patterns

---

## Basic Setup

- [x] Read the project input (`product-requirements-document.md`, `intent.md`)
- [x] Bootstrap agent code in `assets/hello-greeting-agent/` using instructions from the sap-agent-bootstrap section (invoke from inside `assets/hello-greeting-agent/`, use copy commands — do NOT create files manually)
- [x] Install dependencies, validate the agent starts and responds at `/.well-known/agent.json`

---

## Runtime Skills

No runtime skills are needed for this agent — the greeting behaviour is simple enough to be handled entirely in the system prompt.

---

## Project-Specific Tasks

### Greeting Behaviour

- [x] Open `assets/hello-greeting-agent/app/agent.py` and update the system prompt (inside `get_system_prompt()`) to instruct the agent to greet every user with "Hello!" at the start of every response, regardless of the message content
- [x] Ensure the system prompt explicitly states: "Always start your response with 'Hello!' to greet the user warmly and consistently."
- [x] Verify the agent name and description in `/.well-known/agent.json` reflect the greeting agent purpose (e.g. name: "Hello Greeting Agent", description: "An AI agent that greets every user with hello.")

### Consistent Friendly Tone

- [x] Update the system prompt to instruct the agent to maintain a friendly, welcoming tone in all responses
- [x] Add a guardrail instruction: "If you cannot fulfil a request, still start with a greeting before explaining any limitations."

---

## Business Instrumentation

- [x] Implement business step instrumentation for each milestone from the PRD:
  - **M1 (Agent Bootstrapped)**: emit `M1.achieved: agent bootstrapped and accepting messages` on successful startup; emit `M1.missed: agent failed to start or is not accepting messages` on failure
  - **M2 (Greeting Behaviour Verified)**: emit `M2.achieved: greeting behaviour verified across all test cases` when greeting is confirmed in response; emit `M2.missed: one or more test cases did not receive a greeting` when greeting is absent
  - **M3 (Deployment Ready)**: emit `M3.achieved: agent deployed and reachable on SAP BTP` on successful deployment readiness; emit `M3.missed: deployment failed or agent is not reachable` on failure
- [x] Use OpenTelemetry custom spans for each milestone — use the **decorator form** on regular async methods or the **context manager form** inside non-generator async functions. NEVER use `with tracer.start_as_current_span(...)` inside an async generator
- [x] Extract greeting business logic from `stream()` into a plain async helper method (e.g. `_run_agent()`) and instrument that method, then call it from `stream()` and yield the result outside any span context
- [x] Verify `bootstrap(app)` is called after `app = server.build()` in `main.py`

---

## MCP Tool Integration

No SAP API integrations are required for this agent. Skip all MCP tool integration tasks (no `api-specs/`, no `mcp-specs/`, no translation files, no mock config needed).

---

## Testing

- [x] `conftest.py` only sets `IBD_TESTING=true`
- [x] Write one integration test in `assets/hello-greeting-agent/tests/` that:
  - Mocks the LLM to return a canned response that starts with "Hello!"
  - Calls the agent's `invoke` function with a sample user message
  - Asserts the response contains a greeting ("hello" case-insensitive)
- [x] Write one unit test that verifies the system prompt contains the greeting instruction
- [x] Run `pytest` from `assets/hello-greeting-agent/` (no args) — coverage is 76% (above 70% threshold)
- [x] Run `pytest` again from `assets/hello-greeting-agent/` (no args) to generate final `test_report.json`
- [x] Verify `test_report.json` exists in `assets/hello-greeting-agent/`
