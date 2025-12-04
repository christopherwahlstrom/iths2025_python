# pylint: disable=missing-module-docstring

#FizzBuzz

#Klassisk uppgift. Loopa genom 1-100 med följande regler:



# ● Om talet är delbart med 3, skriv ut "Fizz".

#● Om talet är delbart med 5, skriv ut "Buzz".

#● Om talet är delbart med både 3 och 5, skriv ut
#"FizzBuzz".

#● Annars, skriv ut talet självt.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

