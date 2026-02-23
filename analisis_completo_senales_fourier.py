import numpy as np
import matplotlib.pyplot as plt

# ============================================
# ANÁLISIS COMPLETO DE SEÑALES EN TIEMPO Y FRECUENCIA
# Incluye: Pulso rectangular, Escalón, Senoidal
# Incluye: Magnitud Y Fase del espectro
# Incluye: Propiedades (linealidad, desplazamiento, escalamiento)
# ============================================

print("="*60)
print("ANÁLISIS DE SEÑALES EN DOMINIO DEL TIEMPO Y FRECUENCIA")
print("="*60)

# --- PARÁMETROS GENERALES ---
Fs = 1000  # Frecuencia de muestreo (Hz)
T = 2      # Duración (segundos) - más larga para ver mejor las propiedades
N = int(Fs * T)  # Número de muestras
t = np.arange(-T/2, T/2, 1/Fs)  # Tiempo centrado en cero (mejor para visualizar)

print(f"\n📊 PARÁMETROS DE MUESTREO:")
print(f"   Frecuencia de muestreo: {Fs} Hz")
print(f"   Duración: {T} segundos")
print(f"   Número de muestras: {N}")
print(f"   Rango de tiempo: [{t[0]:.2f}, {t[-1]:.2f}] segundos")

# ============================================
# 1. GENERACIÓN DE SEÑALES ELEMENTALES
# ============================================
print("\n" + "="*60)
print("1. GENERACIÓN DE SEÑALES ELEMENTALES")
print("="*60)

# 1.1 PULSO RECTANGULAR
duracion_pulso = 0.2  # 200 ms de duración
pulso_rect = np.where(np.abs(t) < duracion_pulso/2, 1.0, 0.0)
print(f"\n   📦 Pulso rectangular:")
print(f"      - Amplitud: 1.0")
print(f"      - Duración: {duracion_pulso*1000:.0f} ms")
print(f"      - Centrado en: t=0")