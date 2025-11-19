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