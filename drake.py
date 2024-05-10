def drake_equation(R_star, f_p, n_e, f_l, f_i, f_c, L):
    """
    Calculate the Drake Equation to estimate the number of active, communicative extraterrestrial civilizations.

    Parameters:
    - R_star (float): Average rate of star formation in our galaxy per year.
    - f_p (float): Fraction of those stars that have planetary systems.
    - n_e (float): Average number of planets that can potentially support life per star with planets.
    - f_l (float): Fraction of planets that could support life that actually develop life at some point.
    - f_i (float): Fraction of planets with life that actually develop intelligent life.
    - f_c (float): Fraction of civilizations that develop a technology that releases detectable signs.
    - L (float): Length of time such civilizations release detectable signals into space, in years.

    Returns:
    - N (float): Number of civilizations in our galaxy with which communication might be possible.
    """
    N = R_star * f_p * n_e * f_l * f_i * f_c * L

    return N

# Speculative Values Originally From https://web.njit.edu/~gary/202/Lecture27.html then updated with new data collected
R_star = 7  # New stars per year - total number of stars in the galaxy (about 100 billion), and divide by the age of the galaxy (about 14 billion years), to get about 7/year.
f_p = 0.5  # Fraction with planetary systems - Source: Cassan, A., et al. (2012). "One or more bound planets per Milky Way star from microlensing observations." Nature.
n_e = 0.057  # Habitable planets per star system - Source: Petigura, E. A., Howard, A. W., & Marcy, G. W. (2013). "Prevalence of Earth-size planets orbiting Sun-like stars." Proceedings of the National Academy of Sciences.
f_l = 0.1  # Fraction where life develops - speculative - Feel Free to Submit a PR with a citation.
f_i = 0.1  # Fraction developing intelligent life - speculative - Feel Free to Submit a PR with a citation.
f_c = 0.3  # Fraction releasing detectable signals - speculative - Feel Free to Submit a PR with a citation.
L = 1000  # Length of detectable signal emission in years - speculative - Feel Free to Submit a PR with a citation.

# Calculate the number of detectable civilizations
N = drake_equation(R_star, f_p, n_e, f_l, f_i, f_c, L)
print(f"Estimated number of communicative civilizations: {N}")
