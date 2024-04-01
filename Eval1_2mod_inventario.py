#!/usr/bin/env python
# coding: utf-8

# In[4]:


#2 CLASE INVENTARIO 

#INVOCAR CLASE PRODUCTO 
from Eval1_1mod_producto import Producto

#DEFINICIÓN CLASE INVENTARIO 

class Inventario:
    def __init__(self):
        """
        Inicializa el inventario como un diccionario vacío.
        Los productos se almacenan con su id como clave.
        """
        self.productos = {}

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al inventario.
        Args:
            producto (Producto): El producto a agregar.
        """
        if producto.obtener_id() in self.productos:
            print(f"Error: Ya existe un producto con el id {producto.obtener_id()} en el inventario.")
        else:
            self.productos[producto.obtener_id()] = producto
            print(f"Producto {producto.obtener_nombre()} agregado al inventario con éxito.")

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario por su id.
        Args:
            id_producto (int): El id del producto a eliminar.
        """
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con id {id_producto} eliminado del inventario.")
        else:
            print(f"Error: No se encuentra el producto con id {id_producto}.")

    def modificar_producto(self, id_producto, nuevo_nombre=None, nueva_descripcion=None, nueva_cantidad=None, nuevo_precio=None):
        """
        Modifica los atributos de un producto en el inventario.
        Args:
            id_producto (int): El id del producto a modificar.
            nuevo_nombre (str): El nuevo nombre del producto.
            nueva_descripcion (str): La nueva descripción del producto.
            nueva_cantidad (int): La nueva cantidad del producto.
            nuevo_precio (float): El nuevo precio del producto.
        """
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nuevo_nombre is not None:
                producto.modificar_nombre(nuevo_nombre)
            if nueva_descripcion is not None:
                producto.modificar_descripcion(nueva_descripcion)
            if nueva_cantidad is not None:
                producto.modificar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.modificar_precio(nuevo_precio)
            print(f"Producto con id {id_producto} modificado con éxito.")
        else:
            print(f"Error: No se encuentra el producto con id {id_producto} para modificar.")

    def buscar_producto(self, id_producto):
        """
        Busca y retorna un producto en el inventario por su id.
        Args:
            id_producto (int): El id del producto a buscar.
        Returns:
            Producto: El producto encontrado o None si no se encuentra.
        """
        return self.productos.get(id_producto, None)

    def listar_productos(self):
        """
        Imprime un listado de todos los productos en el inventario.
        Muestra la cantidad total de productos y el valor total del inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Listado de productos en el inventario:")
            total_valor = sum(producto.obtener_cantidad() * producto.obtener_precio() for producto in self.productos.values())
            for producto in self.productos.values():
                print(f"- ID: {producto.obtener_id()}, Nombre: {producto.obtener_nombre()}, Descripción: {producto.obtener_descripcion()}, Cantidad: {producto.obtener_cantidad()}, Precio: ${producto.obtener_precio()}")
            print(f"Total de productos: {len(self.productos)}. Valor total del inventario: ${total_valor:.2f}.")


# In[5]:


#PROBANDO AGREGAR PRODUCTOS AL INVENTARIO 

# Creando instancias de Producto
p1 = Producto(1, "Lápiz", "Lápiz HB para dibujo", 100, 0.50)
p2 = Producto(2, "Cuaderno", "Cuaderno espiral de 100 hojas", 50, 2.00)
p3 = Producto(3, "Borrador", "Borrador blanco pequeño", 150, 0.75)

# Creando una instancia de Inventario
mi_inventario = Inventario()

# Agregando los productos al inventario
mi_inventario.agregar_producto(p1)
mi_inventario.agregar_producto(p2)
mi_inventario.agregar_producto(p3)

# Opcional: Listando los productos para verificar su inclusión
mi_inventario.listar_productos()


# In[ ]:




