# task 2 , 3 , 9

def draw(max_num, current_ammount):
    if current_ammount < max_num:
        if current_ammount > 0:
            print("*" * current_ammount)
        draw(max_num, current_ammount + 1)


def draw_plus(max_num, current_ammount):
    if current_ammount < max_num:
        print(current_ammount * "*" , (max_num*2 - current_ammount*2) * " ", current_ammount * "*")
        draw_plus(max_num, current_ammount + 1)

draw(10,0)
draw(10,3)
    
draw_plus(10,0)
draw_plus(10,3)
        
def recursive_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return recursive_palindrome(word[1:-1])
    else:
        return False

print(recursive_palindrome("racecar"))
print(recursive_palindrome("anna"))
print(recursive_palindrome("test"))
print(recursive_palindrome("HELLO"))

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))
print(factorial(4))