from collections import Counter


def generateDocument(characters, document):
    characters_dict = Counter(characters)
    document_dict = Counter(document)
    for each in document_dict.keys():
        if each not in characters_dict.keys() or characters_dict[each] < document_dict[each]:
            return False
    return True


print(generateDocument("Bste!hetsi ogEAxpelrt x ","AlgoExpert is the Best!"))
print(generateDocument("a hsgalhsa sanbjksbdkjba kjx",""))
print(generateDocument(" ","hello"))