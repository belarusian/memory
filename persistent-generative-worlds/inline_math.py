import re

# Ordered from most specific/longest to least specific, to avoid a shorter
# pattern eating part of a longer one. Matched against RAW unicode text
# (before LaTeX-special-character escaping).
TOKEN_PATTERNS = [
    (r'∂L/∂Ṁᵢ', r'\partial L/\partial \dot{M}_i'),
    (r'∂L/∂Ṁ\b', r'\partial L/\partial \dot{M}'),
    (r'∂L/∂M\b', r'\partial L/\partial M'),
    (r'ℝ\^d-valued', r'\mathbb{R}^d\text{-valued}'),
    (r'ℝ\^d', r'\mathbb{R}^d'),
    (r'argmin_\{Y ∈ C\}', r'\operatorname*{argmin}_{Y \in C}'),
    (r'φ_\*C_S\b', r'\varphi_*C_S'),
    (r'M_\{t\+1\}', r'M_{t+1}'),
    (r'M_\{t\+2\}', r'M_{t+2}'),
    (r'z_\{t\+1\}\(x\)', r'z_{t+1}(x)'),
    (r'R_\{t\+1\}\(x\)', r'R_{t+1}(x)'),
    (r'R_\{t\+1\}', r'R_{t+1}'),
    (r'w\^\{t\+1\}_\{ij\}', r'w^{t+1}_{ij}'),
    (r'w\^t_\{ij\}', r'w^t_{ij}'),
    (r'w_\{ij\}', r'w_{ij}'),
    (r'K_ij\b', r'K_{ij}'),
    (r'affordance_\{ij\}', r'\mathrm{affordance}_{ij}'),
    (r'event_t\(x\)', r'\mathrm{event}_t(x)'),
    (r'couples_to\b', r'\mathrm{couples\_to}'),
    (r'ΔΦ_joint\b', r'\Delta\Phi_{\text{joint}}'),
    (r'Δv_joint\b', r'\Delta v_{\text{joint}}'),
    (r'Φ_whole_body\b', r'\Phi_{\text{whole-body}}'),
    (r'ρ_c\(x,\s*a\)', r'\rho_c(x,a)'),
    (r'ρ_c\(x\)', r'\rho_c(x)'),
    (r'ρ_c\b', r'\rho_c'),
    (r'CueCat\^op\b', r'\mathrm{CueCat}^{\mathrm{op}}'),
    (r'ΔS_t\(x\)', r'\Delta S_t(x)'),
    (r'M_t\(x\)', r'M_t(x)'),
    (r'Φ_t\(x\)', r'\Phi_t(x)'),
    (r'v_t\(x\)', r'v_t(x)'),
    (r'S_t\(x\)', r'S_t(x)'),
    (r'z_t\(x\)', r'z_t(x)'),
    (r'R_t\(x\)', r'R_t(x)'),
    (r'L_t\(x\)', r'L_t(x)'),
    (r'F_phys\(M\)', r'F_{\mathrm{phys}}(M)'),
    (r'F_phys\b', r'F_{\mathrm{phys}}'),
    (r'F_ψ\b', r'F_\psi'),
    (r'F_cue\b', r'F_{\mathrm{cue}}'),
    (r'F_field\b', r'F_{\mathrm{field}}'),
    (r'C_S\b', r'C_S'),
    (r'C_A\b', r'C_A'),
    (r'C_z\b', r'C_z'),
    (r'C_R\b', r'C_R'),
    (r'O_θ\b', r'O_\theta'),
    (r'O\*F_\{?field\}?\b', r'O^*F_{\mathrm{field}}'),
    (r'Π_C\b', r'\Pi_C'),
    (r'M\*(?=[\s.,;:)])', r'M^*'),
    (r'M_t\b', r'M_t'),
    (r'R_t\b', r'R_t'),
    (r'S_t\b', r'S_t'),
    (r'Φ_t\b', r'\Phi_t'),
    (r'v_t\b', r'v_t'),
    (r'z_t\b', r'z_t'),
    (r'A_t\b', r'A_t'),
    (r'y_t\b', r'y_t'),
    (r'δH\b', r'\delta H'),
    (r'δM\b', r'\delta M'),
    (r'δS\b', r'\delta S'),
    (r'δΦ\b', r'\delta \Phi'),
    (r'δv\b', r'\delta v'),
    (r'ψ\(t\)', r'\psi(t)'),
    (r'∂_t Π\b', r'\partial_t \Pi'),
    (r'Δψ_a\b', r'\Delta\psi_a'),
    (r'Δψ_b\b', r'\Delta\psi_b'),
    (r'Δψ', r'\Delta\psi'),
    (r'inf_\{Z ∈ C\}', r'\inf_{Z \in C}'),
    (r'Z_n\b', r'Z_n'),
    (r'T_\{M\*\}C\b', r'T_{M^*}C'),
    (r'M_s\b', r'M_s'),
    (r'M_0\b', r'M_0'),
    (r'Ṁ_s\b', r'\dot{M}_s'),
    (r'Ṁᵢ\b', r'\dot{M}_i'),
    (r'Ṁ\b', r'\dot{M}'),
    (r'Ψ\^n\b', r'\Psi^n'),
    (r'Ψ\^\{n\+1\}', r'\Psi^{n+1}'),
    (r'k\^n\b', r'k^n'),
    (r'dM_\{s,i\}/ds', r'dM_{s,i}/ds'),
    (r'\|_\{s=0\}', r'\big|_{s=0}'),
    (r'dM_s/ds', r'dM_s/ds'),
    (r'Hess H\|_C', r'\operatorname{Hess}H|_C'),
    (r'H¹\(𝒢, F_field\)', r'H^1(\mathcal{G}, F_{\mathrm{field}})'),
    (r'H¹\b', r'H^1'),
    (r'Σᵢ', r'\textstyle\sum_i'),
]

COMPILED = [(re.compile(p), r) for p, r in TOKEN_PATTERNS]

def mathify_inline(line):
    """Replace known inline math tokens in a raw (unescaped) text line with
    placeholders, returning (new_line, placeholder_map)."""
    placeholders = {}
    def make_repl(latex):
        idx = len(placeholders)
        key = f"\uE000{idx}\uE001"
        placeholders[key] = f"\\({latex}\\)"
        return key
    for pat, repl in COMPILED:
        line = pat.sub(lambda m, r=repl: make_repl(r), line)
    return line, placeholders

def restore_placeholders(escaped_line, placeholders):
    for key, val in placeholders.items():
        escaped_line = escaped_line.replace(key, val)
    return escaped_line
