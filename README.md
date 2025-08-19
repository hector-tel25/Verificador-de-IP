# 🖧 Verificador de IP e

Aplicación de escritorio en **Python + Tkinter** que permite verificar si una dirección **IP** pertenece a una red en formato **CIDR**.  

Está pensada como una herramienta sencilla pero práctica para:  
- Estudiantes de redes  
- Administradores de sistemas  
- Técnicos que trabajan con direccionamiento IP  

---

## ✨ Características  

- ✅ Verifica si una dirección IP pertenece a una red en formato **CIDR**  
- ✅ Compatible con **IPv4 e IPv6**  
- ✅ Validación de entradas con mensajes de error claros  
- ✅ Colores en el resultado:  
  - 🟢 Verde → la IP pertenece a la red  
  - 🔴 Rojo → la IP **no** pertenece a la red  
  - 🟠 Naranja → familias distintas (IPv4 vs IPv6)  
- ✅ Ejemplos precargados para guiar al usuario  
- ✅ Resumen adicional de la red (prefijo, familia, dirección de red y broadcast en IPv4)  
- ✅ Botón **Limpiar** para restablecer los campos  
- ✅ Interfaz moderna con `ttk` (multiplataforma)  

---

## 📷 Captura de pantalla  

<img width="530" height="318" alt="Captura de pantalla_20250819_175932" src="https://github.com/user-attachments/assets/159c563e-7f73-482f-8def-e074d4ec797c" />

#🛠️ Requisitos

Python 3.7 o superior

Librerías estándar de Python (tkinter, ipaddress)
👉 No es necesario instalar dependencias adicionales
