# Symbolic Regression employing Genetic Programming

## Description
This work concerns the implementation of a Genetic Programming (GP) algorithm for solving the Symbolic Regression problem, which consists in, given a set of inputs, fit a mathematical model that best represents the original function, both in terms of accuracy and simplicity. This approach builds a model by combining building blocks in order to achieve a final solution, measuring its accuracy.

## Problem Modeling
One of the most important steps when building up a Genetic Programming algorithm concerns the problem modeling. Hence, as in GP each individual is a mapping from a set of values to one single output value, the representation here is defined as a binary tree, since it provides a simple way to build and analyse functions by simply walking through the tree. Thus, internal nodes represent mathematical operators while leaf nodes represent terminals (variables and constants). However, it is important to mention that Genetic Programming approaches do not necessarily require a binary tree modeling, we have used such a structure in this work simply because it best fits our needs.

The set of operators supported by the regression module is presented below.

* <b> Binary Operators </b>
  * <b> + </b>: Addition operator;
  * <b> - </b>: Subtraction operator;
  * <b> * </b>: Multiplying operator;
  * <b> / </b>: Division operator.
  
* <b> Unary Operators </b>
  * <b> sen </b>: Sin function;
  * <b> cos </b>: Cos function;
  * <b> log </b>: Logarithmic function;
  * <b> sqrt </b>: Square root function;
  * <b> pow </b>: Exponential function;
  
<!-- For instance, consider the following function: <i> f(x, y) = 0.95x + cos(y) </i>. Its binary tree representation would look like -->

## Implementation

This project was developed using Python 2 and the only exception stands for the experimental analysis as Python 3 was used for plotting purposes. In this section we introduce some relevant project decisions concerning the implementation.

* The set of mathematical operators used are addition, subtraction, multiplication, division, sine, and cosine, since these operators have presented better results compared to an extended set. The reason for this reduction is to favor sufficiency, closure, and parsimony properties of Genetic Programming approaches. However, the code has been entirely modeled in such a way to extend the set of operators if needed.

* Constant terminals are real numbers generated randomically in a range from 0 to 1. Such an interval was chosen due to the fact that they have proved to be enough for the convergency of the solution. Higher constants may lead to withdrawal from the best solution.

* Operators such as sine and cosine use only one operand. Therefore, we always use the left tree node as the argument for trigonometric functions and the right node is left empty.

* We also established a safe criteria for the division operator: in case of division by zero, the output is always set to zero.

* The maximum depth of the tree is set to 7 as default and this value has not been evaluated in the experimental analysis.

* We implemented a penalty measure for individuals that exceed the maximum depth of the tree, a situation derived from crossover and mutation. The penalty is applied to the fitness, boosting it to the maximum integer value that can be represented in Python.

## Project Structure

The code was entirely designed so that future extensions could be possible, hence providing a generic Genetic Programming algorithm for different problems, which would only require individual and fitness calculus changes. The structure adopted is shown below.

* <b> chromossome.py </b>: defines a <i>Chromossome</i> class that represents the tree (i.e the genotype) of an individual. It also provides methods inherent to binary trees such as tree traversal, search and replacement of a node, random subtrees generation, etc.

* <b> individual.py </b>: defines an <i>Individual</i> class that represents an individual of a population, which is composed by its genotype (<i>Chromossome</i>) and the associated fitness. It also provides methods for the calculation of the fitness of a given problem instance and for applying apply mutation to its genotype.

* <b> population.py </b>: defines a <i>Population</i> class that represents a population of individuals. It provides methods for addition and search among the set of individuals and also methods to generate the initial population, which has also been modularized in order to allow the inclusion of different approaches of population generation, even though <i>Ramped Half-and-Half</i> is the standard choice in this project. Furthermore, this class also provides methods to calculate the fitness of the entire population, which uses those methods defined in the <i>Individual</i> class.

* <b> statistics.py </b>: defines a <i>Statistics</i> class that provides a simple and easy way to store and calculate statistics of each algorithm generation.

* <b> utils.py </b>: defines an <i>Utils</i> class that provides a variety of common functions used in all other modules, such as checking whether a terminal is a constant, random probability generation, random integer value generation, random real value generation, etc.

* <b> ioutils.py </b>: defines an <i>IOUtils</i> class that provides a simple interface to file manipulation.

* <b> genprog.py </b>: defines a <i>Genetic Programming</i> class that represents the Genetic Programming itself. It coordinates the algorithm flow: generation of an initial population and the evolution of generations through selection and application of genetic operators. Besides methods regarding the training phase, this module also provides a method to perform the testing phase, which evaluates an instance of the problem using the mathematical model built in the learning process.

* <b> syregression.py </b>: is the main program. This is the module that is executed by the user, which is responsible for parsing the parameters and performing modules calls in order to start the training and testing phases through the utilization of a <i>Genetic Programming</i> instance.

## Results

For information on the results please check the ![documentation](doc/doc.pdf) in which we present graphics and the set of experiments run in order to validate the algorithm.

## Execution & Parameters

In the project root directory, use the following command for running the software:

```bash
$ cd src
$ python syregression [−h] −−train TRAIN −−test TEST −−out OUT
                      [−−pop−size POP SIZE] [−−cross −prob CROSS PROB]
                      [−−mut−prob MUT PROB] [−−max−depth MAX DEPTH]
                      [−−seed SEED] [−−nvariables NVARIABLES] [−−ngen NGEN]
                      [−−tour−size TOUR SIZE] [−−elitism ELITISM]
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

## Input & Output

The input files are given in CSV (Comma-Separated Values) format and their contents are all floating-point values. Hence, let <i> n </i> be the number of entries in a row of the input file. The first <i> n - 1 </i> values correspond to the input variables of a function, that is <i> x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n - 1</sub> </i>, while the last entry refers to the <i> y </i> output of the function when variables <i> x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n - 1</sub> </i> are applied to it, that is <i> f(<i> x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n - 1</sub></i>)</i>.

The output consists of two files: <i>out.txt</i> and <i>out.txt.csv</i>, where <i>out</i> is the output filed defined by <i> --out </i> parameter. The first one stores a log in human-readable format with pertinent information regarding all Genetic Programming generations. The second one produces a CSV file with the same information, which is the input to the scripts used to perform the experimental analysis. We show below an output example.
