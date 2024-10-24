```python
class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift
        self.const = 64
 
    def encode(self, st):
        self.st = st
        self.ans = ''
        self.st = self.st.upper()
        for i in self.st:
            if ord(i) < 65 or ord(i) > 90:
                self.ans += i
            elif ord(i) + self.shift > 90:
                self.ans += chr(ord(i) + self.shift - 26)
            else:
                self.ans += chr(ord(i) + self.shift)
        return self.ans.upper()
        
        
    def decode(self, st):
        self.st = st
        self.ans = ''
        for i in self.st:
            if ord(i) < 65 or ord(i) > 90:
                self.ans += i
            elif ord(i) - self.shift < 65:
                self.ans += chr(ord(i) - self.shift + 26)
            else:
                self.ans += chr(ord(i) - self.shift)
        return self.ans
c = CaesarCipher(5)
print(c.decode('HTIJBFWX'))

```
``` python
    class RomanNumerals:
    @staticmethod
    def to_roman(val):
        st = ''
        while val >= 1000:
            val -= 1000
            st += 'M' 
        while val >= 900:
            val -= 900
            st += 'CM'
        if val >= 500:
            while val >= 500:
                val -= 500
                st += 'D'
        if val >= 400:
            val -= 400
            st += 'CD'
        if val >= 100:
            while val >= 100:
                val -= 100
                st += 'C'
        
        while val >= 90:
            val -= 90
            st += 'XC'
        if val >= 50:
            while val >= 50:
                st += 'L'
                val -= 50
        if val >= 40:
            val -= 40 
            st += 'XL'
        while val >= 10 :
            st += 'X'
            val -= 10
        if val == 9:
            val -= 9
            st += 'IX'
        elif val == 4:
            val -= 4
            st += 'IV'
        else:
            while val >= 5:
                st += 'V'
                val -= 5
        while val >= 1:
            st += "I"
            val -= 1
        return st
    @staticmethod
    def from_roman(roman):
        roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        # Переменная для хранения результата
        decimal_value = 0
        prev_value = 0  # Переменная для хранения предыдущего значения

        # Перебираем символы строки справа налево
        for char in reversed(roman):
            current_value = roman_numerals[char]

            # Если текущее значение меньше предыдущего, то вычитаем его
            if current_value < prev_value:
                decimal_value -= current_value
            else:
                decimal_value += current_value

            
            prev_value = current_value

        return decimal_value


        

c = RomanNumerals
print(c.from_roman('MXI'))

```