import glob
import sys

SYSTEM_PROMPT_PATTERNS = [
    "SYSTEM_PROMPT",
    "system_prompt",
    "system message",
    "system_message",
    "role: system",
]

INJECTION_PHRASES = [
    "ignore previous instructions",
    "ignore all previous instructions",
    "you are now",
    "pretend you are",
    "act as if you have no restrictions",
]

found = []

for filename in glob.glob("**/*.py", recursive=True):
    if filename == "inject_scanner.py":
        continue

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
    except Exception:
        continue

    for pattern in SYSTEM_PROMPT_PATTERNS:
        if pattern.lower() in content.lower():
            found.append(
                f"{filename}: SYSTEM_PROMPT pattern -> {pattern}"
            )

    for phrase in INJECTION_PHRASES:
        if phrase.lower() in content.lower():
            found.append(
                f"{filename}: INJECTION phrase -> {phrase}"
            )

if found:
    print("Prompt injection / hardcoded system prompt findings:")
    for item in found:
        print(f" - {item}")

    sys.exit(1)

print("Custom prompt injection scanner: CLEAN")
sys.exit(0)