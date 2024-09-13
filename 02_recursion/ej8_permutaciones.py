# Ejercicio: Permutaciones
# Definir la función permutaciones, que dada una lista de enteros, retorne una lista de listas de enteros, donde cada lista es cada una de las posibles permutaciones de la lista original.

# Por ejemplo: permutaciones([6,2,3]) = [[6,2,3], [6,3,2], [2,3,6], [2,6,3], [3,2,6], [3,6,2]]


# use backtracking
def permutaciones_con_backtracking(lista):
    def permutaciones_interna(lista, permutacion_actual, permutaciones):
        if len(lista) == 0:
            permutaciones.append(permutacion_actual)
            return
        for i in range(len(lista)):
            permutaciones_interna(
                lista[:i] + lista[i + 1 :],
                permutacion_actual + [lista[i]],
                permutaciones,
            )

    permutaciones = []
    permutaciones_interna(lista, [], permutaciones)
    return permutaciones


print(
    permutaciones_con_backtracking([6, 2, 3])
)  # [[6, 2, 3], [6, 3, 2], [2, 3, 6], [2, 6, 3], [3, 2, 6], [3, 6, 2]]
