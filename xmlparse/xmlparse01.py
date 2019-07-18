import xml.etree.ElementTree as ET

tree = ET.parse("moviesdat.xml")
root = tree.getroot()

print(root.tag) # this should return "collection"

print(root.attrib) # returns empty dictionary
for child in root:
    print(child.tag, child.attrib)

for elem in root.iter():
            print(elem.tag)

print(ET.tostring(root, encoding="utf8").decode("utf8"))

for movie in root.iter("movie"):
    print(movie.attrib)
#x=input("Press Enter to continue")
print("Print the descriptions of each movie")
for description in root.iter('description'):
    print(description.text)

print("Movies that came out in 1992")
for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)

print("Movies available in multiple formats")
for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
    print(movie.attrib)
