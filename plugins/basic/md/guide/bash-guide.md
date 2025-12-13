# Bash Script Guidelines

## Critical Rules (Never Forget)

### 1. Always Use Shebang + set Options
```bash
#!/bin/bash
set -euo pipefail  # Exit on error, undefined vars, pipe failures
```

### 2. Quote Variables Always
```bash
# ❌ Wrong
cat $FILE_PATH

# ✅ Correct
cat "$FILE_PATH"
```

### 3. Use [[ ]] for Conditionals
```bash
# ❌ Old/fragile
if [ $VAR = "value" ]; then

# ✅ Modern/safe
if [[ "$VAR" == "value" ]]; then
```

### 4. Command Substitution: $() not backticks
```bash
# ❌ OUTPUT=`command`
# ✅ OUTPUT=$(command)
```

## Common Mistakes I Make

### Unquoted Variables
```bash
# ❌ Breaks with spaces
FILE_PATH=$(echo $PARAMS | jq -r '.file_path')
cd $FILE_PATH

# ✅ Always quote
FILE_PATH=$(echo "$PARAMS" | jq -r '.file_path')
cd "$FILE_PATH"
```

### File/Directory Tests
```bash
if [[ -f "$FILE" ]]; then   # file exists
if [[ -d "$DIR" ]]; then    # directory exists
if [[ -e "$PATH" ]]; then   # any type exists
if [[ -s "$FILE" ]]; then   # not empty
```

### Parameter Expansion
```bash
TIMEOUT="${TIMEOUT:-30}"              # default value
FILE="${1:?Error: file required}"     # required param
FILENAME="${PATH##*/}"                # basename
EXTENSION="${FILE##*.}"               # get extension
```

### Functions with Local Variables
```bash
my_function() {
    local arg1="$1"
    local result="computed"
    echo "$result"
}

output=$(my_function "input")
```

### Arrays
```bash
FILES=("file1.txt" "file2.txt")
echo "${FILES[0]}"        # single element
echo "${FILES[@]}"        # all elements
echo "${#FILES[@]}"       # length
```

## Security - NEVER Do This

```bash
# ❌ Command injection
eval "$USER_INPUT"
bash -c "$USER_INPUT"

# ✅ Validate first
if [[ "$INPUT" =~ ^[a-zA-Z0-9_-]+$ ]]; then
    process "$INPUT"
fi
```

## Quick Check

- [ ] `#!/bin/bash` + `set -euo pipefail`?
- [ ] All variables quoted?
- [ ] Using `[[ ]]` not `[ ]`?
- [ ] No command injection risk?
- [ ] Functions use `local`?
