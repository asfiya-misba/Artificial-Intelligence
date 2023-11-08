# Bayesian Network Learning and Inference

This project is a Python-based implementation of learning conditional probability tables (CPTs) for a Bayesian Network from training data and performing probabilistic inference. The Bayesian Network consists of four variables:

- B: True if there is a Baseball Game on TV, False if not.
- G: True if George watches TV, False if not.
- C: True if George is out of Cat Food, False if not.
- F: True if George feeds his cat, False if not.

## Task 1 - Learning CPTs

### Usage

To learn the conditional probability tables (CPTs) from training data, use the following command line invocation:

```
bnet.py <training_data>
```

- `<training_data>` is a text file with training data, formatted as described in the prompt.

The program will calculate and display the conditional probability values in standard output.

## Task 2 - Calculate Joint Probability Distribution (JPD)

### Usage

To calculate a specific value in the Joint Probability Distribution (JPD) for this domain using the conditional probability distributions calculated in Task 1, use the following command line invocation:

```
bnet.py <training_data> <Bt/Bf> <Gt/Gf> <Ct/Cf> <Ft/Ff>
```

- `<training_data>` is a text file with training data.
- `<Bt>` if B is true, `<Bf>` if B is false.
- `<Gt>` if G is true, `<Gf>` if G is false.
- `<Ct>` if C is true, `<Cf>` if C is false.
- `<Ft>` if F is true, `<Ff>` if F is false.

Sample Invocation: 
```
bnet.py training_data.txt Bt Gf Ct Ff
```

The program will calculate and display the calculated probability values in standard output.

## Task 3 - Probabilistic Inference by Enumeration

### Usage (Optional Extra Credit)

To calculate the probability for any event given evidence (if available) using inference by enumeration, use the following command line invocation:

```
bnet.py <training_data> <query variable values> [given <evidence variable values>]
```

- `<training_data>` is a text file with training data.
- Values of Query Variable (format is the same as in Task 2).
- Values of Evidence Variable (if any, format is the same as in Task 2).

Sample Invocations:
```
bnet.py training_data.txt Bt Gf given Ff
bnet.py training_data.txt Bt Ff
```

The program will calculate and display the calculated probability values in standard output.

This implementation allows you to learn from data, calculate probabilities for specific events, and perform probabilistic inference for various queries.
