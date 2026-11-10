# Status Report Examples

These examples illustrate the required level of specificity. They are not a fixed script; adapt the wording to the task and host.

## Running

```text
Status: running
Current phase: Verify
Completed: Implemented the parser and added coverage for valid and invalid input.
In progress: Running the focused test suite to check the new behavior.
Blocked: none
Changed: src/parser.ts, tests/parser.test.ts
Next: Inspect test results, then run the relevant build check.
```

## Blocked

```text
Status: blocked
Current phase: Verify
Completed: The implementation and local unit tests are complete.
In progress: Waiting for the staging API credentials required for the integration check.
Blocked: The `STAGING_API_TOKEN` is unavailable. Provide it or confirm that the integration check should be skipped.
Changed: src/client.ts, tests/client.test.ts
Next: Resume the integration check after the credential decision.
```

## Complete

```text
Status: complete
Current phase: Handoff
Completed: Implemented the feature, updated tests, and passed the focused test suite and build.
In progress: none
Blocked: none
Changed: src/feature.ts, tests/feature.test.ts, README.md
Next: none
```

## Failed

```text
Status: failed
Current phase: Verify
Completed: Implemented the requested change and started the focused test suite.
In progress: none
Blocked: The test command failed because the configured dependency could not be installed.
Changed: src/feature.ts, tests/feature.test.ts
Next: Install the missing dependency or provide a compatible environment, then rerun the focused checks.
```
