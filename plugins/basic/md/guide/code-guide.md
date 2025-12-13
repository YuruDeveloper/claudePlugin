# Code Guidelines

## Critical Rules (Never Forget)

### 1. Full Code Only - No Truncation
❌ "rest remains unchanged", "... (omitted)", "same as before"
✅ Complete file contents, always

### 2. Edit First, Create Last
❌ New file when existing can be modified
✅ Rewrite/enhance existing code

### 3. No Unnecessary Fallbacks
❌ `try-catch` hiding real errors
✅ Let failures surface clearly

### 4. Implementation Not Suggestions
❌ "You should write..." or "This would work..."
✅ Actual working code

### 5. Think Before Code
❌ Jump straight to implementation
✅ Analyze approach first

### 6. Clean Up Dead Code
❌ Leave unused imports, variables, files
✅ Remove and flag obsolete code

## Common Mistakes I Make

### Security Vulnerabilities
NEVER write:
- SQL injection: `query = "SELECT * FROM users WHERE id=" + userId`
- XSS: `innerHTML = userInput`
- Command injection: `exec(userInput)`
- Hardcoded secrets: `API_KEY = "abc123"`

### Naming Conventions
- **Default**: PascalCase
- **Language priority**: Python (snake_case), TypeScript (camelCase), Go (MixedCaps)
- **Follow existing project patterns**

### Missing Edge Cases
- Input validation at boundaries
- Null/undefined checks when needed
- Array bounds checking

### Incomplete Refactoring
When changing function signature:
- ❌ Update declaration only
- ✅ Update all call sites too

## Quick Check

Before writing:
- [ ] Editing existing file?
- [ ] Full code output?
- [ ] No security holes?
- [ ] Language conventions?
- [ ] Thought through?