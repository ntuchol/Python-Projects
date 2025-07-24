import numpy as np

    data = np.array([1, 2, 4, 7, 11])
    differences = np.diff(data)
    print(differences)
    # Output: [1 2 3 4]

    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    gradient = np.gradient(y, x)
    print(gradient)
    # Output: (array of approximated derivative values)