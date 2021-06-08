# file = open('../assets/spam.txt')
# # print(file)
# # print(type(file))
# print(file.read())
# file.close()

# file = open('../assets/spam.txt')
# print(file.readlines())
# file.close()

with open('../assets/spam.txt') as file:
    print(file.read())

with open('../assets/spam.txt') as file:
    print(file.readlines())




with open('../assets/brain.jpg', 'rb') as img:
    img_content = img.read()

with open('../assets/brain.copy.jpg', 'wb') as img_copy:
    print(len(img_content))
    img_copy.write(img_content[:len(img_content)//2])
