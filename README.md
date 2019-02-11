# Symbolic Regression through Genetic Programming

## Description
This work concerns the implementation of a Genetic Programming (GP) algorithm for solving the Symbolic Regression problem, which consists in, given a set of inputs, fit a mathematical model that best represents the original function, both in terms of accuracy and simplicity. This approach builds a model by combining building blocks in order to achieve a final solution, measuring its accuracy.

## Problem Modeling
One of the most important steps when building up a Genetic Programming algorithm concerns the problem modeling. Hence, as in GP each individual is a mapping from a set of values to one single output value, the representation here is defined as a binary tree, since it provides a simple way to build and analyse functions by simply walking through the tree. Thus, internal nodes represent mathematical operators while leaf nodes represent terminals (variables and constants). However, it is important to mention that Genetic Programming approaches do not necessarily require a binary tree modeling, we have used such a structure in this work simply because it best fits our needs.

The set of operators supported by the regression module is presented below.

* Binary Operators
  * <b> + </b>: Addition operator;
  * <b> - </b>: Subtraction operator;
  * <b> * </b>: Multiplying operator;
  * <b> / </b>: Division operator.
  
* Unary Operators
  * <b> sen </b>: Sin function;
  * <b> cos </b>: Cos function;
  * <b> log </b>: Logarithmic function;
  * <b> sqrt </b>: Square root function;
  * <b> pow </b>: Exponential function;
  
<!-- For instance, consider the following function: <i> f(x, y) = 0.95x + cos(y) </i>. Its binary tree representation would look like -->

## Implementation



## Results

## Execution

## Parameters
