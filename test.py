import numpy as np

truths = np.array([1, 1, 0, 0])
preds = np.array([0.95, 0.55, 0.01, 0.45])

loss = np.zeros(4)

for i in range(4):
    if truths[1] == 1:
        loss[i] = truths[i] * -1 * np.log(preds[i])
    else:
        loss[i] = truths[i] * -1 * np.log(1-preds[i])

alpha = 0.25
gama = 2.0
weights = np.zeros(4)

for i in range(4):
    if truths[i] == 1:
        weights[i] = alpha * (1 - preds[i]) ** gama
    else:
        weights[i] = (1 - alpha) * (1 - preds[i]) ** gama



print(weights)

