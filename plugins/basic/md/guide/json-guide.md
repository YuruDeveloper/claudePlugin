# JSON Guidelines

## Critical Rules (Never Forget)

### 1. No Trailing Commas
❌ DON'T:
```json
{
  "key": "value",
  "array": [1, 2, 3,]
}
```

✅ DO:
```json
{
  "key": "value",
  "array": [1, 2, 3]
}
```

### 2. No Comments
❌ DON'T:
```json
{
  // This is a comment
  "key": "value"
}
```

✅ DO: Use separate documentation or remove comments entirely

### 3. Double Quotes Only
❌ `'single quotes'` or `unquoted`
✅ `"double quotes"`

### 4. Valid Value Types
- String: `"text"`
- Number: `123` or `45.67`
- Boolean: `true` or `false` (lowercase)
- Null: `null` (lowercase)
- Array: `[1, 2, 3]`
- Object: `{"key": "value"}`

## Common Mistakes I Make

### Package.json Specific
- ❌ Missing `"type": "module"` when using ESM
- ❌ Wrong semver format: `1.2.3.4` (should be `1.2.3`)
- ❌ Duplicate keys
- ✅ Use exact versions for critical deps: `"1.2.3"` not `"^1.2.3"`

### Structure Errors
```json
// ❌ Wrong
{
  key: value,
  "mixed": 'quotes'
}

// ✅ Correct
{
  "key": "value",
  "mixed": "double quotes"
}
```

### Numbers
- ❌ `"123"` when number expected
- ❌ `.5` (must be `0.5`)
- ❌ `1.` (must be `1.0` or `1`)
- ✅ `123`, `0.5`, `1.0`

## Quick Check

Before writing JSON:
- [ ] No trailing commas?
- [ ] No comments?
- [ ] All keys in double quotes?
- [ ] Valid value types?
- [ ] Proper number format?
