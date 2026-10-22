nagoriyuki=["maria@gmail.com", "pedro@outlook.com", "juan@gmail.com","ana@empresa.es", "luis@outlook.com"]
print("Correos registrados:", nagoriyuki)

may=[]
for op in nagoriyuki:
    #Acordarse del split
    goldlewis=op.split('@')
    may.append(goldlewis[1])

print("--- Dominios Únicos Detectados (Set) ---")
chipp = set(may)

print("Total de dominios diferentes:", len(chipp))
for op in chipp:
    print("-", op)

