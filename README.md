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

In the project root directory, use the following command for running the software:

```bash
$ cd src
$ python syregression [−h ] −−train TRAIN −−test TEST −−out OUT
                      [−−pop−size POP SIZE ] [−−cross −prob CROSS PROB ]
                      [−−mut−prob MUT PROB] [−−max−depth MAX DEPTH]
                      [−−seed SEED ] [−−nvariables NVARIABLES ] [−−ngen NGEN]
                      [−−tour−size TOUR SIZE ] [−−elitism ELITISM ]
```

The parameters listed above are:

* <i><b>--h, --help</b></i>: Show help menu.
* <i><b>--train</b></i>: Training file path <b>(Required)</b>
* <i><b>--test</b></i>: Test file path <b>(Required)</b>
* <i><b>--out</b></i>: Output file path <b>(Required)</b>
* <i><b>--pop-size</b></i>: Population size <b>(Default: 30)</b>
* <i><b>--cross-prob</b></i>: Probability of crossing-over <b>(Default: 0.90)</b>
* <i><b>--mut-prob</b></i>: Probability of mutation <b>(Default: 0.05)</b>
* <i><b>--max-depth</b></i>: Maximum tree depth <b>(Default: 7)</b>
* <i><b>--seed</b></i>: Seed for random numbers generation <b>(Default: 1)</b>
* <i><b>--nvariables</b></i>: Number of variables used to build up the mathematical function <b>(Default: 2)</b>
* <i><b>--ngen</b></i>: Number of generations <b>(Default: 30)</b>
* <i><b>--tour-size</b></i>: K size defined for tournament selection <b>(Default: 2)</b>
* <i><b>--elitism</b></i>: Enable the utilization of elitism operators <b>(Default: True)</b>
