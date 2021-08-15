# Epidemic Modeling with Python

This repo contains the code for simulating and fitting a SIR model to real COVID-19 data. Especially, I fit a SIR model
for the 1st wave of COVID-19 in Brazil, using data collected from [Bing](https://github.com/microsoft/Bing-COVID-19-Data). The fit procedure is
done through a genetic algorithm inspired in [Storn and Price, 1997]. __Note:__ The simulations and the fitting procedure are for study purposes, they __do not__ reflect a serious model for the COVID-19 pandemic in Brazil.

## Repo Structure

In ```./models``` you may find an abstract object for an abstract epidemic model. in ```./models/sir.py``` you may find
the code for simulating a SIR model with transmissibility β, and recoverability γ. The ```./data``` directory contains
the data mined from [Bing](https://github.com/microsoft/Bing-COVID-19-Data). In ```Analysis of COVID-19 Data Brazil.ipynb```
you can find the data analysis and fitting procedure.

## Results

Using the differential evolution algorithm, we were able to estimate β = 1.596 and γ = 1.564, yielding an R0 of 1.02. This
is far from the [values reported from COVID-19](https://en.wikipedia.org/wiki/Basic_reproduction_number), especially, the R0
for the COVID-19 ancestral strain (that is presumed to cause the 1st wave of COVID-19 in Brazil) has an R0 between 2.39 to 3.44 according
to [Billah et al., 2020]. There may be two reasons for the incosistency between our results and theirs,

1. The differential evolution algorithm fails to find β and γ correctly,

2. The cases are being underreported, most probably by lack of testing (the case for Brazil).

In either case even though the model fits the epidemic curve for the 1st wave, it cannot be used for forecasting.

## References

[Storn and Price, 1997] Storn, R., & Price, K. (1997). Differential evolution–a simple and efficient heuristic for global optimization over continuous spaces. Journal of global optimization, 11(4), 341-359.

[Billah et al., 2020] Billah, M. A., Miah, M. M., & Khan, M. N. (2020). Reproductive number of coronavirus: A systematic review and meta-analysis based on global level evidence. PloS one, 15(11), e0242128.
