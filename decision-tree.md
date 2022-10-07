# Decision Tree

## Measuring Purity

- Entropy as a measure of impurity
- example: $p = 3/6, H(p) = 1$; $p = 2/6, H(p) = 0.92$; $p = 5/6, H(p) = 0.65$
- The higher the $H$, the less pure the sample.
- $H(p) = -p_1 \log (p_1) - p_0 \log (p_0)$, $p_0 = 1-p_1$
- another measure of impurity is Gini impurity

## Choosing a split: Information gain

- weighted average of entropies
- reduction in entropy = information gain
- Information gain = $H(p_1^{root}) - (w^{left}H(p_1^{left}) + w^{right}H(p_1^{right}))$

## Putting it together

1. Start from root node
2. Calculate information gain for all possible features, pick the one with the highest information gain
3. Split the dataset according to selected feature, and create left and right branches of the tree
4. Keep repeating splitting process until stopping criteria is met:

> - When a node is 100% one class
> - When splitting a node will result in the tree exceeding a max depth
> - Information gain from additional splits is less than threshold
> - When number of examples in a node is below a threshold

## Recursive splitting

- writing a code that calls itself

## Using one-hot encoding of categorical features

- Create $k$ binary features for a categorical feature that takes on $k$ values

## Continuous features

- Consider different values to split on
- Split on the value that gives the greatest information gain

## Regression Trees

- mean values of leaf node as the prediction of test sample
- Key decision: choosing a split
- How to choose a split: weighted average of variances that is the lowest
- Similar idea to 'information gain', calculate the reduction in variance
- Choose the feature that gives the highest reduction in variance

## Tree ensembles

- Trees are **highly sensitive** to small changes of the data -> not robust

## Sampling with replacement

- sample is the same size as the training set

## Random Forest

- Generating a tree sample

> for $b$ = 1 to $B$:
>>
>> - Use sampling with replacement to create a new training set of size $m$
>> - Train a decision tree on the new dataset

- this is called **bagged decision tree**
- this has a problem, most of the root nodes will split at the same features, so we randomise the feature choice
- Randomising the feature choice: at each node, when choosing a feature to use to split, if $n$ features are available, pick a random subset of $k < n$ features and allow the algorithm to only choose from that subset of features
- usually $k = \sqrt{n}$
- this is called **random forest algorithm**

## XGBoost

- a type of tree ensemble
- Boosted trees intuition

> for $b$ = 1 to $B$:
>>
>> - Use sampling with replacement to create a new training set of size $m$.
>> - *But instead of picking from all examples with equal (1/m) probability, make it more likely to pick misclassified examples from previously trained trees*.
>> - Train a decision tree on the new dataset

- Good choice of default splitting criteria and criteria for when to stop splitting
- Built in regularisation to prevent overfitting

## When to use decision tree

- Works well on tabular (structured) data
- Not recommended for unstructured data (images, audio, text)
- Fast
- Small decision trees may be human interpretable

## When to use Neural Network

- Works well on all types of data, including tabular (structured) and unstructured data
- May be slower than a decision tree
- Works with transfer learning (pre-training)
- When building a system of multiple models working together, it might be easier to string together multiple neural networks
