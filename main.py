import formulas


def main():
    N = 700
    Tver_gsig = 0.01
    LAM_size = 350
    BW = 1000*1024
    alpha = 2
    z_0 = 10
    L = 1000
    lm = 0.02
    d = formulas.d_avg(N, lm)
    T_ver = formulas.T_ver(N, Tver_gsig)
    D_min = formulas.D_min(alpha, z_0, d)
    MaxNumTx = formulas.MaxNumTx(L, D_min)
    T_prop = formulas.T_prop(N, LAM_size, MaxNumTx, BW)
    print(f"T_prop: {T_prop}")
    print(f"T_prop (assume alpha=2, z_0=10): {formulas.T_prop_assum_Dmin(d, LAM_size, N, BW, L)}")
    print(f"T_prop (include poisson): {formulas.T_prop_assum(N, LAM_size, BW, L, lm)}")
    print(f"T_ver: {T_ver}")
    print(f"T_top: {formulas.T_top(T_prop, T_ver)}")
    LAM_prd = 5
    f_prd = 0.1
    print(f"N_max (assumptions, original): {formulas.N_max_assum_original(L, LAM_prd, f_prd, BW, LAM_size, lm)}")
    print(f"N_max (assumptions, correct): {formulas.N_max_assum(L, LAM_prd, f_prd, BW, LAM_size, lm)}")
    T_prop = LAM_prd * f_prd
    print(f"N_max (full): {formulas.N_max_full(alpha, lm, T_prop, L, BW, LAM_size, z_0)}")


if __name__ == "__main__":
    main()

