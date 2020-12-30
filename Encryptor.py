
# This program encrypts and decrypts texts. The key and the text come from the user the user

word = input("Text: ")
key = int(input("Key (integer between 0-31): "))
if (key < 0) or (key > 31):
    print("Invalid key entry")
    exit(1)

text = []
for i in word:
    char_num = ord(i)
    m_num = (char_num ^ key)
    text.append(chr(m_num))

print(*text, sep="")
