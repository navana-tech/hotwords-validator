
# 🔍 Hotwords-Validator

This tool validates hotwords or phrases before using them for ASR context biasing. It ensures that each hotword contains only valid characters for the selected language (e.g., English, Hindi, etc.) and helps you catch typos or special characters that can cause issues while using with Bodhi ASR API.

## Usage
```bash
python check_hotwords_characters.py <hotwords_file.txt> <language_code eg. hi>
```

## Input
- The hotwords file should contain **one hotword or phrase per line**.
```
bodhi
navana
post-emi
```  

## Ouput
- A new file <hotwords_file>_validated.txt will be created in the same folder.
- Each line shows the hotword/phrase and validation feedback specifying invalid characters.

```
bodhi | ✅ OK
navana | ✅ OK
post-emi | ❌ Invalid chars: -
```

