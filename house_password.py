def checkio(data):
#All flags are false at the beginning
    uppercase=False
    lowercase=False
    digit=False
#check the minimum length of the password
    if len(data)<10:
        return False
    else:
#check every condition that password should met
        for character in data:
            if character.isdigit():
                digit=True
            if character.isupper():
                uppercase=True
            if character.islower():
                lowercase=True
#If all flags are true then this will mean that the password met all the conditions
        return uppercase and lowercase and digit


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
