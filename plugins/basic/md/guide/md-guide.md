# Markdown Guidelines

## Critical Rules (Never Forget)

### 1. Code Blocks MUST Have Language
❌ DON'T:
````markdown
```
code here
```
````

✅ DO:
````markdown
```bash
echo "hello"
```
````

### 2. Heading Hierarchy - No Skipping
❌ `# H1` → `### H3` (skipped H2)
✅ `# H1` → `## H2` → `### H3`

### 3. Inline Code Requires Backticks
❌ `file.txt` or `npm install` without backticks
✅ `` `file.txt` `` and `` `npm install` ``

### 4. Links Need Descriptive Text
❌ `[here](url)` or `[click this](url)`
✅ `[Installation Guide](url)` or `[API Reference](url)`

### 5. Spacing
- Blank line before/after code blocks
- Blank line between sections
- Blank line between paragraphs

### 6. Lists - 2 Space Indent for Nesting
```markdown
- Item
  - Nested (2 spaces)
    - Double nested (4 spaces)
```

## Common Mistakes I Make

### Escaping Special Characters
When displaying markdown syntax, escape: `\*`, `\_`, `` \` ``, `\[`, `\]`

### Tables Must Align
```markdown
| Left | Center | Right |
|:-----|:------:|------:|
| Text | Text   | Text  |
```

### Nested Structures
Code block in list needs 4+ space indent:
```markdown
1. Install dependencies:

    ```bash
    npm install
    ```
```

### File Paths
Always use inline code for paths: `` `/home/user/file` ``

## Restrictions

- ❌ Emojis (😀)
- ✅ Kaomoji ((´・ω・`))
- ❌ HTML unless necessary
- ❌ Vague link text

## Document Types

**README.md**: Name, Install, Usage, Features
**CLAUDE.md**: Clear instructions, explicit exceptions
**Docs**: Code examples, expected output