invitados = {"Paul", "Koraima", "Andres", "Emilio", "Andrea"}

confirmaciones = {"Paul", "Koraima","Emilio"}

# if "Koraima" in confirmaciones:
#     print("Confirmo")
# else: 
#     print("No confirmo")


#print(f"Personas que no han confirmado:{no_confirmado}")

#Todos los invitados, (Confirmaciones y no confirmaciones)
todos_los_invitados = invitados.union(confirmaciones) 
print(f"todos los invitados: {todos_los_invitados}")
print(f"Confirmados: {confirmaciones}")
no_confirmados = invitados - confirmaciones
print(f"No confirmados: {no_confirmados}")