# hypothesis_testing.py
from scipy import stats as st

def hypothesis_test(good_weather, bad_weather, alpha=0.05):
    results = st.ttest_ind(good_weather, bad_weather)
    print('valor p:', results.pvalue)

    if (results.pvalue < alpha):
        print("Aprobamos Hipotesis Alternativa")
        print("Hipotesis Alternativa (H1): La duración promedio de los viajes cambia los sábados lluviosos.")
    else:
        print("Aprobamos la Hipotesis Nula")
        print("Hipotesis nula (H0): La duración promedio no cambia los sábados lluviosos.")
