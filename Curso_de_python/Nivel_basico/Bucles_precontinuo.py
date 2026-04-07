# for i in range(10): 
#     if i == 5: 
#         break 
#     print(i+1)

# numeros = [1,3,5,8,9,11,13,15]
# objetivo = 7 

# for i in numeros:
#     if i == objetivo: 
#         print(f"Numero {objetivo} encontrado.")
#         break 
# else: 
#  print(f"Numero no encontrado")


numeros = [1,2,3,4,5,6,7,8,9]

for i in numeros: 
    if i % 2==0: 
        continue
    else: 
        print(i)