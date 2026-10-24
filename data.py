# The data of the assignment and one function to compute all the metrics

genuine = [0.91, 0.88, 0.84, 0.79, 0.76, 0.72, 0.66, 0.61, 0.55, 0.48]
impostor = [0.62, 0.53, 0.47, 0.41, 0.38, 0.33, 0.29, 0.24, 0.18, 0.12]
FTA = 0.05


def rates(tau):
    # count the false non-matches (genuine scores below the threshold)
    false_non_matches = 0
    for s in genuine:
        if s < tau:
            false_non_matches = false_non_matches + 1

    # count the false matches (impostor scores above or equal to the threshold)
    false_matches = 0
    for s in impostor:
        if s >= tau:
            false_matches = false_matches + 1

    # matcher level
    FNMR = false_non_matches / len(genuine)
    FMR = false_matches / len(impostor)
    TAR = 1 - FNMR
    TRR = 1 - FMR

    # system level (with the failure-to-acquire rate)
    FAR = (1 - FTA) * FMR
    FRR = FTA + (1 - FTA) * FNMR

    return FMR, FNMR, TAR, TRR, FAR, FRR
