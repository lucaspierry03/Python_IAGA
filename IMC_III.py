paciente = input("Nome do paciente........: ")
pc = float(input("Peso.................: "))
alt = float(input("Altura...............: "))
vlr_IMC = pc / (alt ** 2)

if (vlr_IMC < 18.5):
    interpretacao = "Magreza"
elif (vlr_IMC < 25.0):
    interpretacao = "Normal"
elif (vlr_IMC < 30.0):
    interpretacao = "Sobrepeso"
elif (vlr_IMC < 40.0):
    interpretacao = "Obesidade"
else:
    interpretacao = "Obesidade grave"

print()
print(f"Nome do Paciente: {paciente}")
print(f"Peso Corporal...: {pc:.3f} kgs")
print(f"Altura..........: {alt:.2f} metros")
print(f"Valor do IMC.....: {vlr_IMC:.2f} ({interpretacao})")