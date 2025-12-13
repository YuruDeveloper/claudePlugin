# YAML Guidelines

## Critical Rules (Never Forget)

### 1. Spaces Only - NO TABS
❌ DON'T: Use tabs for indentation
✅ DO: Use 2 or 4 spaces consistently

```yaml
# ✅ Correct
services:
  web:
    image: nginx
```

### 2. Indentation is Structure
```yaml
# ❌ Wrong indentation
services:
web:
  image: nginx

# ✅ Correct
services:
  web:
    image: nginx
```

### 3. Colon-Space Required
❌ `key:value` or `key :value`
✅ `key: value`

### 4. Strings Quote Rules
```yaml
# Simple strings - no quotes needed
name: john

# Special chars - use quotes
message: "Hello: world"
path: 'C:\Users\path'

# Multiline
description: |
  Line 1
  Line 2
```

## Common Mistakes I Make

### Boolean Values
```yaml
# ❌ Wrong - will be strings
enabled: "true"
disabled: yes

# ✅ Correct
enabled: true
disabled: false
```

Valid booleans: `true`, `false`, `yes`, `no`, `on`, `off`

### Arrays
```yaml
# Style 1 - Block
items:
  - item1
  - item2
  - item3

# Style 2 - Flow
items: [item1, item2, item3]

# ❌ DON'T mix styles inconsistently
```

### Anchors and Aliases
```yaml
# Define anchor
defaults: &defaults
  timeout: 30
  retries: 3

# Use alias
service1:
  <<: *defaults
  name: api
```

### Numbers and Strings
```yaml
# ❌ Interpreted as octal
version: 0123

# ✅ Quote version numbers
version: "0123"

# ✅ Port numbers don't need quotes
port: 8080
```

### Empty Values
```yaml
# All represent null/empty
key1:
key2: null
key3: ~
```

## Docker Compose Specific

```yaml
# ✅ Proper structure
version: "3.8"
services:
  web:
    image: nginx:latest
    ports:
      - "80:80"
    environment:
      - NODE_ENV=production
    volumes:
      - ./data:/data
```

Common mistakes:
- ❌ Wrong version format: `version: 3.8` (needs quotes)
- ❌ Port without quotes: `ports: [80:80]` (should be `"80:80"`)

## Quick Check

Before writing YAML:
- [ ] Using spaces, not tabs?
- [ ] Consistent indentation (2 or 4 spaces)?
- [ ] `key: value` with space after colon?
- [ ] Strings with special chars quoted?
- [ ] Version numbers quoted?
- [ ] Boolean values correct (true/false)?
