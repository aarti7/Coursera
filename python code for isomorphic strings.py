string1 = "Hi, I am Paul."
string2 = "Hi, I am Mike."
string3 = "Hi, I am Paula"#Same length as string 1, except . is replaced by a"
string4 = "Hi, I am Paul."
string5 = "Hi, I am Amber."

def Checkisomorphicstrings(string1, string2):
    if len(string1) == len(string2):
        print "The two strings are same length; i.e.",len(string1)
        k=0
        for i in range(len(string1)):
                if string1[k] == string2[k]:
                    if k ==len(string1)-1:
                        print "And these strings are isomorphic"
                    else:
                        k +=1
                else:
                    print "But the strings got mismatched at", string1[k], "and", string2[k]
                    print "i.e. from", k, "th postions onwards."
                    print "hence they are NOT isomorphic"
                    break

    else:
        print "Two strings are not same length, hence not isomorphic" 
Checkisomorphicstrings(string1, string4)
