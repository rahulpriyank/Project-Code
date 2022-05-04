dict = {
         "kursi" : "chair",
         "palang" : "bed",
         "akhbaar" : "newspaper"
}
print("Options are Here",dict.keys())
a = input("Enter the Hindi word :")
# if we search any item out of the key then it will throw an error
print("The meaning of the given hindi word is", dict[a])

# Below line syntax will not throw an error it will show the result as none
print("The meaning of the given hindi word is", dict.get(a))


