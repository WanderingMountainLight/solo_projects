# Calculator Project - Learning Log
**Date:** November 9, 2025  
**Time invested:** ~4 hours total, 3.5 hours coding (30min-1hr stuck time) and ~30 minutes of debreif
**Goal:** Translate flowchart to working calculator with full error handling

## What I Built
After completing building and refactoring a calculator via the Launch School Core curriculum walk through. I elected to pause and come back to rebuild a second one without the walk through. I completed a FlowChart to confirm my logic and error handling prior to my coding session. I then worked to convert the FlowChart into workable code.

## Key Accomplishments
I was able to get the 'happy path' core functionality working with no errors or syntax look ups.

## Where I Got Stuck
- **try/except structure**: Initially wrote `try int(num):` instead of block structure with code inside `try:`
- **Function arguments**: Forgot to pass arguments to validation functions (`valid_op()` vs `valid_op(op_input)`)
- **Calling functions twice**: Had `pass_num()` then `num1 = pass_num()` causing double input prompts
- **Validation timing**: Tried to validate AFTER conversion instead of BEFORE
- **Pylint compliance**: Started at 7.38/10, learned about trailing-whitespace, bare-except and inconsistent returns to reach 10/10

## Patterns to Watch
- **Function parameters/scope**: Forgetting to pass arguments to functions happened multiple times
- **Validate-before-convert**: Always validate string input BEFORE trying to convert it
- **Specific exceptions**: Use `except ValueError:` instead of bare `except:` for predictable error handling
- **Return consistency**: All return paths in a function should return the same type

## Next Steps
- If I continue refining this calculator, I would look to add additional functionality around more complex calculations, and error handling.