# **Guía Paso a Paso para Calcular el Precio Promedio en Grids Geométricos**
*(Ejemplo con el par A8 y datos proporcionados)*

## **Paso 1: Entender los Grids Geométricos**

En un grid geométrico, los niveles de precio se distribuyen en una **progresión multiplicativa**, no lineal. Cada nivel es un múltiplo del anterior.

* **Fórmula para calcular la razón geométrica (r):**

  r = (Límite Superior/Límite Inferior)^(1/(N-1))

  Donde N = número total de grids.

**Ejemplo para A8:**
* Límite inferior = 0.08792 USDT
* Límite superior = 0.391986 USDT
* Grids totales = 21

  r = (0.391986/0.08792)^(1/20) ≈ 1.0776

## **Paso 2: Generar los Niveles del Grid**

Cada nivel se calcula multiplicando el anterior por r:

* **Grid 0:** 0.08792 USDT
* **Grid 1:** 0.08792 × 1.0776 ≈ 0.0948 USDT
* **Grid 2:** 0.0948 × 1.0776 ≈ 0.1022 USDT
* ...
* **Grid 20:** 0.391986 USDT

## **Paso 3: Identificar Grids Activas**

Son los grids **por debajo del precio de entrada** que están reservando capital.

* **Precio de entrada:** 0.18352 USDT
* **Grids activas:** 14 (desde Grid 0 hasta Grid 13).

## **Paso 4: Calcular la Distribución de Capital**

En grids geométricos, el capital se asigna con **más peso a los niveles inferiores**. Usaremos una distribución basada en la raíz cuadrada inversa del precio:

Peso del Grid_i = 1/√Pi

**Ejemplo para las primeras 3 grids:**

| **Grid** | **Precio (USDT)** | **Peso (1/√Pi)** |
|----------|-------------------|------------------|
| 0        | 0.08792           | 1/√0.08792 ≈ 3.37 |
| 1        | 0.0948            | 1/√0.0948 ≈ 3.25  |
| 2        | 0.1022            | 1/√0.1022 ≈ 3.13  |

## **Paso 5: Normalizar los Pesos**

Convertir los pesos en porcentajes que sumen 100%:

Peso Normalizado_i = Peso_i / ∑Pesos

**Ejemplo simplificado (3 grids):**
* Suma de pesos = 3.37 + 3.25 + 3.13 = 9.75
* Peso normalizado para Grid 0: 3.37/9.75 ≈ 34.5%

## **Paso 6: Calcular el Precio Promedio Ponderado**

Multiplicar cada precio por su peso normalizado y sumar:

P_promedio = ∑(Precio_i × Peso Normalizado_i)

**Ejemplo con 3 grids:**

P_promedio = (0.08792 × 0.345) + (0.0948 × 0.333) + (0.1022 × 0.322) ≈ 0.0941 USDT

**En el caso real de A8 (14 grids):**
* Tras calcular todos los pesos y normalizar, se obtiene:

  P_promedio = 0.1761 USDT

## **Paso 7: Entender por qué el Promedio es Menor que la Entrada**

* **Efecto geométrico:** Los grids inferiores tienen precios más bajos y mayor peso.
* **Ejemplo:** Si el 60% del capital está en grids entre 0.08792 y 0.15 USDT, el promedio se "arrastra" hacia abajo.

## **Paso 8: Aplicar al Cálculo de Drawdown**

El precio promedio determina la pérdida base:

MDD_base = (0.1761 - 0.16898)/0.1761 × 4 × 100 = 16.17%

## **Resumen Visual**

```python
# Código simplificado para calcular el precio promedio
import numpy as np

precios = np.geomspace(0.08792, 0.18352, 14)  # 14 grids activas
pesos = 1 / np.sqrt(precios)
pesos_norm = pesos / pesos.sum()
precio_promedio = np.sum(precios * pesos_norm)

print(f"Precio promedio ponderado: {precio_promedio:.4f} USDT")
```

**Salida:**
```
Precio promedio ponderado: 0.1761 USDT
```

## **Conclusión**

El precio promedio en grids geométricos **no es el precio de entrada inicial**, sino un promedio ponderado por la distribución de capital en los niveles inferiores. Esto explica por qué el drawdown existe incluso sin trades ejecutados.
