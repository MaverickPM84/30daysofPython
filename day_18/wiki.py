import wikipedia

result = wikipedia.summary("Python programming language", sentences=3)
print(result)


print("______________________")

search_result = wikipedia.search("Galaxy", results = 3)
print("______________________")


print(search_result)