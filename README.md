
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

## 🧹 Rules for Fixing Hotwords

### 1️⃣ Remove All Punctuation and Special Characters
Hotwords should not contain symbols like `.`, `@`, `%`, `-`, `_`, `/`, `#`, `!`, etc.

- ❌ **Invalid Examples:**
  - `loan@bodhi`
  - `emi%payment`
  - `bodhi.ai`

- ✅ **Fixed Examples:**
  - `loan bodhi`
  - `emi payment`
  - `bodhi ai`

📝 **Explanation:**  
Punctuation and symbols are not valid input for ASR biasing. Replace them with spaces or remove them entirely.

---

### 2️⃣ Remove Numeric Digits
Digits (0–9) should be written as **spoken words** for better recognition.

- ❌ **Invalid Examples:**
  - `emi123`
  - `loan2025`
  - `73percent`

- ✅ **Fixed Examples:**
  - `emi one two three`
  - `loan twenty twenty five`
  - `seventy three percent`

📝 **Explanation:**  
ASR models process spoken words, not numbers. Always write out numbers as they are pronounced.

---

### 3️⃣ Use Only Letters and Spaces
Avoid connecting words using dashes, underscores, or slashes.

- ❌ **Invalid Examples:**
  - `post-emi`
  - `loan_disbursement`
  - `loan/disbursal`

- ✅ **Fixed Examples:**
  - `post emi`
  - `loan disbursement`
  - `loan disbursal`

📝 **Explanation:**  
Use clean, space-separated words for accurate pronunciation-based matching.

---

### 4️⃣ Write Numbers in Full (Language-Specific)

Replace digits with their full spoken equivalents, depending on the **language** of your model.

#### **English Examples**
| Digits | Written Form |
|---------|--------------|
| `73` | seventy three |
| `24x7` | twenty four by seven |
| `2FA` | two factor authentication |


📝 **Explanation:**  
This ensures that the ASR model correctly recognizes number-related terms as they would be spoken.

---

## 📋 Common Invalid Examples and Their Fixes

| Invalid Hotword | Invalid Characters | Fixed Hotword | Notes |
|-----------------|--------------------|----------------|-------|
| `post-emi` | `-` | `post emi` | Remove hyphen |
| `bodhi.ai` | `.` | `bodhi ai` | Replace dot with space |
| `loan@bodhi` | `@` | `loan bodhi` | Remove special character |
| `navana#123` | `#123` | `navana one two three` | Replace digits with words |
| `73` | `73` | `seventy three` | Write number in words |
| `₹loan` | `₹` | `loan` | Remove currency symbol |
| `EMI₹2000` | `₹2000` | `emi two thousand` | Remove currency and spell number |
| `credit-score!` | `!-` | `credit score` | Remove punctuation |

---

