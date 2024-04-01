#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#3 MENÚ 

#invocar clase producto e invocar clase inventario 
from Eval1_1mod_producto import Producto
from Eval1_2mod_inventario import Inventario


# In[ ]:


def mostrar_menu():
    """
    Imprime las opciones disponibles en el menú del sistema de gestión de inventario.
    """
    print("\nMenú del Sistema de Gestión de Inventario")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Modificar producto")
    print("4. Buscar producto por ID")
    print("5. Listar todos los productos")
    print("6. Salir")

def main():
    """
    Punto de entrada principal del programa. Crea una instancia de Inventario y procesa
    las entradas del usuario para interactuar con el sistema de gestión de inventario.
    """
    inventario = Inventario()  # Instancia de la clase Inventario.

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Agregar producto
            id = int(input("ID del producto: "))
            nombre = input("Nombre del producto: ")
            descripcion = input("Descripción del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id, nombre, descripcion, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            # Eliminar producto
            id = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id)
        elif opcion == '3':
            # Modificar producto
            id = int(input("ID del producto a modificar: "))
            nombre = input("Nuevo nombre (dejar en blanco para no modificar): ")
            descripcion = input("Nueva descripción (dejar en blanco para no modificar): ")
            cantidad = input("Nueva cantidad (dejar en blanco para no modificar): ")
            precio = input("Nuevo precio (dejar en blanco para no modificar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.modificar_producto(id, nombre, descripcion, cantidad, precio)
        elif opcion == '4':
            # Buscar producto por ID
            id = int(input("ID del producto a buscar: "))
            producto = inventario.buscar_producto(id)
            if producto:
                print(f"Producto encontrado: ID {producto.obtener_id()}, Nombre {producto.obtener_nombre()}, Descripción {producto.obtener_descripcion()}, Cantidad {producto.obtener_cantidad()}, Precio {producto.obtener_precio()}")
            else:
                print("Producto no encontrado.")
        elif opcion == '5':
            # Listar todos los productos
            inventario.listar_productos()
        elif opcion == '6':
            # Salir del programa
            print("Saliendo del sistema de gestión de inventario.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()


# In[ ]:




