
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Gráfica de una función lineal")

st.sidebar.title("Diego Jesus Ramirez Rodriguez")
st.sidebar.write("Graficador de funciones lineales")

st.write("Modifica los valores de m y b para observar cómo cambia la gráfica.")

m = st.number_input("Valor de m:", value=2.0)
b = st.number_input("Valor de b:", value=1.0)

x = np.linspace(-10, 10, 100)
y = m * x + b

fig, ax = plt.subplots()

ax.plot(x, y, color="blue", label=f"y = {m}x + {b}")

ax.set_title("Función lineal")
ax.set_xlabel("x")
ax.set_ylabel("y")

ax.grid(True)
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)
ax.legend()

st.pyplot(fig)

st.write(f"**Ecuación:** y = {m}x + {b}")
