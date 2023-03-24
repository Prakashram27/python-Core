def nth_root(radicant,n):
    return radicant ** (1/n)

def original_suffix(value):
    s = str(value)
    if s.endswith('11'):
        return 'th'
    elif s.endswith('12'):
        return 'th'
    elif s.endswith('13'):
        return 'th'
    elif s.endswith('1'):
        return 'sd'
    elif s.endswith('2'):
        return 'nd'
    elif s.endswith('3'):
        return 'rd'
    return 'th'

def ordinal(value):
    return str(value)+ original_suffix(value)

def display_nth_root(radicand,n):
    root = nth_root(radicand,n)
    message = "The " + ordinal(n) + " root of "+ str(radicand) + 'is' + str(root)
    print(message)
    
display_nth_root(64,4)



def even_or_odd(n):
    if n%2 == 0:
        print('even')
        return
    print('Odd')

w = even_or_odd(31)
print(w)
print(w is None)