import os
import sys

ALLOWED_CHARS_PATH = "./allowed_characters"
LANGUAGES = ["en", "hi", "ta", "te", "bn", "or", "ml", "kn", "gu", "mr"]


def load_allowed_characters(language):
    lang_file_path = os.path.join(ALLOWED_CHARS_PATH, f"{language}.txt")
    allowed_chars = set(" ")
    with open(lang_file_path, "r", encoding="utf-8") as f:
        for line in f:
            ch = line.strip()
            allowed_chars.add(ch)
    return allowed_chars


def check_phrases(input_file, language):
    results = []
    allowed_chars = load_allowed_characters(language)

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            phrase = line.strip()
            if not phrase:
                continue
            invalid_chars = sorted(set(ch for ch in phrase if ch not in allowed_chars))

            if invalid_chars:
                results.append(f"{phrase} | ❌ Invalid chars: {''.join(invalid_chars)}")
            else:
                results.append(f"{phrase} | ✅ OK")
    output_file = f"{os.path.splitext(input_file)[0]}_validated.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(results))
    print(f"\n✅ Output written to: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_characters.py <context_words.txt> <language>")
        print("Usage: python check_characters.py context_words.txt hi")
        sys.exit(1)

    input_file = sys.argv[1]
    language = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"❌ {input_file} file not found: ")
        sys.exit(1)

    if language not in LANGUAGES:
        print(f"❌ {language} not supported. Supported languages: {', '.join(LANGUAGES)}")
        sys.exit(1)

    check_phrases(input_file, language)
