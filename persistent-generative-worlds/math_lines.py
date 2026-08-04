# Exact standalone display-equation lines (stripped) mapped to proper LaTeX math,
# keyed by (chapter_number, verbatim stripped source line).
MATH_LINES = {
(6, "O_θ(M_t) = y_t,"):
    r"\[ O_\theta(M_t) = y_t, \]",
(6, "M_t : X → ℝ^d."):
    r"\[ M_t : X \to \mathbb{R}^d. \]",
(6, "M_t —(O_θ)→ y_t —(reasoning)→ Δψ —(Π_C)→ Y —(Commit)→ M_{t+1}."):
    r"\[ M_t \xrightarrow{O_\theta} y_t \xrightarrow{\text{reasoning}} \Delta\psi \xrightarrow{\Pi_C} Y \xrightarrow{\text{Commit}} M_{t+1}. \]",
(7, "M_t(x) = (Φ_t(x), v_t(x), S_t(x), R_t(x), z_t(x))."):
    r"\[ M_t(x) = \bigl(\Phi_t(x),\, v_t(x),\, S_t(x),\, R_t(x),\, z_t(x)\bigr). \]",
(7, "M_t(x) = (Φ_t, v_t, S_t, A_t, R_t, z_t),"):
    r"\[ M_t(x) = (\Phi_t,\, v_t,\, S_t,\, A_t,\, R_t,\, z_t), \]",
(7, "A : M × C → P(Δψ),"):
    r"\[ A : M \times C \to \mathcal{P}(\Delta\psi), \]",
(8, "ΔS_t(x) ≥ 0."):
    r"\[ \Delta S_t(x) \ge 0. \]",
(9, "z_{t+1}(x) = z_t(x) + λ · ẑ(x)."):
    r"\[ z_{t+1}(x) = z_t(x) + \lambda \cdot \hat{z}(x). \]",
(10, "A : M × C → P(Δψ),"):
    r"\[ A : M \times C \to \mathcal{P}(\Delta\psi), \]",
(10, "w^{t+1}_{ij} = (1 − α) w^t_{ij} + α · affordance_{ij},"):
    r"\[ w^{t+1}_{ij} = (1-\alpha)\, w^t_{ij} + \alpha \cdot \mathrm{affordance}_{ij}, \]",
(10, "F_cue : CueCat^op → Set,"):
    r"\[ F_{\mathrm{cue}} : \mathrm{CueCat}^{\mathrm{op}} \to \mathrm{Set}, \]",
(11, "R_{t+1}(x) = R_t(x) ⊕ event_t(x),"):
    r"\[ R_{t+1}(x) = R_t(x) \oplus \mathrm{event}_t(x), \]",
(12, "M_{t+1} = M_t + Δψ."):
    r"\[ M_{t+1} = M_t + \Delta\psi. \]",
(13, "∂_t Π = −δH/δM + F_ψ(M, p, a, o),"):
    r"\[ \partial_t \Pi = -\delta H/\delta M + F_\psi(M, p, a, o), \]",
(13, "π(a | x) ∝ exp(β · ρ_c(x, a)),"):
    r"\[ \pi(a \mid x) \propto \exp\bigl(\beta \cdot \rho_c(x, a)\bigr), \]",
(14, "Y = argmin_{Y ∈ C} ‖Y − (M_t + Δψ)‖²."):
    r"\[ Y = \operatorname*{argmin}_{Y \in C} \|Y - (M_t + \Delta\psi)\|^2. \]",
(16, "M* = Π_C(M* + Δψ)."):
    r"\[ M^* = \Pi_C(M^* + \Delta\psi). \]",
(18, "C = C_S ∩ C_z ∩ C_R ∩ C_A ∩ ⋯,"):
    r"\[ C = C_S \cap C_z \cap C_R \cap C_A \cap \cdots, \]",
(19, "L = ½‖v‖² − Φ − δS + η⟨v, ∇Φ⟩."):
    r"\[ L = \tfrac{1}{2}\|v\|^2 - \Phi - \delta S + \eta\langle v, \nabla\Phi\rangle. \]",
(19, "F_phys(M) = −δH/δM."):
    r"\[ F_{\mathrm{phys}}(M) = -\delta H/\delta M. \]",
(20, "∂Φ/∂t = δH/δv, ∂v/∂t = −δH/δΦ."):
    r"\[ \partial\Phi/\partial t = \delta H/\delta v, \qquad \partial v/\partial t = -\delta H/\delta\Phi. \]",
(21, "η : F_cue ⇒ O*F_field,"):
    r"\[ \eta : F_{\mathrm{cue}} \Rightarrow O^*F_{\mathrm{field}}, \]",
(33, "Z(t) = r(t) e^{iψ(t)},"):
    r"\[ Z(t) = r(t)\, e^{i\psi(t)}, \]",
(40, "y_t = O_θ(W),"):
    r"\[ y_t = O_\theta(W), \]",
}
