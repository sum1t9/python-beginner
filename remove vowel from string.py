def remvowel(string):
    vowel=('a','e','i','o','u','A','E','I','O','U')
    for x in string:
        if x in vowel:
            string=string.replace(x,"")

    print(string)
string="Geeks For Geeks is An CS Portal"
remvowel(string)