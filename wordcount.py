def word_count(str):
    count = dict()
    words = str.split()
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    return count
print( word_count("ore no nawa vishal des nawa des "))


'''def word_count(str ):
 
    count = dict()
    words = str.split()
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    return count
print( word_count(str(input("enter the sentence")))) '''
 #   str q=input("enter the sentence")
 
"""def word_count(str ):
    str = "how is the whether how is life"
    count = dict()
    words = str.split()
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    return count
print( word_count(str))
 #   str q=input("enter the sentence") """
  