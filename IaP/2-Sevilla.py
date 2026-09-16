lluvia = "La lluvia en Sevilla es una maravilla"
palabra1 = "lluvia"
palabra2 = "pura"
palabra3 = "villa"

if palabra1 in lluvia and palabra2 in lluvia and palabra3 in lluvia:
    print("Efectivamente, la lluvia en Sevilla es una maravilla")
else:
    print("Pues no, no lo es")

frase=lluvia.split("en ")[1]

print(frase)