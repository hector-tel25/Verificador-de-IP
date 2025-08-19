import tkinter as tk
from tkinter import ttk, messagebox
import ipaddress

def set_resultado(texto, color="black"):
    etiqueta_resultado.config(text=texto, fg=color)

def verificar_ip(*_):
    red_input = entrada_red.get().strip()
    ip_input = entrada_ip.get().strip()

    if not red_input or not ip_input:
        messagebox.showerror("Error", "Completa ambos campos: Red y Dirección IP.")
        set_resultado("")
        detalle_var.set("")
        return

    try:
        red = ipaddress.ip_network(red_input, strict=False)
    except ValueError as e:
        messagebox.showerror("Error en la red (CIDR)", f"⚠️ Entrada inválida:\n{e}")
        set_resultado("")
        detalle_var.set("")
        return

    try:
        ip = ipaddress.ip_address(ip_input)
    except ValueError as e:
        messagebox.showerror("Error en la IP", f"⚠️ Entrada inválida:\n{e}")
        set_resultado("")
        detalle_var.set("")
        return

    # Ayuda si se mezclan familias (IPv4 vs IPv6)
    if red.version != ip.version:
        set_resultado("⚠️ La red y la IP son de familias distintas (IPv4 vs IPv6).", "orange")
        detalle_var.set(f"Red: {red} ({'IPv4' if red.version == 4 else 'IPv6'})  |  "
                        f"IP: {ip} ({'IPv4' if ip.version == 4 else 'IPv6'})")
        return

    if ip in red:
        set_resultado(f"✅ La IP {ip} SÍ pertenece a la red {red}", "green")
    else:
        set_resultado(f"❌ La IP {ip} NO pertenece a la red {red}", "red")

    # Pequeño resumen de la red
    info = [f"Prefijo: /{red.prefixlen}", f"Familia: {'IPv4' if red.version == 4 else 'IPv6'}"]
    if red.version == 4:
        info.append(f"Broadcast: {red.broadcast_address}")
        info.append(f"Dirección de red: {red.network_address}")
    detalle_var.set("  |  ".join(info))

def limpiar():
    entrada_red.delete(0, tk.END)
    entrada_ip.delete(0, tk.END)
    set_resultado("")
    detalle_var.set("")
    entrada_red.focus_set()

# ---- Ventana principal ----
ventana = tk.Tk()
ventana.title("Verificador de IP en Red")
ventana.geometry("520x280")
ventana.resizable(False, False)

# Tema ttk 
try:
    style = ttk.Style()
    style.theme_use("clam")
except Exception:
    pass  # Si el tema no está disponible, seguimos con el predeterminado

frame = ttk.Frame(ventana, padding=15)
frame.pack(fill="both", expand=True)

# Red
ttk.Label(frame, text="Red (formato CIDR):").pack(pady=(0, 4), anchor="w")
entrada_red = ttk.Entry(frame, width=40)
entrada_red.pack()
entrada_red.insert(0, "192.168.1.0/24")  # ejemplo

# IP
ttk.Label(frame, text="Dirección IP:").pack(pady=(10, 4), anchor="w")
entrada_ip = ttk.Entry(frame, width=40)
entrada_ip.pack()
entrada_ip.insert(0, "192.168.1.50")  # ejemplo

# Botones
botones = ttk.Frame(frame)
botones.pack(pady=12)
ttk.Button(botones, text="Verificar", command=verificar_ip).pack(side="left", padx=5)
ttk.Button(botones, text="Limpiar", command=limpiar).pack(side="left", padx=5)

# Resultado 
etiqueta_resultado = tk.Label(frame, text="", wraplength=480, font=("Arial", 11))
etiqueta_resultado.pack(pady=(6, 2), anchor="w")

# Detalle adicional 
detalle_var = tk.StringVar(value="")
tk.Label(frame, textvariable=detalle_var, fg="gray25", wraplength=480, justify="left").pack(anchor="w")

# Bind Enter para verificar
entrada_red.bind("<Return>", verificar_ip)
entrada_ip.bind("<Return>", verificar_ip)


entrada_red.focus_set()

ventana.mainloop()
