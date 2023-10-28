#!/usr/bin/python3

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    try:
        np_m_a = np.array(m_a)
        np_m_b = np.array(m_b)

        result = np.dot(np_m_a, np_m_b)

        return result.tolist()
    except (ValueError, TypeError):
        raise ValueError("m_a and m_b must be a list of lists of integers or floats") from None
    except Exception:
        raise ValueError("m_a and m_b can't be multiplied") from None
