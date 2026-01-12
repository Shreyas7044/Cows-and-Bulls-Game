# 🐄 Cows and Bulls Game in Python

Cows and Bulls is a classic pen-and-paper guessing game implemented here using Python. The computer generates a secret 4-digit number with unique digits, and the player must guess it using logical hints.

---

## 🎯 Game Rules

- The secret code is a **4-digit number**
- All digits must be **unique**
- The player guesses the number
- After each guess:
  - **Bull** → Correct digit in the correct position
  - **Cow** → Correct digit in the wrong position
- The game continues until:
  - The player guesses correctly (4 bulls), or
  - The player runs out of tries

---

## 📌 Example

Secret Code: `1234`  
Guess: `1246`  

Result:
- 2 Bulls (1, 2)
- 1 Cow (4)

---

## 🛠️ Approach Used

1. Generate a random 4-digit number.
2. Ensure no repeated digits.
3. Take user guesses.
4. Compare guess with secret number.
5. Count bulls and cows.
6. Repeat until success or tries exhausted.

---

## 📷 Screenshot
![Application Screenshot]()

---

## 🧠 Concepts Used
- Python functions.
- Lists and sets.
- Loops and conditionals.
- Random number generation.
- User input validation.
