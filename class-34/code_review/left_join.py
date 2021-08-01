hash1={'fond': 'enamored','wrath': 'anger','diligent': 'employed','outfit':'grab','guide':'usher' }
hash2={'fond': 'averse','wrath': 'diligent','diligent': 'idle','guide':'follow','flow':'jam' }

def left_join(h1,h2):
    output = []
    for i,key in enumerate(h1):
        second_value = h2[key] if key in h2 else None
        appended_array = [key, h1[key], second_value]
        output.append(appended_array)
    return output

print(left_join(hash1,hash2))



