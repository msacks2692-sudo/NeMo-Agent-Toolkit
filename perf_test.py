import re
import timeit

text = """Thought: I should search for the temperature in SF.
Action: search
Action Input: what is the temperature in SF?
"""

regex_str = r"Action\s*\d*\s*:[\s]*(.*?)\s*Action\s*\d*\s*Input\s*\d*\s*:[\s]*(.*?)(?=\s*[\n|\s]\s*Observation\b|$)"
compiled_regex = re.compile(regex_str, re.DOTALL)

def without_compile():
    re.search(regex_str, text, re.DOTALL)

def with_compile():
    compiled_regex.search(text)

print("Without compile:", timeit.timeit(without_compile, number=100000))
print("With compile:", timeit.timeit(with_compile, number=100000))
