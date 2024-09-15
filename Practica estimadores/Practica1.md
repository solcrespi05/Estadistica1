# Practica1 detallada

## 1. **Estimadores: Cómo calcular estimadores de la media y la varianza, y qué significa que un estimador sea insesgado**

### a) **Estimadores**

Un **estimador** es una función basada en los datos muestrales que nos permite hacer inferencias sobre un parámetro poblacional desconocido. Si $X_1, X_2, \dots, X_n$  son observaciones de una muestra aleatoria, podemos usar estos datos para construir estimadores de parámetros como la media, varianza, etc.

### b) **Estimador de la Media**

El **estimador de la media poblacional**  $\mu$ , basado en una muestra  $X_1, X_2, \dots, X_n$ , es la **media muestral** $\bar{X}$ :

$$
\hat{\mu} = \bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i
$$

Este estimador tiene la propiedad de ser **insesgado**, lo que significa que, en promedio, su valor coincide con el valor verdadero del parámetro poblacional. Formalmente, si  $E(\bar{X}) = \mu$ , entonces  $\bar{X}$  es insesgado.

### c) **Estimador de la Varianza**

### d) **Estimador Insesgado**

Para estimar la varianza poblacional $\sigma^2$ , el **estimador insesgado de la varianza** es:

$$
\hat{\sigma}^2 = S^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar{X})^2
$$

¿Por qué dividimos entre  $n-1$  en lugar de $n$ ? Porque usar $n$  introduce un sesgo hacia abajo en la estimación, es decir, el estimador tendería a subestimar la varianza verdadera. Dividir entre $n-1$  corrige este sesgo, haciendo que el estimador sea insesgado.

Un **estimador insesgado** es aquel cuyo valor esperado es igual al parámetro poblacional que intenta estimar. Formalmente, si  $\hat{\theta}$  es un estimador de $\theta$ , entonces $\hat{\theta}$  es insesgado si:

$$
E(\hat{\theta}) = \theta
$$

Por ejemplo,  $E(\bar{X}) = \mu$  y $E(S^2) = \sigma^2$ , lo que indica que tanto la media muestral como la varianza muestral son estimadores insesgados.

## 2. **Error Cuadrático Medio (ECM)**

El **Error Cuadrático Medio (ECM)** de un estimador mide la calidad del estimador, ya que toma en cuenta tanto la **varianza** del estimador como su **sesgo**.

### a) **Definición**

El ECM de un estimador $\hat{\theta}$  de un parámetro $\theta$  se define como:

$$
ECM(\hat{\theta}) = E[(\hat{\theta} - \theta)^2]
$$

Este valor se puede descomponer en dos partes:

$$
ECM(\hat{\theta}) = \text{Var}(\hat{\theta}) + (\text{sesgo}(\hat{\theta}, \theta))^2
$$

Donde:

 $\text{Var}(\hat{\theta})$  es la **varianza** del estimador.

$\text{sesgo}(\hat{\theta}, \theta) = E[\hat{\theta}] - \theta$  → es la diferencia entre el valor esperado del estimador y el valor verdadero del parámetro.

### b) **Interpretación**

- Si el estimador es **insesgado**, el sesgo es cero, y el ECM se reduce a la varianza del estimador:  $ECM(\hat{\theta}) = \text{Var}(\hat{\theta})$ .
- Si el estimador tiene sesgo, el ECM considera tanto el error introducido por el sesgo como la variabilidad del estimador.

### c) **Ejemplo**

Supongamos que tienes dos estimadores de la media, $\hat{\theta}_1$  y  $\hat{\theta}_2$ . Aunque uno podría tener menor varianza, si tiene un gran sesgo, su ECM podría ser mayor que el del otro estimador con menor sesgo pero mayor varianza. Esto muestra que el ECM combina ambas fuentes de error.

## 3. **Función de Verosimilitud y Máxima Verosimilitud (MLE)**

### a) **Función de Verosimilitud**

La **función de verosimilitud** expresa la probabilidad de los datos observados en función de los parámetros del modelo. Dada una muestra  $X_1, X_2, \dots, X_n$  y un modelo con un parámetro desconocido $\theta$ , la función de verosimilitud se define como:

$$
L(\theta) = f(X_1|\theta) \times f(X_2|\theta) \times \dots \times f(X_n|\theta)
$$

Donde  $f(X_i|\theta)$  es la función de densidad o de probabilidad de la observación  $X_i$ , dado  $\theta$ .

### b) **Estimación por Máxima Verosimilitud (MLE)**

El estimador de **Máxima Verosimilitud (MLE)** es el valor del parámetro $\theta$  que maximiza la función de verosimilitud:

$$
\hat{\theta}{MLE} = \arg \max{\theta} L(\theta)
$$

Es decir, es el valor de  $\theta$  que hace más probable observar los datos que tenemos.

### c) **Importancia del MLE**

El MLE tiene varias propiedades deseables, especialmente cuando el tamaño de la muestra es grande:

- **Consistencia**: El MLE converge al valor verdadero del parámetro a medida que el tamaño de la muestra aumenta.
- **Eficiencia**: El MLE tiene la varianza más baja posible entre todos los estimadores insesgados.
- **Normalidad Asintótica**: Para muestras grandes, el MLE es aproximadamente normalmente distribuido.

### d) **Ejemplo: Distribución Normal**

Si tenemos una muestra  $X_1, X_2, \dots, X_n$  que sigue una distribución normal  $N(\mu, \sigma^2)$ , el MLE para  $\mu$  es simplemente la media muestral $\hat{\mu} = \bar{X}$ .

## 4. **Intervalos de Confianza**

### a) **Definición**

Un **intervalo de confianza** es un rango de valores calculado a partir de los datos muestrales que contiene el valor verdadero del parámetro poblacional con una cierta probabilidad (el nivel de confianza). Por ejemplo, un intervalo de confianza del 95% para la media $\mu$  significa que, en el 95% de las muestras, el intervalo contiene el valor verdadero de  $\mu$.

### b) **Cálculo del Intervalo de Confianza para la Media**

Si los datos vienen de una distribución normal con varianza  $\sigma^2$  conocida, el intervalo de confianza para la media  $\mu$  con nivel de confianza $1 - \alpha$  es:

$$
\bar{X} \pm Z_{\alpha/2} \left( \frac{\sigma}{\sqrt{n}} \right)
$$

Donde:

- $\bar{X}$  es la media muestral,
- $Z_{\alpha/2}$  es el cuantil de la distribución normal estándar correspondiente al nivel de confianza deseado (e.g., $Z_{0.025} = 1.96$  para un 95% de confianza),
- $\sigma$   es la desviación estándar de la población (o su estimador),
- $n$  es el tamaño de la muestra.

### c) **Interpretación**

Un intervalo de confianza no nos da la probabilidad de que un parámetro caiga en ese intervalo en una sola muestra. En cambio, si repetimos el experimento muchas veces y calculamos un intervalo de confianza para cada muestra, aproximadamente el 95% de estos intervalos contendrán el valor verdadero del parámetro.

## 5. **Pruebas de Hipótesis**

### a) **Definición**

Una **prueba de hipótesis** es un procedimiento estadístico para tomar decisiones sobre un parámetro poblacional. Comienza con la formulación de dos hipótesis:

- **Hipótesis nula** ( $H_0$ ): Es la hipótesis que se somete a prueba y generalmente propone que no hay efecto o diferencia.
- **Hipótesis alternativa** ( $H_A$ ): Es la hipótesis que queremos probar.

### b) **Pasos de una Prueba de Hipótesis**

1. **Formular  $H_0$  y $H_A$** .
Ejemplo:  $H_0: \mu = \mu_0,  H_A: \mu \neq \mu_0$ .
2. **Seleccionar un nivel de significancia  $\alpha$** , que es la probabilidad de rechazar incorrectamente $H_0$  (error tipo I). Comúnmente $\alpha = 0.05$ .

3. **Calcular la estadística de prueba**. Para una prueba sobre la media, si la varianza es conocida, se usa:

$$
Z = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}}
$$

4. **Determinar la región de rechazo** o calcular el **valor p**. Si el valor  $p$  es menor que  $\alpha$ , rechazamos  $H_0$ .

### c) **Región de Rechazo y Valor p**

- **Región de Rechazo**: Es el conjunto de valores para la estadística de prueba que lleva a rechazar  $H_0$ . Por ejemplo, en una prueba bilateral, rechazamos  $H_0$  si  $|Z| > Z_{\alpha/2}$ .
- **Valor p**: Es la probabilidad de observar un valor tan extremo como el obtenido si $H_0$  fuera cierta. Si  $p < \alpha$ , rechazamos  $H_0$ .

### d) **Ejemplo**

Si estamos probando si la media de una población es $\mu_0$  usando una muestra  $X_1, X_2, \dots, X_n$ , calculamos la estadística  $Z$ . Si  $Z$  cae en la región de rechazo (por ejemplo, $|Z| > 1.96$   para un nivel de significancia del 5%), rechazamos la hipótesis nula y aceptamos que  $\mu \neq \mu_0$ .

---