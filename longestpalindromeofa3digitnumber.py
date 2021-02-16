

def longestPalindrome():
    start = 999
    end = 999

    palindrome = 0
    for a in range(start, 100, -1):
        for b in range(end, 100, -1):
            mul = a * b
            if(mul > palindrome):
                s = str(mul)
                if(s == s[::-1]):
                    palindrome = mul
    return palindrome

print(longestPalindrome())