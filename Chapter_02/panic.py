phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
plist2 = plist.copy()

for i in range(4):
    plist.pop()

plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

on = plist2[1:3]
on.extend(plist2[5:3:-1])
on.extend(plist2[7:5:-1])

new_new_phrase = ''.join(on)
print("Shiny and new:")
print(new_new_phrase)
