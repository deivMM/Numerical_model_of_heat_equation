# Numerical_model_of_heat_equation
Numerical model of the heat equation

Temperature $ \to T = f(x,t)[ºC]$

Time $\to t[s]$

Thermal diffusivity $\to \alpha[\frac{m^2}{s}]$


$$\LARGE\nabla^{2}T+\frac{q}{k}=\frac{1}{\alpha}\frac{\partial T}{\partial t}$$

$$\frac{\partial^2 T}{\partial x^2}+\frac{\partial^2 T}{\partial y^2}+\frac{\partial^2 T}{\partial z^2}+\frac{q}{k}=\frac{1}{\alpha}\frac{\partial T}{\partial t}$$

$$\frac{\partial^2 T}{\partial x^2}+\frac{q}{k}=\frac{1}{\alpha}\frac{\partial T}{\partial t}$$


$$\frac{k}{c_p\rho}\underset{difcentral}{\underbrace{\frac{\partial^2 T}{\partial x^2}}}+\frac{q}{c_p\rho} = \underset{dif.progr.}{\underbrace{\frac{\partial T}{\partial t}}}$$


