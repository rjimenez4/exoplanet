import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, Markdown

# 🔹 Explicació de la fórmula ESI dins del notebook
explanation = """
# 🌍 **Earth Similarity Index (ESI)**
L'ESI és un índex que mesura la similitud d'un exoplaneta amb la Terra en una escala de 0 a 1.
Es basa en la fórmula:

\[
ESI = \prod_{i} \left( 1 - \left| \frac{x_i - x_{Earth}}{x_i + x_{Earth}} \right| \right)^{w_i}
\]

On:
- \( x_i \) són les propietats de l'exoplaneta (radi, temperatura...).
- \( x_{Earth} \) són els valors equivalents per a la Terra.
- \( w_i \) són pesos ajustats segons la importància de cada paràmetre.

---
"""
display(Markdown(explanation))

# 🔹 Funció per calcular l'ESI per a un paràmetre
def esi_single(x, x_earth, weight):
    return (1 - abs((x - x_earth) / (x + x_earth))) ** weight if x > 0 else np.nan

# 🔹 Funció per calcular l'ESI total
def esi_calculator(radius, temp, radius_earth=1.0, temp_earth=288):
    w_radius = 0.57  # Pes per al radi
    w_temp = 0.43    # Pes per a la temperatura

    esi_r = esi_single(radius, radius_earth, w_radius)
    esi_t = esi_single(temp, temp_earth, w_temp)

    if np.isnan(esi_r) or np.isnan(esi_t):
        return np.nan  # Si falta alguna dada, retornem NaN
    return esi_r * esi_t

# 🔹 Descarregar dades en línia del NASA Exoplanet Archive (Caltech)
url = 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,pl_rade,pl_eqt+from+ps&format=csv'
df = pd.read_csv(url)

# 🔹 Comprovem quines columnes té el dataset
print("📌 Columnes disponibles al CSV:")
print(df.columns)

# 🔹 Filtrar només planetes amb les dades necessàries
df_filtered = df.dropna(subset=['pl_rade', 'pl_eqt'])

# 🔹 Calcular ESI per a cada exoplaneta
df_filtered['ESI'] = df_filtered.apply(lambda row: esi_calculator(row['pl_rade'], row['pl_eqt']), axis=1)

# 🔹 Mostrar els 10 exoplanetes més semblants a la Terra
print("\n🌍 **Els 10 exoplanetes més semblants a la Terra segons l'ESI:**")
display(df_filtered[['pl_name', 'pl_rade', 'pl_eqt', 'ESI']].sort_values(by='ESI', ascending=False).head(10))

# 🔹 Identificar planetes sense prou dades
df_missing = df[df['pl_rade'].isna() | df['pl_eqt'].isna()]
print("\n⚠️ **Exoplanetes sense prou dades per calcular l'ESI:**")
display(df_missing[['pl_name', 'pl_rade', 'pl_eqt']])

# 🔹 Representació gràfica dels ESI calculats
plt.figure(figsize=(10, 5))
plt.hist(df_filtered['ESI'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.xlabel("Earth Similarity Index (ESI)")
plt.ylabel("Nombre d'exoplanetes")
plt.title("Distribució de l'ESI per als exoplanetes")
plt.show()
