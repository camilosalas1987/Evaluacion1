#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. CLASE PRODUCTO

class Producto:
    def __init__(self, id, nombre, descripcion, cantidad, precio):
        """
        Inicializa un nuevo objeto Producto con los atributos dados.

        Parámetros:
        - id (int): Identificador único para el producto.
        - nombre (str): Nombre del producto.
        - descripcion (str): Descripción detallada del producto.
        - cantidad (int): Cantidad del producto disponible.
        - precio (float): Precio del producto.
        """
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        """Retorna el id del producto."""
        return self.id

    def obtener_nombre(self):
        """Retorna el nombre del producto."""
        return self.nombre

    def obtener_descripcion(self):
        """Retorna la descripción del producto."""
        return self.descripcion

    def obtener_cantidad(self):
        """Retorna la cantidad disponible del producto."""
        return self.cantidad

    def obtener_precio(self):
        """Retorna el precio del producto."""
        return self.precio

    def modificar_nombre(self, nuevo_nombre):
        """Modifica el nombre del producto."""
        self.nombre = nuevo_nombre

    def modificar_descripcion(self, nueva_descripcion):
        """Modifica la descripción del producto."""
        self.descripcion = nueva_descripcion

    def modificar_cantidad(self, nueva_cantidad):
        """Modifica la cantidad del producto. La nueva cantidad debe ser un entero no negativo."""
        if nueva_cantidad >= 0:
            self.cantidad = nueva_cantidad
        else:
            print("Error: La cantidad no puede ser negativa.")

    def modificar_precio(self, nuevo_precio):
        """Modifica el precio del producto. El nuevo precio debe ser un valor no negativo."""
        if nuevo_precio >= 0:
            self.precio = nuevo_precio
        else:
            print("Error: El precio no puede ser negativo.")


# In[2]:


#USO DE CLASE PRODUCTO: OBTENER VALORES

# Definición de los productos usando la clase Producto con las abreviaturas especificadas

# Producto 1: Lápiz
p1 = Producto(1, "Lápiz", "Lápiz HB para dibujo", 100, 0.50)

# Producto 2: Cuaderno
p2 = Producto(2, "Cuaderno", "Cuaderno espiral de 100 hojas", 50, 2.00)

# Producto 3: Borrador
p3 = Producto(3, "Borrador", "Borrador blanco pequeño", 150, 0.75)

# Imprimiendo la información de los productos para verificar
print(f"Producto: {p1.obtener_nombre()}, Descripción: {p1.obtener_descripcion()}, Precio: {p1.obtener_precio()}")
print(f"Producto: {p2.obtener_nombre()}, Descripción: {p2.obtener_descripcion()}, Precio: {p2.obtener_precio()}")
print(f"Producto: {p3.obtener_nombre()}, Descripción: {p3.obtener_descripcion()}, Precio: {p3.obtener_precio()}")


# In[3]:


# USO: modificar el precio y la cantidad
p1.modificar_precio(0.55)
p1.modificar_cantidad(150)
print(f"Actualización - Precio: {p1.obtener_precio()}, Cantidad: {p1.obtener_cantidad()}")


# In[ ]:




