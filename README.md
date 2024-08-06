# MAB-Module 

## Function name <br>
**mab_function()** <br>

## Function Code
Copy everything from the file including functions *flatten(lst)* and *unflatten(flat_list, structure)* <br>
**MAB_function.py** <br>

## Function Usage
Has been shown in: <br>
**MAB_MODULE.ipynb**

## Function Parameters
Requires 4 function Parameters: <br>
**mab_function(parameter_values, bounds, m_iterations, e_factor)** <br>
where, <br>
*parameter_values* = A list of all the **parameter values to be optimized** [List, length - Number of parameters] <br>
*bounds* = A list of limit boundaries (range) of the parameter values [List, length - Number of parameters] <br>
*m_iterations* = Number of max iterations [Integer] <br>
*e_factor* = Exploration factor [Float] <br>

## Function Necessities
To use the mab function you need to have 1 function: <br>
*1. objective_function(para)* <br>
Takes *para* as function parameter, (expects a list same as *parameter_values*) <br>
Use this function to calculate the sum rate/other value<br>
Return the sum rate/other value [Float] <br>

### Note
Generally with MAB Algorithm, the penalty function differs from problem to problem. You can incorporate the penalty function in the *objective_function(para)* function and return (sum rate + penalty value). <br>
> **Return: Rₛᵤₘ + Total penalty** <br>
