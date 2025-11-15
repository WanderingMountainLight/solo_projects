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

git  The "Y e s" bug was frustrating but taught me to test with realistic inputs, not just correct happy-path data.

**Date:** November 15, 2025  
**Time invested:** ~1 hour (coding and debugging)
**Goal:** Complete Feature 4: Internationalization (multiple languages)

## What I Built
Successfully implemented internationalization with 4 languages (English, Spanish, Portuguese, German):
- Restructured JSON to nest languages under top-level keys
- Added language selection at program start with validation
- Implemented dictionary mapping for cleaner language selection (LSBot's suggested refinement, my implementation)
- Added localized yes/no validation for each language
- All user-facing text now fully localized including error messages

**All 4 bonus features now complete!**

## Key Accomplishments
- Generated comprehensive JSON translations for 4 languages independently
- Used dictionary mapping (`lang_map`) instead of if/elif chain for cleaner code
- Successfully debugged language selection and message loading flow
- Maintained 10/10 pylint score throughout

## Where I Got Stuck
- **F-string syntax with dictionaries**: Got `SyntaxError: unmatched '['` when using same quote types for f-string and dictionary key. Fixed by alternating quote styles: `f"{messages['key']}"` vs `f'{messages["key"]}'`
- **KeyError on invalid input**: Tried to access `messages['invalid_nums']` when JSON key was `'invalid_num'` (singular). Typo in code didn't match JSON.
- **German "Nein" validation failing**: Had typo `"Nien"` in JSON instead of `"Nein"`. Took a moment to spot since validation was working for other languages.
- **Chicken-and-egg problem**: Initially tried to use localized error for invalid language choice, but messages aren't loaded yet. Solved by hardcoding pre-selection error in English.

## Patterns Reinforced
- **Check JSON keys carefully**: Typos in dictionary keys cause KeyErrors that aren't caught until runtime
- **Quote consistency in f-strings**: When nesting quotes, alternate single/double to avoid syntax errors
- **Dictionary mapping vs if/elif**: Much cleaner and more maintainable for simple key-value mappings
- **Timing of variable availability**: Can't use `messages` before language is selected and messages are loaded

## What I Learned Today
- **Two-stage message loading**: Load entire JSON into `all_messages`, then select specific language into `messages`
- **F-string quote nesting**: Can't use `f'{messages['key']}'` - must alternate quote types
- **When NOT to extract functions**: Language selection happens once at startup, doesn't need to be a function
- **Localization boundaries**: Some messages (like pre-language-selection errors) must stay in one language

## What Still Needs Practice
- **JSON access patterns**: Still need to look up syntax for loading and accessing nested JSON structures
- **Variable naming conventions**: Remembering to use `all_messages` vs `messages` for clarity
- **When to use .title()**: Apply to user input for validation, not to stored values in JSON

## Next Steps
- Refactoring phase: Apply remaining LSBot suggestions
  - Split `operation_choice()` into smaller focused functions  
  - Move division by zero handling to main
  - Wrap everything in `main()` function
- Final polish and testing across all languages

## Reflection
Completing internationalization felt like a major milestone. The JSON structure came naturally, but the two-stage loading (all_messages → messages) took a moment to internalize. Most bugs were typos rather than logic errors, which shows the patterns are sinking in. Still reaching for documentation on JSON syntax, but that's expected. Four languages is ambitious and working smoothly!