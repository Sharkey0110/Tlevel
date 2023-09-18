
char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

products = {
    "cost": 32.67,
    "sell": 45,
    "stock": 1200
    }

def triangle(base, height):
    return (base*height)/2

def power(voltage, current):
    return voltage * current

def add(a, b):
    return a + b

def days(year):
    return year * 365

def morse(word):
    word = word.upper()
    morse = ""
    for i in word:
        morse += char_to_dots[i]
    return morse

def sales(products):
    gain = products["sell"] * products["stock"]
    loss = products["cost"] * products["stock"]
    return round(gain - loss,2)

print(sales(products))
