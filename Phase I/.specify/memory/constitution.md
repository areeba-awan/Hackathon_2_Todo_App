# Evolution of Todo Constitution

The supreme governing document for the Evolution of Todo multi-phase AI agent project.

## Core Principles

### I. Spec-Driven Development (MANDATORY)

All development MUST follow Spec-Driven Development (SDD) as the primary methodology. No agent may write production code without approved specifications and tasks. The mandatory workflow sequence is:

- **Constitution** → The supreme governing document defining project-wide rules
- **Specs** → Feature specifications in `specs/<feature>/spec.md` detailing requirements
- **Plan** → Architectural decisions and implementation strategy in `specs/<feature>/plan.md`
- **Tasks** → Testable, ordered tasks in `specs/<feature>/tasks.md`
- **Implement** → Code execution following Red-Green-Refactor cycles

**Rationale**: SDD ensures architectural consistency, reduces rework, and maintains quality across all phases and contributors.

### II. Agent Behavior Rules

Agents operating on this project MUST adhere to these non-negotiable rules:

1. **No Manual Coding**: Humans do not write production code. All code originates from agent execution of approved tasks.
2. **No Feature Invention**: Agents MUST NOT introduce features not specified in approved specifications. Scope creep requires spec amendment.
3. **No Specification Deviation**: Implementation MUST exactly match approved specs. Deviations require spec re-review and approval.
4. **Refinement at Spec Level**: Design issues, ambiguities, or improvements MUST be addressed by amending specifications, not by unilateral code-level decisions.

**Rationale**: Prevents architectural drift, ensures traceability, and maintains project vision across all contributors.

### III. Phase Governance

Each phase operates under strict governance to prevent scope leakage and maintain focus:

1. **Phase Scope Isolation**: Each phase (I-V) is strictly bounded by its specification document. Features defined for future phases MUST NOT be implemented early.
2. **No Future Feature Leakage**: Architecture decisions and code patterns must not include hooks, abstractions, or infrastructure specifically for future-phase features unless explicitly approved in the current phase's spec.
3. **Evolution Through Documentation**: Architecture may evolve only through updated specifications and plans. No organic evolution through implementation decisions.
4. **Phase Completion Criteria**: A phase is complete only when all tasks in its `tasks.md` are marked done and tests pass.

**Rationale**: Prevents feature creep, maintains clear milestones, and ensures each phase delivers tangible value.

### IV. Technology Stack Constraints

The following technology choices are fixed for the project lifetime:

- **Backend**: Python with FastAPI framework
- **ORM/Data Access**: SQLModel for database interactions
- **Database**: Neon DB (PostgreSQL-compatible cloud database)
- **AI Framework**: OpenAI Agents SDK for agent behavior
- **Integration Protocol**: Model Context Protocol (MCP) for tool/external system integration
- **Frontend (Phase III+)**: Next.js framework
- **Infrastructure (Phase IV+)**: Docker containers, Kubernetes orchestration
- **Event-Driven Architecture (Phase V)**: Kafka for event streaming, Dapr for distributed primitives

Any deviation from these technologies requires an ADR (Architecture Decision Record) with full trade-off analysis and user approval.

**Rationale**: Consistent technology choices reduce cognitive load, enable knowledge sharing, and prevent stack fragmentation.

### V. Quality Principles

All code, architecture, and documentation MUST adhere to these quality standards:

1. **Clean Architecture**: Separation of concerns with clear boundaries between layers (API, business logic, data access).
2. **Stateless Services**: Services MUST be stateless where required to enable horizontal scaling and resilience.
3. **Separation of Concerns**: Distinct modules for distinct responsibilities. No God modules or services.
4. **Cloud-Native Readiness**: Design assumes cloud deployment from day one (environment variables for config, observability hooks, graceful degradation).
5. **Observable Systems**: All services MUST emit structured logs, metrics, and traces for operational visibility.
6. **Test Coverage**: Unit tests for business logic, integration tests for API contracts and data operations.

**Rationale**: Quality principles ensure maintainability, scalability, and operational excellence across the project lifecycle.

## Development Workflow

### Phase Transition Requirements

Before transitioning between phases, the following must be complete:

1. All `tasks.md` items for the current phase are marked complete
2. All tests pass (unit, integration, and any E2E)
3. Code passes linting and security scanning
4. Documentation reflects current state (README, API docs, architecture)
5. Retrospective conducted and lessons learned documented

### Specification Amendment Process

To modify an approved specification:

1. Identify the specific section requiring change
2. Document the rationale for change (problem, impact, alternatives considered)
3. Obtain stakeholder approval for the amendment
4. Update the spec, plan, and tasks accordingly
5. Re-run affected task chains

Unapproved specification changes are prohibited.

## Governance

**Constitution Supremacy**: This constitution supersedes all other project documents, practices, and conventions. In cases of conflict, this document takes precedence.

**Amendment Process**: Constitutional amendments require:
- Documentation of proposed change with rationale
- Review by all active contributors
- Explicit user consent before adoption
- Version increment following semantic versioning rules

**Compliance Verification**: All code contributions MUST be verified for constitution compliance during review.

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02
