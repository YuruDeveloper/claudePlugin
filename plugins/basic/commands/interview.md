markdown---
description: Deep interview based on a spec file or idea, then produce a detailed specification
argument-hint: [file path or idea text]
---

## Input

$ARGUMENTS

- If a file path: Read and fully understand the contents
- If idea text: Treat as initial concept and begin interview from there

## Process

1. Identify all explicit and implicit requirements from the input
2. Conduct a deep interview with the user based on the question areas below
3. Repeat until all ambiguities are resolved
4. After interview completion, write a detailed specification document

## Question Areas

- Technical architecture and implementation strategy
- UI/UX flows, edge cases, and interaction patterns
- Data modeling and state management
- API contracts and external system integration boundaries
- Performance, scalability, and bottlenecks
- Security considerations and threat model
- Error handling and failure scenarios
- Trade-offs between competing approaches
- Migration and backward compatibility
- Testing strategy and observability

## Interview Rules

- Never ask obvious or surface-level questions
- Only ask deep questions that reveal hidden complexity
- Always follow up when user answers are vague
- Challenge user assumptions when they seem weak
- Group max 2-3 questions per turn
- Explicitly confirm an area is sufficiently explored before moving on

## Completion Criteria

- All question areas sufficiently explored
- No remaining ambiguities
- User confirms no additional topics to discuss

## Output

- If file input: Write as `-detailed.md` suffix next to the original file
- If idea input: Write in current directory with a filename based on the core keyword of the idea
- Must be structured and detailed enough for implementation