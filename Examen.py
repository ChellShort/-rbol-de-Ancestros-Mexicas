class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

def find_lca(root, node1, node2):
    if root is None:
        return None

    if root.name == node1 or root.name == node2:
        return root

    found_nodes = []
    for child in root.children:
        lca = find_lca(child, node1, node2)
        if lca is not None:
            found_nodes.append(lca)

    if len(found_nodes) == 2:
        return root
    elif len(found_nodes) == 1:
        return found_nodes[0]
    else:
        return None

def find_previous_ancestor(root, target, previous_ancestor=None):
    if root is None:
        return None

    if root.name == target:
        return previous_ancestor

    for child in root.children:
        previous_ancestor = root
        result = find_previous_ancestor(child, target, previous_ancestor)
        if result is not None:
            return result

# Construye tu árbol genealógico aquí

raiz = TreeNode("Cuauhtémoc")
e1 = TreeNode("Xochitl")
e2 = TreeNode("Moctezuma")
e3 = TreeNode("Iztaccíhuatl")
e4 = TreeNode("Tonantzin")
e5 = TreeNode("Tlaloc")
e6 = TreeNode("Itzpapalotl")
e7 = TreeNode("Malinalli")
e8 = TreeNode("Xipe Totec")
e9 = TreeNode("Metztli")
e10 = TreeNode("Huitzilopochtli")
e11 = TreeNode("Tepoztecatl")
e12 = TreeNode("Atlacoya")
e13 = TreeNode("Cipactli")
e14 = TreeNode("Miquiztli")
e15 = TreeNode("Temachtiani")
e16 = TreeNode("Tlachinolli")
e17 = TreeNode("Amoxtli")
e18 = TreeNode("Tlatocatl")
e19 = TreeNode("Tezcatlipoca")
e20 = TreeNode("Cuetlaxochitl")
e21 = TreeNode("Xilatzin")
e22 = TreeNode("Ayuliyah")
e23 = TreeNode("Cuetzpallin")
e24 = TreeNode("Atl")
e25 = TreeNode("Yaotl")
e26 = TreeNode("Tochtli")
e27 = TreeNode("Ichtaca")
e28 = TreeNode("Xiuhtecuhtli")
e29 = TreeNode("Olin")
e30 = TreeNode("Tepaneca")
e31 = TreeNode("Tlahuicole")
e32 = TreeNode("Citlalicue")
e33 = TreeNode("Tezcatzoncatl")
e34 = TreeNode("Tlahuizcalpantecuhtli")
e35 = TreeNode("Teyacapan")
e36 = TreeNode("Mixcoatl")
e37 = TreeNode("Tepin")
e38 = TreeNode("Tepilhuan")
e39 = TreeNode("Temilotzin")
e40 = TreeNode("Xipilli")

raiz.children = [e1, e2]  
e1.children = [e3]
e2.children = [e4, e5]
e4.children = [e6, e7]
e5.children = [e8, e9]
e8.children = [e10, e11]
e9.children = [e12, e13]
e11.children = [e14, e15]
e15.children = [e16, e17]
e17.children = [e18, e19]
e18.children = [e20]
e19.children = [e21, e22]
e20.children = [e23, e24]
e22.children = [e25, e26]
e24.children = [e27, e28]
e28.children = [e29, e30]
e29.children = [e31, e32]
e32.children = [e33, e34]
e34.children = [e35, e36]
e36.children = [e37, e38]
e38.children = [e39, e40]

# Pedir el número de ancestros
while True:
  try:
    num_ancestros = int(input("Cuántos ancestros quieres encontrar? "))
    break
  except ValueError:
    print("Por favor ingresa un número válido")
    
# Crea una lista para almacenar los nombres de los ancestros
ancestros = []
for i in range(num_ancestros):
    ancestro = input(f"Ingresa el nombre del ancestro {i + 1}: ")
    
    # Verifica si el nombre ingresado está en el árbol genealógico
    if not any(ancestro in node.name for node in [raiz, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25, e26, e27, e28, e29, e30, e31, e32, e33, e34, e35, e36, e37, e38, e39, e40]):
        print(f"El nombre '{ancestro}' no se encontró en el árbol genealógico.")
        exit(1)
    
    ancestros.append(ancestro)

# Itera a través de los nombres de ancestros y encuentra el ancestro común más bajo
ancestro_anterior = None
for i in range(1, num_ancestros):
    node1 = ancestros[i - 1]
    node2 = ancestros[i]
    lca = find_lca(raiz, node1, node2)
    try:
        lca = find_lca(raiz, node1, node2)
        if lca:
            if lca.name == node1 or lca.name == node2:
                previous_ancestor = find_previous_ancestor(raiz, lca.name)
                if previous_ancestor:
                    ancestro_anterior = previous_ancestor.name
                else:
                    ancestro_anterior ="No se encontró un ancestro anterior"
            else:
                ancestro_anterior = lca.name
        else:
            ancestro_anterior = f"No se encontró un ancestro común para {node1} y {node2}"
    except AttributeError as e:
        print(f"Error: {e}")

if ancestro_anterior is not None:
    print(ancestro_anterior)
