# pylint: disable=missing-module-docstring

#Password spraying:

#Ladda ner password_spraying.py från uppgiftsmaterial.

#Kontrollera om någon utav lösenorden i password_list matchar lösenordet för en user i user_credentials

#Skriv resultatet till fil (och i konsolen) med varje lösenord per user och om det lyckades eller inte.

#Exempel:user1: 123456 -> failed user1: Welcome123 -> failed

from password_spraying import user_credentials, password_list

with open("results.txt", "w", encoding="utf-8") as file:
    for user, correct_password in user_credentials.items():
        for password in password_list:
            if password == correct_password:
                result = f"{user}: {password} -> success"
            else:
                result = f"{user}: {password} -> failed"
            
            print(result)
            file.write(result + "\n")


