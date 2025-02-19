import streamlit as st
import math

st.title("🔄 Calculadora de Razón Geométrica para Grid Trading")
st.markdown("#### *Herramienta para determinar la razón constante entre niveles de precios en grids geométricos*")

with st.expander("📚 **Instrucciones**", expanded=True):
    st.write("""
    1. **Ingresa los parámetros**:
       - Límite inferior (precio mínimo del rango)
       - Límite superior (precio máximo del rango)
       - Número total de grids (niveles de precio)
    
    2. Haz clic en **Calcular Razón Geométrica**
    
    3. **Resultados**:
       - Razón geométrica (r) con 10 decimales
       - Verificación del cálculo
       - Detalle de primeros y últimos grids
    """)

st.divider()

# Inputs numéricos con formato especial
col1, col2, col3 = st.columns(3)
with col1:
    lower = st.number_input("Límite Inferior (USDT)", 
                          min_value=0.00000001, 
                          value=0.08792,
                          format="%.8f")
with col2:
    upper = st.number_input("Límite Superior (USDT)", 
                          min_value=0.00000001, 
                          value=0.391986,
                          format="%.8f")
with col3:
    grids = st.number_input("Número de Grids", 
                          min_value=2, 
                          value=21,
                          help="Mínimo 2 grids")

st.divider()

if st.button("🚀 Calcular Razón Geométrica", type="primary"):
    if lower >= upper:
        st.error("Error: El límite inferior debe ser menor que el superior")
    elif grids < 2:
        st.error("Error: Debe haber al menos 2 grids")
    else:
        try:
            # Cálculo principal
            n = grids - 1  # Intervalos entre grids
            ratio = (upper / lower) ** (1 / n)
            verification = ratio ** n  # Debería ser igual a upper/lower
            
            # Contenedor de resultados con borde alternativo
            st.markdown('<div style="border: 1px solid #e6e6e6; border-radius: 5px; padding: 10px; margin-bottom: 10px;">', 
                      unsafe_allow_html=True)
            
            st.subheader("📊 Resultados")
            
            # Razón con alta precisión
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric(label="**Razón Geométrica (r)**", 
                        value=f"{ratio:.10f}",
                        help="Multiplicador constante entre cada grid")
            
            with col_b:
                st.metric(label="**Verificación (r^n)**", 
                        value=f"{verification:.10f}",
                        help=f"Debería ser igual a {upper/lower:.10f}")

            # Detalle de grids
            st.markdown("**Primeros 3 Grids:**")
            grid_detail = [
                lower,
                lower * ratio,
                lower * (ratio ** 2)
            ]
            st.write(f"{grid_detail[0]:.10f} → {grid_detail[1]:.10f} → {grid_detail[2]:.10f}")

            st.markdown("**Últimos 3 Grids:**")
            grid_detail_end = [
                upper / (ratio ** 2),
                upper / ratio,
                upper
            ]
            st.write(f"{grid_detail_end[0]:.10f} → {grid_detail_end[1]:.10f} → {grid_detail_end[2]:.10f}")

            # Explicación matemática
            with st.expander("🧮 Explicación del Cálculo"):
                st.latex(f'''
                r = \\left(\\frac{{P_{{max}}}}{{P_{{min}}}}\\right)^{{\\frac{{1}}{{n-1}}}} 
                = \\left(\\frac{{{upper}}}{{{lower}}}\\right)^{{\\frac{{1}}{{{grids-1}}}}} 
                = {ratio:.10f}
                ''')
                st.write(f"Donde: \n- Pmax/Pmin = {upper/lower:.10f}\n- Exponente = 1/{grids-1} ≈ {1/(grids-1):.10f}")
            
            st.markdown('</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error en el cálculo: {str(e)}")

st.markdown("---")
st.caption("🔍 **Nota:** Para mayor precisión, todos los cálculos usan aritmética de punto flotante de 64 bits.")
