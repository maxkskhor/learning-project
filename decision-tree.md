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
