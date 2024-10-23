def solve(s):
    const = 96
    summ = 0
    for i in range(len(s)):
        i = 0
        while not s[i] in "aeiou":
            print(i)
            i += 1
            summ += ord(s[i]) - const 
    return summ
