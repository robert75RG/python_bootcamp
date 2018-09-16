import re

post_code_patter = re.compile('\d{2}-\d{3}')
email_pattern = re.compile('{\w\.}*@{\w')
date_patter = re.compile('\d{1,2} \w{3} \d{4}')
with open('input.txt') as f:
    tekst = f.read()
    cody = post_code_patter.findall(tekst)

    data = date_patter.findall(tekst)
    print(cody)
    print(data)
