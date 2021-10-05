import formulas
import matplotlib.pyplot as plt
import numpy as np
import os

def test():
    N = 700
    Tver_gsig = 0.01
    LAM_size = 350
    BW = 1024*1024
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
    print(f"N_max (full): {formulas.N_max(alpha, lm, T_prop, L, BW, LAM_size, z_0)}")

    print("Target: 0.5 :")
    print(f"T_prop (assume alpha=2, z_0=10, d=50, N=3800, L=5000): {formulas.T_prop_assum_Dmin(50, LAM_size, 3800, BW, 5000)}")
    print(f"T_prop (assume alpha=2, z_0=10, d=50, N=4100, L=5000): {formulas.T_prop_assum_Dmin(50, LAM_size, 4100, BW, 5000)}")


def plot_LAM_period(func, saveloc, LAM_size=350):
    BW = 1024 * 1024
    alpha = 2
    z_0 = 10
    lm = 0.02
    f_prd = 0.1

    x = np.array(range(1000, 5001, 500))
    y1 = [func(L, 5, f_prd, BW, LAM_size, lm) for L in x]
    plt.plot(x, y1, label='05sec LAM period', linestyle='solid', color='red')
    y2 = [func(L, 10, f_prd, BW, LAM_size, lm) for L in x]
    plt.plot(x, y2, label='10sec LAM period', linestyle='dashed', color='green')
    y3 = [func(L, 15, f_prd, BW, LAM_size, lm) for L in x]
    plt.plot(x, y3, label='15sec LAM period', linestyle='dotted', color='blue')
    y4 = [func(L, 20, f_prd, BW, LAM_size, lm) for L in x]
    plt.plot(x, y4, label='20sec LAM period', linestyle=(0, (1, 1)), color='purple')
    y5 = [func(L, 25, f_prd, BW, LAM_size, lm) for L in x]
    plt.plot(x, y5, label='25sec LAM period', linestyle='dashdot', color='grey')
    y6 = [func(L, 30, f_prd, BW, LAM_size, lm) for L in x]
    plt.plot(x, y6, label='30sec LAM period', linestyle=(0, (3, 1, 1, 1, 1, 1)), color='orange')

    plt.title(f'Maximum number of nodes for time required to propagate LAMs. LAM_size = {LAM_size}')

    plt.xlabel('Area Length/Width (L) in meters')
    plt.ylabel('Number of Nodes')
    plt.yticks(range(0, 8001, 1000))

    # Add a grid
    plt.grid(alpha=.4)

    # Add a Legend
    plt.legend()

    # Show the plot
    plt.savefig(saveloc, bbox_inches='tight')
    plt.close()


def plot_lambda(func, saveloc, LAM_size=350):
    BW = 1024 * 1024
    alpha = 2
    z_0 = 10
    LAM_prd = 5
    f_prd = 0.1

    x = np.array(range(1000, 5001, 500))
    y1 = [func(L, LAM_prd, f_prd, BW, LAM_size, 0.02) for L in x]
    plt.plot(x, y1, label='Nodes/Unit Area = 0.02', linestyle='solid', color='red')
    y2 = [func(L, LAM_prd, f_prd, BW, LAM_size, 0.04) for L in x]
    plt.plot(x, y2, label='Nodes/Unit Area = 0.04', linestyle='dashed', color='green')
    y3 = [func(L, LAM_prd, f_prd, BW, LAM_size, 0.06) for L in x]
    plt.plot(x, y3, label='Nodes/Unit Area = 0.06', linestyle='dotted', color='blue')
    y4 = [func(L, LAM_prd, f_prd, BW, LAM_size, 0.08) for L in x]
    plt.plot(x, y4, label='Nodes/Unit Area = 0.08', linestyle=(0, (1, 1)), color='purple')
    y5 = [func(L, LAM_prd, f_prd, BW, LAM_size, 0.1) for L in x]
    plt.plot(x, y5, label='Nodes/Unit Area = 0.1', linestyle='dashdot', color='grey')

    plt.title(f'Maximum number of nodes for density of nodes. LAM_size = {LAM_size}')

    plt.xlabel('Area Length/Width (L) in meters')
    plt.ylabel('Number of Nodes')
    plt.yticks(range(500, 4501, 500))

    # Add a grid
    plt.grid(alpha=.4)

    # Add a Legend
    plt.legend()

    # Show the plot
    plt.savefig(saveloc, bbox_inches='tight')
    plt.close()


def plot_distance(saveloc, LAM_size=350):
    BW = 1024 * 1024
    alpha = 2
    z_0 = 10
    LAM_prd = 5
    f_prd = 0.1
    T_prop = LAM_prd * f_prd
    lm = 0.02

    x = np.array(range(1000, 5001, 500))
    y1 = [formulas.N_max_d(T_prop, BW, L, 50, LAM_size) for L in x]
    plt.plot(x, y1, label='d=50m', linestyle='solid', color='red')
    y2 = [formulas.N_max_d(T_prop, BW, L, 100, LAM_size) for L in x]
    plt.plot(x, y2, label='d=100m', linestyle='dashed', color='green')
    y3 = [formulas.N_max_d(T_prop, BW, L, 150, LAM_size) for L in x]
    plt.plot(x, y3, label='d=150m', linestyle='dotted', color='blue')
    y4 = [formulas.N_max_d(T_prop, BW, L, 200, LAM_size) for L in x]
    plt.plot(x, y4, label='d=200m', linestyle=(0, (1, 1)), color='purple')
    y5 = [formulas.N_max_d(T_prop, BW, L, 250, LAM_size) for L in x]
    plt.plot(x, y5, label='d=250m', linestyle='dashdot', color='grey')
    y6 = [formulas.N_max_d(T_prop, BW, L, 300, LAM_size) for L in x]
    plt.plot(x, y6, label='d=300m', linestyle=(0, (3, 1, 1, 1, 1, 1)), color='orange')

    plt.title(f'Maximum number of nodes for distance (d) between sender and receiver. LAM_size = {LAM_size}')

    plt.xlabel('Area Length/Width (L) in meters')
    plt.ylabel('Number of Nodes')
    plt.yticks(range(500, 4501, 500))

    # Add a grid
    plt.grid(alpha=.4)

    # Add a Legend
    plt.legend()

    # Show the plot
    plt.savefig(saveloc, bbox_inches='tight')
    plt.close()


def plot_for_size(LAM_size=350):
    plot_LAM_period(formulas.N_max_assum_original, f'graphs/original/LAM_prd_{LAM_size}.pdf', LAM_size)
    plot_LAM_period(formulas.N_max_assum, f'graphs/corrected/LAM_prd_{LAM_size}.pdf', LAM_size)
    plot_lambda(formulas.N_max_assum_original, f'graphs/original/density_{LAM_size}.pdf', LAM_size)
    plot_lambda(formulas.N_max_assum, f'graphs/corrected/density_{LAM_size}.pdf', LAM_size)
    plot_distance(f'graphs/original/distance_{LAM_size}.pdf', LAM_size)


def main():
    # test()

    os.makedirs('graphs/original', exist_ok=True)
    os.makedirs('graphs/corrected', exist_ok=True)

    # Paper claims LAM_size = 350 bytes
    plot_for_size(350)

    # But 250/300 is a closer match to their graphs?
    plot_for_size(300)
    plot_for_size(250)


if __name__ == "__main__":
    main()

