def Palindrom(S):
    
    if len(S) <= 1:
        return True
    if S[0] == S[-1]:
        return Palindrom(S[1:-1])
    else:
        return False

strings = ["radar", "level", "hello", "madam", "python"]
for s in strings:
    print(f"Строка '{s}' является палиндромом: {Palindrom(s)}")
