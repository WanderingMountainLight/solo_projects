# Calculator Project - Learning Log
# November 9, 2025 - Build base calculator from scratch
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

# November 14, 2025 - Add Launch School Suggested Bonus Features
**Time invested:** ~3 hours total (2 hours coding, 1 hour learning/debugging)
**Goal:** Rebuild solo calculator with bonus features independently to prove mastery

## What I Built
Successfully rebuilt my calculator with three bonus features:
1. **Floating-point support** - Changed validation and calculations to handle decimals
2. **Calculator loop** - Added ability to perform multiple calculations without relaunching app
3. **JSON configuration** - Extracted all user messages to external configuration file

Still to implement: Internationalization (3+ languages)

## Key Accomplishments
- Implemented features WITHOUT looking at last week's guided calculator first
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
Rebuilding independently proved I understand the patterns, not just following along. Getting stuck on different issues is part of learning and growing.

# November 15, 2025 - Internationalization feature
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
- **KeyError on invalid input**: Tried to access `messages['invalid_nums']` when JSON key was `'invalid_num'` (singular). Typo in code didn't match JSON. The "Y e s" bug was frustrating but taught me to test with realistic inputs, not just correct happy-path data.
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
Completing internationalization felt like a major milestone. The JSON structure came naturally, but the two-stage loading (all_messages -> messages) took a moment to internalize. Most bugs were typos rather than logic errors, which shows the patterns are sinking in. Still reaching for documentation and Claude for JSON syntax, but that's expected. Four languages is ambitious and working smoothly!

# November 16, 2025 - LSBot Refactor
**Time invested:** ~2.5 hours (refactoring and testing)
**Goal:** Apply LSBot's refinement suggestions through systematic refactoring

## What I Built
Completed all refactoring improvements on solo calculator:
1. **Split operation functions** - Separated prompting from calculation logic; this was mostly complete in my base code but moved the prompt into the function.
2. **Wrapped in main()** - Moved all execution code into main function
3. **Parameter passing** - Functions now receive messages dict instead of accessing globals

Division by zero was already in correct location, so skipped that refactoring.

**Final result: Fully-featured calculator with 4 languages, clean structure, 10/10 pylint**

## Key Accomplishments
- Successfully refactored working code without breaking functionality
- Maintained 10/10 pylint score through all changes
- Tested each refactoring individually before moving to next
- Used separate git branches for each refactoring (building good habits)
- Functions are now self-contained with no global variable dependencies

## Where I Got Stuck
- **Parameter propagation**: When moving `messages` into main(), had to update all function calls to pass it as parameter. Initially forgot the division by zero check also calls `pass_num()`, causing error until fixed.
- **Module-level vs function scope**: Took a moment to understand what belongs outside main() (imports, JSON loading, function definitions) vs inside main() (all execution including language selection)

## Patterns Reinforced
- **One refactoring at a time**: Changed one thing, tested, committed. Didn't try to do everything at once.
- **Functions with parameters are more reusable**: Passing `messages` as parameter makes functions testable and independent. Allows updates to one file that are automatically implemented across the app. 
- **Git branches for organization**: Even small refactorings benefit from separate branches. Allows for the ability to scrap the code if the feature doesn't work as expected without impacting main branch/app.
- **Test after every change**: Verified functionality in all 4 languages after each refactoring

## What I Learned Today
- **Main() function pattern**: Professional Python programs wrap execution in main(), keeping module level for setup only. This was an LSBot recommendation.
- **Global variable**: When functions access global variables, they're harder to test and reuse, this becomes clear when refactoring and moving parts of the app into different functions. Passing as parameters is cleaner.
- **Refactoring is about structure, not features**: Code does the same thing, but organization makes it more maintainable.
- **"Wall of text" observation**: Even well-structured code can look dense. The difference is in how the logic flows, not how it looks at first glance. Collapsing the functions in VSCode when they are feature complete is useful to focus on current problems.

## Challenges Overcome
- **Passing messages as parameters**: Required systematic updates to function signatures and all locations where they are called. This was the most interesting challenge from today, ensuring every function that needs messages receives it explicitly rather than grabbing it from global scope.

## Final State
Solo calculator now has:
- 4 languages (English, Spanish, Portuguese, German)
- Floating-point support with input validation
- Loop for multiple calculations
- JSON configuration with fully localized messages
- Clean function separation (prompting, validation, calculation)
- Professional structure with main() wrapper
- Zero global variable dependencies in functions
- 10/10 pylint score

## Reflection
The refactoring phase solidified understanding of function design and scope. While the original code worked, the refactored version is more maintainable and professional. The "wall of text" observation is interesting - suggests I'm still building the mental models for quickly parsing code structure. Passing parameters instead of using globals felt awkward initially but makes complete sense now. This exercise proved I can not only build features but also improve existing code systematically.

## Comparison to Guided Calculator
- Solo version has 4 languages vs guided version's 3
- Both maintain 10/10 pylint
- Solo version built independently, proving mastery of patterns
- Refactoring applied same principles learned yesterday but implemented autonomously
- More confident in decision-making about code organization

# November 16, 2025 (Session 2) - Final Polish Based on LSBot Feedback
**Time invested:** ~30 minutes
**Goal:** Apply LSBot's additional refinement suggestion

## What I Built
Final refinement to number input handling:
- Updated `pass_num()` to include initial prompt inside function
- Added `prompt_key` parameter to make function more flexible and reusable
- Matches pattern established with `prompt_for_operation()`
- All number prompts now handled consistently

## Key Accomplishments
- Responded to code review feedback with additional refinement
- Maintained 10/10 pylint score
- Function now more reusable and follows single responsibility principle
- Completed full development cycle: Build, Review, Refine, Complete

## What Changed
**Before:**
```python
# In main:
prompt(messages['first_num'])
num1 = pass_num(messages)
```

**After:**
```python
# In main:
num1 = pass_num(messages, 'first_num')
# Prompt happens inside function now
```

## What I Learned
- **Encapsulation matters**: Moving prompt into function makes the function self-contained
- **Parameterization adds flexibility**: `prompt_key` parameter makes same function work for different prompts
- **Consistency in design**: All input functions (numbers, operations) now follow same pattern
- **Professional iteration**: Real development includes listening to feedback, implementing and refining working code

## Reflection
My implementation of LSBot's feedback is driven by my belief that "code works" isn't the end goal of Software Development and Engineering. Professional code is maintainable and consistent. Software Engineers respond to feedback. LSBot's suggestion helped me see that even though my code worked and was beyond good enough, it could be more elegant by following the same pattern throughout. This exercise reinforced that software development is iterative and that good developers welcome feedback as an opportunity to improve.

## Final Project State
Calculator is now complete with:
- All 4 bonus features implemented
- All LSBot refinements applied
- Consistent function design throughout
- Professional git history showing iterative improvement
- 10/10 pylint score maintained across all changes
- 4 languages fully localized

# Final Project Reflection
I found developing the calculator on my own to be challenging but the problemsolving and iteration to be engaging and rewarding. As an aspiring SWE just starting their Launch School reskill journey, I find challenges like this are why I'm interested in pursuing this career change. I am coming into the SWE field at an exciting and challenging time with the prevalence of AI systems to write boiler plate type code, but I am enjoying the challenge while also making use of AI systems to provide me an instant feeback loop and as a tool to be better, not the solution machine.