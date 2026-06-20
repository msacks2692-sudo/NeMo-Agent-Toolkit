## 2025-06-20 - Pre-compiling Regex in ReAct output parser
**Learning:** Precompiling regexes in hot paths is important, but replacing dynamic string regex matching on failure paths is unexpectedly a huge optimization, speeding up the fail path by ~48%.
**Action:** Always check the failure paths for dynamic regex compilation.

## 2025-06-20 - Pre-compiling Regex in ReAct output parser
**Learning:** Precompiling regexes in hot paths is important, but replacing dynamic string regex matching on failure paths is unexpectedly a huge optimization, speeding up the fail path by ~48%.
**Action:** Always check the failure paths for dynamic regex compilation.
