from urllib.request import urlopen
"""
with open("spells.txt","r") as spellFile:
    #spell1  = spellFile.readline()
    #print(spell1)
    #print(1)
    print(spellFile.readlines())
    print(type(spellFile.readlines()))
"""


with open("spells.txt","r") as spellFile:
    for spell in spellFile:
        spell = spell.strip("\n")
        print(spell)
#spellFile.close

print(1)
page1 = urlopen("http://olympus.realpython.org/profiles/aphrodite")
print(1.5)
page = urlopen("http://roll20.net/compendium/dnd5e/Prestidigitation")
print(2)
html_bytes = page.read()
print(3)
html = html_bytes.decode()
print(4)
print(html)
print(5)
