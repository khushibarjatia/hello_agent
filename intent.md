# Hello Greeting Agent

Simple AI conversational agent that greets users with "hello" in every interaction.

## Business challenge

Users need a conversational AI agent that reliably greets them at the start of every interaction, improving engagement and ensuring a consistent, friendly experience.

## Business Goals & Success Criteria

| Metric | Baseline | Target | Timeline | Process / Capability | Source |
|--------|----------|--------|----------|----------------------|--------|
| Greeting coverage per user interaction | — | 100% of interactions start with a greeting | — | User Engagement / Conversational Interface | user |
| User engagement / satisfaction | — | Improved (qualitative) | — | User Engagement / Conversational Interface | user |

## Key Milestones

1. **Agent bootstrapped** — Python A2A agent project is created and runs locally.
2. **Greeting behaviour verified** — Agent responds with "hello" on every new conversation turn.
3. **Deployment ready** — Agent is packaged, tested, and deployed to SAP BTP.

## Business Architecture (RBA)

### End-to-End Process

Lead to Cash (E2E)

### Process Hierarchy

```
Lead to Cash (E2E)
└── Manage Customers and Channels (generic)
    └── Manage and operate sales channels (generic) (BPS-371)
        └── Operate omnichannel customer platforms
```

### Summary

The greeting agent maps to the "Manage and Operate Sales Channels" sub-process within Lead to Cash, covering the need to engage and interact with users across channels via a conversational interface.

## Fit Gap Analysis

| Requirement (business) | Standard asset(s) found | API ORD ID | MCP Server ORD ID | MCP Server Version | Webhook API ORD ID | Data Product ORD ID | Gap? | Notes / assumptions |
|------------------------|------------------------|------------|-------------------|--------------------|--------------------|---------------------|------|---------------------|
| Greet user on every interaction | None directly applicable | — | — | — | — | — | Yes | Requires custom AI agent; standard SAP products (Commerce Cloud, S/4HANA) do not cover this conversational greeting use case |

### Key findings

- No standard SAP product directly covers a simple greeting agent use case.
- A custom pro-code Python AI agent (A2A protocol) is the appropriate approach.
- The agent requires no external MCP tool integrations for its core greeting behaviour.
- SAP BTP is the target runtime platform.
- The solution is intentionally minimal and can be extended with additional capabilities later.

## Recommendations

### Hello Greeting AI Agent

#### Executive Summary

Custom Python A2A agent deployed on SAP BTP that greets every user.

#### Recommended Solution

A pro-code Python agent built using the A2A protocol, hosted on SAP BTP. The agent greets every user with "hello" at the start of each conversation turn. It includes OpenTelemetry instrumentation and a test suite.

#### Recommended solution category

AI Agent

#### Intent fit
95%
