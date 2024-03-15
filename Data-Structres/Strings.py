txt_1 = 'Hello World!'
'Hello World!'

txt_2 = "HELLO WORLD!"
'HELLO WORLD!'

long_txt = """
           Hello World,
           Welcome DSMLBC!
           """
'Hello World, \n Welcome DSMLBC!'

#####################
# Indexing & Slicing
#####################

txt_1[0]
'H'

txt_1[-1]
'!'

txt_1[1:4]
'ell'

txt_1[:5]
'Hello'

#####################
# String Methods
#####################

len(txt_1)
12

txt_1.upper()
'HELLO WORLD!'

txt_2.lower()
'hello world!'

txt_1.replace("World", "Era")
'Hello Era!'

txt_1.split()
['Hello', 'World!']

' Hello World! '.strip()
'Hello World!'

'hello world!'.capitalize()
'Hello world!'