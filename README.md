
# Hotwords-Validator

1. Keep all hotowrds/phrases each on a single line as mentioned below

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

