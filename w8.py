import numpy as np

# Inputs
i1, i2 = 0.05, 0.10
t1, t2 = 0.01, 0.99
b1 = 0.35
b2 = 0.60
η = 0.1

# ----------------------------
# Input → Hidden (9 weights)
# ----------------------------
w1, w2, w3 = 0.15, 0.20, 0.25    # to h1
w4, w5, w6 = 0.30, 0.24, 0.22    # to h2
w7, w8, w9 = 0.40, 0.45, 0.54    # to h3

# ----------------------------
# Hidden → Output (6 weights in picture but total 12 are given)
# but you want only 12 TOTAL weight so we use ONLY these 3+3
# ----------------------------
w10, w11, w12 = 0.40, 0.45, 0.54   # h1,h2,h3 → o1
w13, w14, w15 = 0.50, 0.55, 0.60   # h1,h2,h3 → o2


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# ---------- Forward pass ----------


# Hidden layer
neth1 = i1*w1 + i2*w2 + b1*w3
outh1 = sigmoid(neth1)

neth2 = i1*w4 + i2*w5 + b1*w6
outh2 = sigmoid(neth2)

neth3 = i1*w7 + i2*w8 + b1*w9
outh3 = sigmoid(neth3)

# Output neurons
neto1 = outh1*w10 + outh2*w11 + outh3*w12 + b2
outo1 = sigmoid(neto1)

neto2 = outh1*w13 + outh2*w14 + outh3*w15 + b2
outo2 = sigmoid(neto2)

# Error
E_total = 0.5*(t1-outo1)**2 + 0.5*(t2-outo2)**2
print("Total Error:", E_total)

# ---------- Backward pass ----------
delta_o1 = -(t1-outo1) * outo1*(1-outo1)
delta_o2 = -(t2-outo2) * outo2*(1-outo2)

# Update hidden→output weights
w10 -= η * delta_o1 * outh1
w11 -= η * delta_o1 * outh2
w12 -= η * delta_o1 * outh3

w13 -= η * delta_o2 * outh1
w14 -= η * delta_o2 * outh2
w15 -= η * delta_o2 * outh3

# Hidden deltas
delta_h1 = (delta_o1*w10 + delta_o2*w13) * outh1*(1-outh1)
delta_h2 = (delta_o1*w11 + delta_o2*w14) * outh2*(1-outh2)
delta_h3 = (delta_o1*w12 + delta_o2*w15) * outh3*(1-outh3)

# Update input→hidden
w1 -= η * delta_h1 * i1
w2 -= η * delta_h1 * i2
w3 -= η * delta_h1 * b1

w4 -= η * delta_h2 * i1
w5 -= η * delta_h2 * i2
w6 -= η * delta_h2 * b1

w7 -= η * delta_h3 * i1
w8 -= η * delta_h3 * i2
w9 -= η * delta_h3 * b1

# ---------- Print updated weights clearly ----------
print("\nUpdated Weights:")
print(f"w1={w1:.5f},  w2={w2:.5f},  w3={w3:.5f}")
print(f"w4={w4:.5f},  w5={w5:.5f},  w6={w6:.5f}")
print(f"w7={w7:.5f},  w8={w8:.5f},  w9={w9:.5f}")

print(f"w10={w10:.5f}, w11={w11:.5f}, w12={w12:.5f}")
print(f"w13={w13:.5f}, w14={w14:.5f}, w15={w15:.5f}")
