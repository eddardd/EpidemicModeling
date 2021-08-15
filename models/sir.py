import numpy as np

from models import AbstractModel
from scipy.integrate import odeint

class SIRModel(AbstractModel):
    def __init__(self, β=1.0, γ=1.0, N=1.0):
        super().__init__()
        self.β = β
        self.γ = γ
        self.N = N

    def dynamics(self, state, t):
        S, I, R = state
        dS = - (self.β / self.N) * I * S
        dI = (self.β / self.N) * I * S - self.γ * I
        dR = self.γ * I

        return np.array([dS, dI, dR])

    def __call__(self, time_span, initial_conditions):
        return odeint(self.dynamics, initial_conditions, time_span)