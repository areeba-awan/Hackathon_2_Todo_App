---
id: 001
title: Create Global Constitution
stage: constitution
date: 2026-01-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: human
command: /sp.constitution Create a single global constitution for the entire "Evolution of Todo" project covering Phase I through Phase V
labels: [constitution, governance, project-rules]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - none
---

## Prompt

/sp.constitution Create a single global constitution for the entire "Evolution of Todo" project covering Phase I through Phase V.

This constitution must define:

1. Spec-Driven Development as mandatory
   - No agent may write code without approved specs and tasks
   - All work must follow: Constitution → Specs → Plan → Tasks → Implement

2. Agent Behavior Rules
   - No manual coding by humans
   - No feature invention
   - No deviation from approved specifications
   - Refinement must occur at spec level, not code level

3. Phase Governance
   - Each phase is strictly scoped by its specification
   - Future-phase features must never leak into earlier phases
   - Architecture may evolve only through updated specs and plans

4. Technology Constraints
   - Python for backend
   - Next.js for frontend (later phases)
   - FastAPI, SQLModel, Neon DB
   - OpenAI Agents SDK, MCP
   - Docker, Kubernetes, Kafka, Dapr (later phases)

5. Quality Principles
   - Clean architecture
   - Stateless services where required
   - Clear separation of concerns
   - Cloud-native readiness

This constitution must remain stable across all phases and act as the supreme governing document for all agents.

## Response snapshot

Created comprehensive global constitution at `.specify/memory/constitution.md` defining:

- **Principle I**: Spec-Driven Development (MANDATORY) - enforcing Constitution → Specs → Plan → Tasks → Implement workflow
- **Principle II**: Agent Behavior Rules - no manual coding, no feature invention, no spec deviation, spec-level refinement
- **Principle III**: Phase Governance - strict phase isolation, no future feature leakage, documented evolution
- **Principle IV**: Technology Stack Constraints - Python/FastAPI/SQLModel/Neon DB, OpenAI Agents SDK, MCP, Next.js, Docker/Kubernetes/Kafka/Dapr
- **Principle V**: Quality Principles - clean architecture, stateless services, separation of concerns, cloud-native, observability

Plus Development Workflow section covering phase transition requirements and specification amendment process.

## Outcome

- ✅ Impact: Created supreme governing document for entire Evolution of Todo project (Phase I-V)
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md
- 🔁 Next prompts: Proceed to Phase I feature specification using /sp.specify
- 🧠 Reflection: Constitution establishes SDD methodology foundation for all future work

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
