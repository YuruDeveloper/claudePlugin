# Makefile Guidelines

## Critical Rules (Never Forget)

### 1. TABS Not Spaces for Commands
```makefile
# ✅ TAB before command
target:
→   echo "Hello"

# ❌ Spaces - WILL FAIL
target:
    echo "Wrong"
```

### 2. .PHONY for Non-File Targets
```makefile
.PHONY: clean test build

clean:
→   rm -rf dist/
```

### 3. Variables: = vs :=
```makefile
FILES = $(wildcard *.txt)  # Lazy (evaluated when used)
NOW := $(shell date)       # Immediate (evaluated now)
```

## Common Mistakes I Make

### Multi-line Commands Need && or ;
```bash
# ❌ Each line is separate shell
install:
→   cd project
→   npm install  # Won't work!

# ✅ Chain with &&
install:
→   cd project && npm install

# ✅ Or backslash continuation
install:
→   cd project && \
→   npm install
```

### Dependencies
```makefile
# Build depends on clean
build: clean
→   npm run build

# Multiple dependencies
deploy: build test
→   ./deploy.sh
```

### Suppress Command Echo with @
```makefile
clean:
→   @echo "Cleaning..."  # Don't show echo command
→   @rm -rf dist/        # Don't show rm command
```

### Ignore Errors with -
```makefile
clean:
→   -rm file_that_might_not_exist
→   @echo "Done"
```

### Pattern Rules
```makefile
%.js: %.ts
→   tsc $<

# $< = first prerequisite
# $@ = target name
# $^ = all prerequisites
```

### Automatic Variables
- `$@` - Target name
- `$<` - First prerequisite
- `$^` - All prerequisites
- `$?` - Changed prerequisites

## Example
```makefile
.PHONY: all build clean

APP := myapp
BUILD_DIR := dist

all: build

build: clean
→   @mkdir -p $(BUILD_DIR)
→   @npm run build

clean:
→   @rm -rf $(BUILD_DIR)
```

## Quick Check

- [ ] TABs not spaces?
- [ ] .PHONY declared?
- [ ] Multi-line uses && or \?
- [ ] @ to suppress echo?
- [ ] Variables use := or =?
