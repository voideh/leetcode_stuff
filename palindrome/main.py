# non-string solution to numerical palindromes
def len_num(x: int) -> int:
    curr = x
    cnt = 0
    while curr != 0:
        curr //= 10
        cnt += 1
    return cnt

def num_rev(x: int) -> int:
    n = 0
    curr = x
    cnt = len_num(x)
    # effectively rebuild the number in reverse
    while cnt > 0:
        n += (curr % 10)*(10**(cnt-1))
        curr //= 10
        cnt -= 1
    return n

def is_palindrome(x: int) -> bool:
    # negatives are never palindromes
    if x < 0: return False
    return x == num_rev(x)