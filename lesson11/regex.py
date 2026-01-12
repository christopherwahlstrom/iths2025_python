import re

pattern = r"a.c"
text = "abc axc a-c aqr"
print(re.findall(pattern, text))

pattern = r"\d+"
text = "123 45 6789 abc 1 99999"
print(re.findall(pattern, text))

pattern = r"[^abc]+"
text = "123abc456dEf"
print(re.findall(pattern, text))

pattern = r"\S+"
text = "Hello world!\nProgramming in python"
print(text)
print(re.findall(pattern, text))

pattern = r"(abc)"
text = "abcabcccxx"
print(re.search(pattern, text).group())

pattern = r"apple|pear|orange"
text = "There are one apple and one orange"
print(re.findall(pattern, text))

pattern = r"(abc)"
text = "abcabcccxx"
print(re.search(pattern, text))
print(re.search(pattern, text).group())
print(re.search(pattern, text).start())
print(re.search(pattern, text).end())
print(re.search(pattern, text).span())

pattern = r"Hello"
text = "Hello world!"
print(re.match(pattern, text).group())

pattern = r"Hello"
text = "world! Hello"
match = re.match(pattern, text)
if match:
    print(match.group())
else:
    print("No match")

text = "There are 42 apple and 45 orange"
for i in re.finditer(r"\d+", text):
    print(i.group(), i.start())

text = "Call me on 07083725999"
print(re.sub(r"\d+", "#", text))

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b"
text = "Send me an email @ bobbo@bobbo.se"
print(re.sub(pattern, "[redacted]", text))

ip = r"\b\d{1,3}(\.\d{1,3}){3}\b"
html = r"<.*?>"
password = r"(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}"
personnr = r"\b\d{6}-\d{4}\b"

