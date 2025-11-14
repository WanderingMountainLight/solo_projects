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

**Date:** November 14, 2025  
**Time invested:** ~3 hours total (2 hours coding, 1 hour learning/debugging)
**Goal:** Rebuild solo calculator with bonus features independently to prove mastery

## What I Built
Successfully rebuilt my calculator with three bonus features:
1. **Floating-point support** - Changed validation and calculations to handle decimals
2. **Calculator loop** - Added ability to perform multiple calculations without relaunching app
3. **JSON configuration** - Extracted all user messages to external configuration file

Still to implement: Internationalization (3+ languages)

## Key Accomplishments
- Implemented features WITHOUT looking at yesterday's guided calculator first
- Applied `.strip()` consistently to all inputs from the start (LSBot's refinement suggestion)
- Used `\n` formatting in JSON for multi-line messages
- Maintained 10/10 pylint score throughout
- Proper git workflow with feature branches for each bonus feature

## Where I Got Stuck
- **Naming conflicts**: Created function `continue_calc()` with variable `continue_calc` inside it. Python couldn't distinguish between them
- **Yes/No validation logic**: Loop kept continuing even after setting `continue_calc = False`. Turned out I was testing with spaces between letters ("Y e s" instead of "Yes")
- **f-string overuse**: Used f-strings without variables (`f'text'` instead of `'text'`), caught by pylint
- **JSON key typo**: Misspelled `continue_calculation` as `continue_caclulation` in code, causing KeyError

## Patterns Reinforced
- **Input handling consistency**: Adding `.strip()` to EVERY input makes program more robust
- **Test with edge cases**: Spaces, wrong capitalization, invalid entries. Users type weird things
- **One feature per branch**: Clean git history makes it easy to track what changed when
- **Function vs. top-level code**: Not everything needs to be in a function. Loops can live at module level until wrapping in main()
- **Debugging with print statements**: Adding debug prints helped identify the "Y e s" spacing issue

## What I Learned Today
- **Scope matters**: Global variables can be accessed inside functions, but it creates dependencies that limit reusability
- **Validation before conversion**: Always check if string is valid BEFORE calling `float()` to avoid crashes
- **Git workflow becoming automatic**: Branch, implement, test, pylint, commit, merge, delete is now muscle memory
- **JSON structure**: User-facing strings belong in config files, not hardcoded in Python

## Next Steps
- Complete Feature 4: Internationalization (3 languages with dictionary mapping)
- Apply remaining LSBot refinements during refactoring phase
- Wrap everything in `main()` function
- Further split `operation_choice()` into smaller focused functions

## Reflection
Rebuilding independently proved I understand the patterns, not just following along. Getting stuck on different issues is part of learning and growing. The "Y e s" bug was frustrating but taught me to test with realistic inputs, not just correct happy-path data.