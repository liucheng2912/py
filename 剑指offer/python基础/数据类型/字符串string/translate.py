intab='adfas'
outtab='12345'
transtab = str.maketrans(intab,outtab)
st = 'just do it'
print(st.translate(transtab))