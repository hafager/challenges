batman = "NAANAAANNNAANAAAANANANANAAAAAAAANNAANAAANAAANANNAAAAAAAANNNAANAAAAANAANAAAA"

binary = ""
for i in batman:
    if i == "N":
        binary += "B"
    else:
        binary += "A"

print binary

print len(binary)
