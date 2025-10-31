
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
bodhi.ai
loan@bodhi
navana#123
73
seventy three
₹loan
EMI₹2000
credit-score!
```  

## Ouput
- A new file <hotwords_file>_validated.txt will be created in the same folder.
- Each line shows the hotword/phrase and validation feedback specifying invalid characters.

```
bodhi | ✅ OK
navana | ✅ OK
post-emi | ❌ Invalid chars: -
bodhi.ai | ❌ Invalid chars: .
loan@bodhi | ❌ Invalid chars: @
navana#123 | ❌ Invalid chars: #123
73 | ❌ Invalid chars: 37
seventy three | ✅ OK
₹loan | ❌ Invalid chars: ₹
EMI₹2000 | ❌ Invalid chars: 02EIM₹
credit-score! | ❌ Invalid chars: !-
```

## Fix hotwords

Based on the output by remove/changing characters whcich are not valid. Punctuations, numerics and special characters are not valid. for any numbers pleasew rite its full form of how it is pronounced like `73` should be `seventy three` for english and similar to other languages as well.

