
import re 
pattern =r"colour"
text_1 = "My favourite colour is Red.I love blue colour as well "
text_2 =re.sub(pattern,'color',text_1,count=3)
#text_2 =re.sub(pattern,'color',text_1,count=3)
print(text_2)