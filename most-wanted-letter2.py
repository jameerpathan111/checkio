import re
def checkio(text):
    count=dict()
    for char in text:
        char=char.lower()
        x=re.findall('[a-z]',char)
        if len(x)>0:
            count[char]=count.get(char,0)+1
    lst=list()
    for keys,values in list(count.items()):
        tmp=values,keys
        lst.append(tmp)
    lst.sort(reverse=True)
    maxlist=list()
    numMax,letterMax=max(lst)
    for values,keys in lst:
        if values==numMax:
            tmp=keys,values
            maxlist.append(tmp)
    maxlist.sort()
    tmp=maxlist[0]
    return tmp[0]

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
