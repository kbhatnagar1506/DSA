"""
📌 PROBLEM STATEMENT: Linear Regression to Predict Restaurant Profit

You're the CEO of a restaurant franchise looking to expand into new cities.
You already have profit data from 20 cities and their populations.

🎯 GOAL:
Build a simple machine learning model using **Linear Regression** to:
- Learn the relationship between a city's population and expected monthly profit.
- Predict profit for a new city given its population.

👨‍💻 WHAT YOU WILL BUILD:
- A machine learning model using **gradient descent** to minimize cost.
- A way to visualize both data and the fitted regression line.
- A predictor that can estimate profits for cities with different population sizes.
"""
# ---------- STEP 0: IMPORT LIBRARIES ----------
# numpy: for math and array operations
# matplotlib: for plotting graphs
import numpy as np
import matplotlib.pyplot as plt

# ---------- STEP 1: LOAD AND RETURN DATA ----------
# This function returns example city population and profit data
def load_data():
    # Population of 20 cities (in units of 10,000 people)
    population = np.array([
        6.1101, 5.5277, 8.5186, 7.0032, 5.8598, 8.3829, 7.4764, 8.5781, 6.4862, 5.0546,
        5.7107, 14.164, 5.734, 8.4084, 5.6407, 5.3794, 6.3654, 5.1301, 6.4296, 7.0708
    ])
    # Monthly profit from each city (in units of $10,000)
    profit = np.array([
        17.592, 9.1302, 13.662, 11.854, 6.8233, 11.886, 4.3483, 12.0, 6.5987, 3.8166,
        3.2522, 15.505, 3.1551, 7.2258, 0.71618, 3.5129, 5.3048, 0.56077, 3.6518, 5.3893
    ])
    return population, profit

# ---------- STEP 2: VISUALIZE THE DATA ----------
def plot_data(x, y):
    # Plot red 'x' markers at each (population, profit) point
    plt.scatter(x, y, c='red', marker='x', label='Training data')
    plt.title("City Population vs. Profit")
    plt.xlabel("City Population (in 10,000s)")
    plt.ylabel("Profit (in $10,000s)")
    plt.legend()
    plt.grid(True)
    plt.show()

# ---------- STEP 3: COST FUNCTION ----------
# Measures how well our model predicts the data
# Lower cost = better fit
def compute_cost(x, y, w, b):
    print(x.shape[0])
    m = x.shape[0]  # Number of training examples
    total_cost = 0

    for i in range(m):
        prediction = w * x[i] + b  # Linear function f(x) = wx + b
        error = prediction - y[i]  # Difference between predicted and actual profit
        total_cost += error ** 2   # Square the error and add it to total

    total_cost = total_cost / (2 * m)  # Divide by 2m for MSE cost
    return total_cost

# ---------- STEP 4: COMPUTE GRADIENT ----------
# Computes how to change w and b to reduce the cost function
def compute_gradient(x, y, w, b):
    m = x.shape[0]  # Number of training examples
    dj_dw = 0       # Partial derivative of cost w.r.t. w
    dj_db = 0       # Partial derivative of cost w.r.t. b

    for i in range(m):
        prediction = w * x[i] + b
        error = prediction - y[i]
        dj_dw += error * x[i]   # ∂J/∂w component
        dj_db += error          # ∂J/∂b component

    dj_dw /= m
    dj_db /= m
    return dj_dw, dj_db

# ---------- STEP 5: GRADIENT DESCENT ----------
# Iteratively updates w and b to minimize cost
def gradient_descent(x, y, w_init, b_init, alpha, iterations):
    w = w_init
    b = b_init
    cost_history = []

    for i in range(iterations):
        dj_dw, dj_db = compute_gradient(x, y, w, b)

        # Update parameters using learning rate (alpha)
        w -= alpha * dj_dw
        b -= alpha * dj_db

        # Track cost for visualization
        cost = compute_cost(x, y, w, b)
        cost_history.append(cost)

        # Print every 10% of iterations
        if i % (iterations // 10) == 0 or i == iterations - 1:
            print(f"Iteration {i:4}: Cost = {cost:.4f}, w = {w:.4f}, b = {b:.4f}")

    return w, b, cost_history

# ---------- STEP 6: MAKE A PREDICTION ----------
# Predict profit given population using learned w and b
def predict(x, w, b):
    return w * x + b

# ---------- STEP 7: MAIN FUNCTION ----------
if __name__ == "__main__":
    # Load dataset
    x_train, y_train = load_data()

    # Visualize the dataset
    plot_data(x_train, y_train)

    # Initialize parameters
    initial_w = 0.0  # Start weight (slope)
    initial_b = 0.0  # Start bias (intercept)
    alpha = 0.01     # Learning rate (controls step size)
    iterations = 1500  # Number of gradient descent iterations

    # Train the model using gradient descent
    w_final, b_final, cost_history = gradient_descent(
        x_train, y_train, initial_w, initial_b, alpha, iterations
    )

    # ---------- STEP 8: MAKE PREDICTIONS ----------
    pop1 = 3.5
    pop2 = 7.0
    print(f"\n📈 For population = 35,000 → Predicted profit = ${predict(pop1, w_final, b_final) * 10000:.2f}")
    print(f"📈 For population = 70,000 → Predicted profit = ${predict(pop2, w_final, b_final) * 10000:.2f}")
