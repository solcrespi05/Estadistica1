
# Contenidos para Resolver la Práctica 1

## 1. Modelos No Paramétricos

### a) Estadísticos Descriptivos:
- **Media Muestral (\(ar{x}\))**: Es una medida de tendencia central que estima la media poblacional y se calcula como:
x̄ = (1/n) * Σ x_i


  
- **Mediana**: Es el valor que divide los datos en dos partes iguales. Es más robusta frente a valores atípicos.

- **Proporciones**: La proporción se calcula dividiendo el número de observaciones que cumplen cierta condición entre el número total de observaciones:
  \[
  	ext{Proporción} = rac{	ext{Número de observaciones que cumplen la condición}}{n}
  \]

### b) Función de Distribución Acumulada (CDF) e Intervalos de Confianza:
- **Función de Distribución Acumulada (CDF, \(F(x)\))**: Es la probabilidad acumulada de que una variable aleatoria \(X\) tome un valor menor o igual a \(x\):
  \[
  F(x) = P(X \leq x)
  \]
  
- **Intervalos de Confianza**: Para una media con varianza conocida, un intervalo de confianza del 95% para la media es:
  \[
  ar{x} \pm z_{lpha/2} \cdot rac{\sigma}{\sqrt{n}}
  \]
  donde \(z_{lpha/2}\) es el valor crítico de la distribución normal.

### c) Distribuciones:
- **Distribución Normal \(N(0, 1)\)**: Es una distribución simétrica y muy utilizada en estadística. Su función de densidad es:
  \[
  f(x) = rac{1}{\sqrt{2\pi}} e^{-rac{x^2}{2}}
  \]
  
- **Distribución Exponencial**: Se utiliza para modelar el tiempo entre eventos. Su función de densidad es:
  \[
  f(x) = \lambda e^{-\lambda x}, \quad x \geq 0
  \]

## 2. Modelos Paramétricos

### a) Estimadores de Momentos y de Máxima Verosimilitud:
- **Estimadores de Momentos**: Se obtienen igualando los momentos muestrales con los momentos teóricos de una distribución.

- **Estimadores de Máxima Verosimilitud (MLE)**: Se calculan maximizando la función de verosimilitud. Ejemplo para la distribución normal \(N(\mu, \sigma^2)\):
  \[
  L(\mu, \sigma^2) = \prod_{i=1}^{n} rac{1}{\sqrt{2\pi \sigma^2}} \exp\left( -rac{(x_i - \mu)^2}{2\sigma^2} 
ight)
  \]
  El MLE se obtiene resolviendo las ecuaciones derivadas de esta función.

### b) Estimadores Insesgados y Asintóticamente Insesgados:
- **Estimador Insesgado**: Es un estimador cuyo valor esperado es igual al parámetro que estima, es decir, \(E(\hat{	heta}) = 	heta\).
  
- **Estimador Asintóticamente Insesgado**: Es un estimador que se vuelve insesgado a medida que el tamaño de la muestra aumenta.

### c) Error Cuadrático Medio (ECM):
El **Error Cuadrático Medio (ECM)** de un estimador combina su varianza y el cuadrado de su sesgo:
\[
ECM(\hat{	heta}) = 	ext{Var}(\hat{	heta}) + 	ext{Sesgo}(\hat{	heta})^2
\]
El ECM se usa para comparar la precisión de diferentes estimadores.

## 3. Test de Hipótesis e Intervalos de Confianza

### a) Test de Hipótesis:
- **Hipótesis Nula \(H_0\)**: Es la afirmación que se intenta refutar con los datos.
  
- **Hipótesis Alternativa \(H_A\)**: Es la afirmación que se acepta si los datos proporcionan suficiente evidencia para rechazar \(H_0\).

### b) Región de Rechazo y Valor Crítico:
- **Región de Rechazo**: Es el conjunto de valores de la estadística de prueba que llevan al rechazo de la hipótesis nula.
  
- **Valor Crítico**: Es el valor que separa la región de rechazo del resto de la distribución. Para un nivel de significancia \(lpha\), el valor crítico \(z_{lpha/2}\) se obtiene de las tablas de la distribución normal o \(t\)-Student, dependiendo de si se conoce la varianza.

## 4. Errores de Medición y Estimación de Parámetros

- **Errores de Medición**: Los errores de medición se modelan como \(X = \mu + \epsilon\), donde \(\epsilon\) es un error aleatorio con media cero y varianza conocida. La media muestral sigue siendo un buen estimador de \(\mu\).

- **Varianza del Estimador de la Media**: La varianza de la media muestral se reduce a medida que aumenta el tamaño de la muestra:
  \[
  	ext{Var}(ar{X}) = rac{\sigma^2}{n}
  \]

---

Este README contiene los conceptos clave para resolver la práctica, incluyendo la estimación de parámetros, pruebas de hipótesis, y el uso de distribuciones estadísticas.
