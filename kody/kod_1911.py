line = " pvanecek ; kiv.zcu.cz ; Vanecek;PETR "
line = line.strip()
data = line.split(';')
output = f"{data[3].capitalize()} {data[2].upper()} <{data[0].lower()}@{data[1]}>"
print(output)