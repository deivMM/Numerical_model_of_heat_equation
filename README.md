# Numerical model of heat equation
Numerical model of the heat equation

Temperature $ \LARGE\to T = f(x,t)[ºC]$

Time $\LARGE\to t[s]$

Thermal diffusivity $\LARGE\to \alpha=\frac{k}{\rho c_p}[\frac{m^2}{s}]$


$$\LARGE\nabla^{2}T+\frac{q}{k}=\frac{1}{\alpha}\frac{\partial T}{\partial t}$$

$$\frac{\partial^2 T}{\partial x^2}+\frac{\partial^2 T}{\partial y^2}+\frac{\partial^2 T}{\partial z^2}+\frac{q}{k}=\frac{1}{\alpha}\frac{\partial T}{\partial t}$$

$$\frac{\partial^2 T}{\partial x^2}+\frac{q}{k}=\frac{1}{\alpha}\frac{\partial T}{\partial t}$$


$$\frac{k}{c_p\rho}\underset{difcentral}{\underbrace{\frac{\partial^2 T}{\partial x^2}}}+\frac{q}{c_p\rho} = \underset{dif.progr.}{\underbrace{\frac{\partial T}{\partial t}}}$$


