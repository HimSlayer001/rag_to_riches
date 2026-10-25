import numpy as np

#i need a query vector + embedded Database to
def cosine_similarity(a: list[float], b: list[float]
)->float:
    a = np.array(a)
    b = np.array(b)

    denominator = np.linalg.norm(a)*np.linalg.norm(b)

    if denominator==0:
        return 0.0

    return float(np.dot(a,b)/denominator)



