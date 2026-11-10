---
name: task-progress
description: Keep long-running AI tasks transparent by maintaining an accurate phase-based status, reporting progress at meaningful checkpoints, and surfacing blockers, files changed, and next actions. Use for coding, research, analysis, or other multi-step work when the user may ask what has been completed or what the AI is doing now.
---

# Task Progress

Make the current state of a multi-step task visible without pretending to observe activity that the host does not expose.

## Core rules

- At the beginning of a non-trivial task, create a short ordered checklist of concrete outcomes. Use phases the user can understand, such as `Understand`, `Plan`, `Implement`, `Verify`, and `Handoff`.
- Keep exactly one phase marked `in_progress` unless work is genuinely parallel. Mark an item `completed` immediately after its acceptance condition is met; do not wait until the end to reconstruct history.
- Before a file edit, state what is being changed and why. During longer work, send concise updates when a phase changes, a meaningful artifact is produced, a tool run finishes, or a blocker appears.
- Treat tool calls as evidence, not as progress by themselves. Report the result that affects the task: files inspected, decision made, test outcome, or unresolved issue.
- Do not invent completion percentages, hidden execution details, elapsed time, or background activity. If the host does not expose a process or tool's internal progress, say so explicitly.
- Keep progress updates separate from the final handoff. The final response must state what changed, what was verified, and what remains unresolved.

## Checkpoint cadence

Send a progress update at these checkpoints:

1. **Start**: state the goal, current interpretation, and first investigation step.
2. **After discovery**: summarize the relevant findings and the implementation direction.
3. **Before editing**: name the files or artifacts to be created or modified and the behavioral change.
4. **After each major phase**: state the acceptance result and the next phase.
5. **On a blocker**: identify the exact missing input, failure, or external dependency; distinguish it from work that is merely still in progress.
6. **Before handoff**: summarize verification status and any remaining risks.

For a short task, combine checkpoints into one or two updates. Do not emit repetitive updates for every trivial command.

## Status report format

When the user asks for status, or when a checkpoint update is due, use this compact format:

```text
Status: <running | blocked | complete | failed>
Current phase: <one phase>
Completed: <concrete outcomes>
In progress: <current action and its purpose>
Blocked: <none, or exact blocker and what is needed>
Changed: <files/artifacts changed so far, or none>
Next: <next concrete action>
```

Use a checklist when the task has several phases:

```text
Progress
- [x] Understand request and constraints
- [x] Inspect relevant code or sources
- [~] Implement the agreed change
- [ ] Verify behavior
- [ ] Report result
```

Do not list a phase as complete merely because work started. A phase is complete only when its stated acceptance condition has been met.

## Planning and scope

- Translate a vague request into a small number of observable outcomes before implementation.
- If an important choice is unresolved, ask one concise question and mark the task `blocked` only when work cannot safely continue without that answer.
- If the user says to continue, resume from the last known phase and restate the next action instead of restarting the task.
- Preserve user-owned or unrelated changes. Mention them only when they affect the current task.
- For parallel work, name each stream and report each stream's state separately; do not collapse unfinished work into a single completed status.

## Files, tools, and verification

- Record created, modified, and deleted files using paths relative to the project when possible.
- For code changes, report verification commands or checks and whether they passed, failed, or were not run. Do not equate a successful edit with verified behavior.
- For long-running commands, report `started`, `completed`, or `failed` only when the host provides that evidence. Do not claim to monitor a command after the tool call has returned unless a supported background-job status is available.
- If durable cross-session visibility is needed and the environment permits it, maintain one small project-local status artifact such as `.ai/task-progress.md` or `.ai/task-progress.json`. Keep it append-safe, avoid secrets, and update it at phase boundaries. Do not create this artifact for every short task.
- A durable status artifact is a supplement to, not a replacement for, the conversational status report. If the environment cannot persist it, continue with in-session updates and say that visibility ends with the session.

## Blockers and recovery

Classify the state accurately:

- `running`: work can continue and the next action is known.
- `blocked`: progress requires user input, unavailable credentials/access, a failed dependency, or an external process that must finish.
- `complete`: the requested outcome is implemented and applicable verification is finished.
- `failed`: the requested outcome could not be completed; include the failure and the safest recovery action.

When blocked, include:

- the exact condition;
- what has already been completed;
- what input or external event is needed;
- whether partial changes are safe to keep.

When recovering from a failure, do not silently retry indefinitely. Explain the retry target and update the status after the retry.

## Boundaries

This skill is a transparency protocol, not a process monitor, tracing backend, scheduler, or guarantee of real-time observability. It cannot reveal tool execution that the host does not report, infer another agent's hidden state, or make an uncooperative model emit updates. Use host-native logs, tracing, job controls, or dashboards when true external monitoring is required.

## Completion checklist

Before declaring the task complete, confirm:

- the requested outcome is present;
- every planned phase is either completed or explicitly removed with a reason;
- relevant tests, builds, inspections, or other verification are reported;
- blockers and unsupported observations are not hidden;
- the final response names the next action only when follow-up remains.
