# Ejercicio 1 
Determine cuáles de las siguientes distribuciones son EDMs identificando (en donde sea posible), el parámetro natural 𝜃, la función cumulante 𝜅(𝜃), el parámetro de dispersión 𝜙 y la función de normalización 𝑎(𝑦, 𝜙):
### (a)Normal:  
$$
    f(y,\mu ,\sigma ^{2}) = \frac{1}{\sqrt{2\pi \sigma ^{2}}}e^{-\frac{(y- \mu)^{2}}{2\sigma ^{2}}}$$  
### (b) Poisson
$$f(y;\mu )=  \frac{e^{-\mu}\mu^{y}}{y!}$$  

### (c) Binomial. Considere 𝑦 𝜖 [0, 1] como la proporción de éxitos en 𝑛 experimentos de Bernoulli con probabilidad de éxito 𝜇\n.
$$f(y;\mu,n)=\binom{m}{my}\mu^{ny}(1-\mu)^{n-ny}$$  

### (d)Weibull
$$f(y;\alpha, \gamma) = \frac{\alpha}{\gamma}(\frac{y}{\gamma})^{\alpha-1} e^{-(\frac{y}{\gamma})^{\alpha}}$$  

###    (e) Weibull con 𝛼 = 1 y 𝛾 = 1/𝜆 (¿qué distribución es esta?)
### (f ) Geométrica

$$𝑓 (𝑦; 𝑝) = 𝑝(1 − 𝑝)^{𝑦−1}$$  

###    (g) Beta  
$$𝑝(𝑦; 𝛼, 𝛽) = B[𝛼, 𝛽]𝑦^{𝛼−1}(1 − 𝑦)^{𝛽−1}$$  

###    (h) Gamma  
$$
    f(y;\alpha, \lambda) = \frac{1}{\Gamma (\alpha)}e^{-\lambda y}\lambda^{\alpha}y^{\alpha-1}$$  

(ayuda: realice el cambio de variable 𝜆 = 𝛼/𝜇 y haga los cálculos para la PDF 𝑓 (𝑦; 𝛼, 𝜇) )  

### (i) Gaussiana inversa  

$$f(y;\mu, \phi )=  \frac{1}{\sqrt{2\pi y^{3}\phi}}e ^{-\frac{(y-\mu)^{2}}{2\phi y \mu^{2}}} $$  
## Resolución :  
i. Tratamos de llevarla a forma canonica para entenderla mejor
$$f(y;\mu,\sigma^{2}) =  \frac{1}{\sqrt{2\pi \sigma ^{2}}} exp \left[\frac{y\mu - (\mu^{2}/2)}{\sigma^{2}}- \frac{y^{2}}{2\sigma^{2}} \right] 
$$  

ya con esto vemos que el parámetro $\theta$ = $\mu$ porque es el queda multiplicando a la $y$ y la función cumulante ($\kappa(\theta)= \mu$) sería: $(\mu^{2}/2)exp \left{- \frac{y^{2}}{2\sigma^{2}} \right}$. El parametro de disperción seria $\sigma^{2}$
(sacado del libro de Dunn)  

ii.
Poisson escrita de la forma de EDM:  
$$P(y; \mu) = \exp \left\{y \log(\mu) - \mu - \log(y!) \right\}$$


mostrando que el parametro canonico $\theta$ es $log(\mu)$
,$\kappa(\theta) = \mu$, y $\phi =1$. La funcion normalizadora es $a(y,\phi) =1/y!$  
iii. Binomial de la forma EDM  
$$
\binom{m}{my}exp\left [ m\left\{ y log\frac{\mu}{1-\mu} + log(1-\mu)\right\} \right ]$$  

donde el parámetro canonico es $\theta = log\left\{\mu/( 1-\mu)\right\} $. Entonces $\kappa(\theta) = -log (1-\mu)$, y $\phi = 1/n$. Por último $\binom{m}{my}$ es la función normlizadora. La dsitribución binomial es un EDM cuando se conoce n 

iv , v. Weibull -> esta distribución no siempre es EDM, solo cuando $\alpha = 1$ que en realidad queda como la distribución exponencial con media $\gamma$. 
Entonces en a forma EDM nos queda:
$$P(y, \gamma) = exp \left\{−(y/γ) − log γ\right\}
$$  
Con lo que nos deja de parametro canonico a $-1/\gamma$ , $\kappa(\theta) = log\gamma$ y $\phi = 1$  

las otras distribuciones las hare más adelante cuando tenga tiempo y ganas :)