# Solo Loan Calculator - Learning Log

## Session 1: November 19, 2025

### Time Invested
4 hours building/debugging

### What I Built
- Phase 1: Happy path implementation
- Phase 2: Input handling (comma support)

### Key Decisions Made
1. **Incremental approach**: Chose to build happy path first, then add features
2. **Git workflow**: Started on main for scaffold, branching for features
3. **Input cleaning strategy**: For phase 1 & 2 I will do the cleaning of inputs individually. Phase 3+, I will build a helper function for cleaner

### Stuck Points & Breakthroughs

#### Stuck: Formula syntax error
**Problem**: 'int' object is not callable, invalid syntx, did you forget a comma?
**Cause**: while inputting the formula, I added an extra 1 without an operation so python parced it as if I was calling a set
**Solution**: Troubleshooting with AI (Claude) review, found the extra 1 input that my eyes weren't seeing
**Lesson**: In Python, `number(expression)` means "call number as a function." All math operations need explicit operators (* / + -), or Python interprets parentheses as a function call

#### Stuck: Pylint inconsistent-return-statements
**Problem**: I had a pattern of adding an if True statement after a while loop that validated an input and would loop if the input was false
**Solution**: I removed the if statement and fixed the indent
**Lesson**: If the function will only pass the value if it's true, I don't need the redundent/explict True check after. I can just install the logic.

#### Stuck: Pylint no-else-return
**Problem**: Similar to above
**Solution**: Same
**Lesson**: Same

### What I Reinforced
- Validation loops, Function design, Input handling, and Validation

### Questions for Later Review
- Not yet

### Next Steps
- Phase 3: Validation and 0% APR handling
- Create `clean_input()` helper function (DRY refactor)

---

## Patterns Observed
If while loops will not return a value while it is false, I can just have the logic after the validation completes and passed the True value

## Session 2: November 19, 2025 (Continued)

### Time Invested
1 hour split across building and debugging

### What I Built
- Phase 3: Comprehensive validation + 0% APR handling
- Phase 4: Polish (screen clearing, formatting refinements)

### Key Decisions Made
1. **Helper function decision**: Considered creating `clean_input()` helper but chose to keep validation functions separate for clarity - each has subtly different requirements, and the helper function would have lead to the code being harder to follow, due to multiple functions needing to be passed to achieve the desired return.
2. **Validation strategy**: Added `<= 0` checks to principle and term inputs (rejects zero); interest uses `< 0` (allows 0% APR)
3. **Line continuation**: Used parentheses for multi-line function calls to satisfy pylint while keeping output clean

### Stuck Points & Breakthroughs

#### Stuck: Rendering terrible after pylint fixes
**Problem**: Prompts were displaying with extra whitespace and newlines after making pylint happy
**Cause**: Used triple-quoted strings with indentation - Python included all the whitespace in the string
**Solution**: Changed to parentheses-based line continuation for function calls
**Lesson**: Triple-quoted strings preserve ALL whitespace including indentation. For breaking long lines, use parentheses or backslashes instead.

#### Stuck: Interest validation bug
**Problem**: Validation was checking `float(user_input)` instead of `float(cleaned_user)`
**Cause**: Used wrong variable - tried to convert "5%" to float instead of "5"
**Solution**: Changed to check `float(cleaned_user)` after removing `%` symbol via the cleaned_user variable
**Lesson**: Always validate the cleaned version of input, not the raw input with special characters

#### Breakthrough: 0% APR handling
**Problem**: Original formula divides by zero when APR is 0
**Solution**: Added conditional check - if APR is 0, use simple division (principle/term), else use compound interest formula
**Lesson**: Edge cases often need special handling. The 0% case has a much simpler formula: just divide principle by number of payments.

### What I Reinforced
- Edge case handling (0% APR, negative values, zero values)
- Validation patterns across multiple similar functions
- Pylint compliance while maintaining readable code
- String formatting (`:g` for removing trailing zeros)
- Code organization and feature branch workflow
- Import os and os.system('clear') command, initally passed as os.system(clear) which produced an error before resolving

### Questions for Later Review
- When is code duplication acceptable vs when should you create helpers?
- Trade-offs between DRY principle and code clarity

### Completed Features
- [x] Phase 1: Happy path
- [x] Phase 2: Input handling  
- [x] Phase 3: Validation + 0% APR
- [x] Phase 4: Polish & UX improvements

### Next Steps
- Phase 5: Amortization schedule (stretch goal) - TBD
- Consider: How to balance percieved DRY effiecncy vs code clarity for similar but different functions.

---

## Patterns Observed
- Each validation function has subtle differences (> 0 vs >= 0, cleaning needs, return types)
- Sometimes keeping code separate is clearer than forcing abstraction
- Pylint forces you to think about line length and readability
- Testing edge cases (0%, negatives) reveals bugs in validation logic