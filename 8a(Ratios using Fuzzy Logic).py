# Ratios using Fuzzy Logic
!pip install fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
s1="I love fuzzywuzzys"
s2="I am loving fuzzywuzzys"
print("fuzzywuzzy ratio: ",fuzz.ratio(s1,s2))
print("fuzzywuzzy partial ratio: ",fuzz.partial_ratio(s1,s2))
print("fuzzywuzzy token sort ratio: ",fuzz.token_sort_ratio(s1,s2))
print("fuzzywuzzy token set ratio: ",fuzz.token_set_ratio(s1,s2))
#for process library
query="fuzzs for fuzzys"
choices=['fuzzy for fuzzy','fuzzy fuzzy','g. for fuzzys']
print("List of ratios: ")
print(process.extract(query,choices),'\n')
print("Best among the above list: ",process.extractOne(query, choices))