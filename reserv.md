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