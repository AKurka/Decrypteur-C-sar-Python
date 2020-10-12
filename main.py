MessageCrypte="oh kdfkdjh yrxv shuphwwudlw gdvvxuhu od frqilghqwldolwh vlpsohphqw"
lg=len(MessageCrypte)
MessageClair=""
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cle=3

for i in range(lg):
    if MessageCrypte[i]==' ':
        MessageClair+=' '
    else:
        lettre = (alphabet.index(MessageCrypte[i])-cle)%26
        MessageClair += alphabet[lettre]

print(MessageClair)