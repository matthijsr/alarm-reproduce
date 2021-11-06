import formulas
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_size(saveloc):
    BW = 1024 * 1024
    LAM_prd = 5
    f_prd = 0.1
    T_prop = LAM_prd * f_prd
    d = 50

    x = np.array(range(1000, 5001, 500))
    y1 = [formulas.N_max_d(T_prop, BW, L, d, 50) for L in x]
    plt.plot(x, y1, label='LAM_size=50B', linestyle='solid', color='red')
    y2 = [formulas.N_max_d(T_prop, BW, L, d, 100) for L in x]
    plt.plot(x, y2, label='LAM_size=100B', linestyle='dashed', color='green')
    y3 = [formulas.N_max_d(T_prop, BW, L, d, 200) for L in x]
    plt.plot(x, y3, label='LAM_size=200B', linestyle='dotted', color='blue')
    y4 = [formulas.N_max_d(T_prop, BW, L, d, 300) for L in x]
    plt.plot(x, y4, label='LAM_size=300B', linestyle='solid', color='yellow')
    y5 = [formulas.N_max_d(T_prop, BW, L, d, 350) for L in x]
    plt.plot(x, y5, label='LAM_size=350B', linestyle='dashdot', color='grey')
    y6 = [formulas.N_max_d(T_prop, BW, L, d, 600) for L in x]
    plt.plot(x, y6, label='LAM_size=600B', linestyle='solid', color='cyan')
    y7 = [formulas.N_max_d(T_prop, BW, L, d, 750) for L in x]
    plt.plot(x, y7, label='LAM_size=750B', linestyle='dashed', color='black')
    y8 = [formulas.N_max_d(T_prop, BW, L, d, 1024) for L in x]
    plt.plot(x, y8, label='LAM_size=1024B', linestyle='dotted', color='purple')

    # plt.title(f'Maximum number of nodes for distance (d) between sender and receiver. LAM_size = {LAM_size}')

    plt.xlabel('Area Length/Width (L) in meters')
    plt.ylabel('Number of Nodes')
    plt.yticks(range(0, 12001, 1000))

    plt.xlim([1000, 5000])
    plt.ylim([0, 12000])

    # Add a grid
    plt.grid(alpha=.4)

    # Add a Legend
    plt.legend()

    # Show the plot
    plt.savefig(saveloc, bbox_inches='tight')
    plt.close()


def plot_size_fixed_length(saveloc):
    BW = 1024 * 1024
    LAM_prd = 5
    f_prd = 0.1
    T_prop = LAM_prd * f_prd
    d = 50
    L = 5000

    x = np.array(range(10, 2001, 10))
    y1 = [formulas.N_max_d(T_prop, BW, L, 50, LAM_size) for LAM_size in x]
    plt.plot(x, y1, linestyle='solid', color='red')
    # y1 = [formulas.N_max_d(T_prop, BW, L, 50, LAM_size) for LAM_size in x]
    # plt.plot(x, y1, label='d=50m', linestyle='solid', color='red')
    # y2 = [formulas.N_max_d(T_prop, BW, L, 100, LAM_size) for LAM_size in x]
    # plt.plot(x, y2, label='d=100m', linestyle='dashed', color='purple')
    # y3 = [formulas.N_max_d(T_prop, BW, L, 200, LAM_size) for LAM_size in x]
    # plt.plot(x, y3, label='d=200m', linestyle='dotted', color='green')
    # y4 = [formulas.N_max_d(T_prop, BW, L, 300, LAM_size) for LAM_size in x]
    # plt.plot(x, y4, label='d=300m', linestyle='dashdot', color='blue')

    # plt.title(f'Maximum number of nodes for distance (d) between sender and receiver. LAM_size = {LAM_size}')

    plt.xlabel('LAM_size in bytes')
    plt.ylabel('Number of Nodes')
    plt.yticks(range(0, 12001, 1000))

    plt.xlim([0, 2000])
    plt.ylim([0, 12000])

    # Add a grid
    plt.grid(alpha=.4)

    # Add a Legend
    # plt.legend()

    # Show the plot
    plt.savefig(saveloc, bbox_inches='tight')
    plt.close()


def plot_bw(saveloc):
    LAM_size=350
    LAM_prd = 5
    f_prd = 0.1
    T_prop = LAM_prd * f_prd
    d = 50

    x = np.array(range(1000, 5001, 500))
    y1 = [formulas.N_max_d(T_prop, 10 * 1024, L, d, LAM_size) for L in x]
    plt.plot(x, y1, label='BW=10 KiBps', linestyle='solid', color='red')
    y2 = [formulas.N_max_d(T_prop, 100 * 1024, L, d, LAM_size) for L in x]
    plt.plot(x, y2, label='BW=100 KiBps', linestyle='dashed', color='green')
    y3 = [formulas.N_max_d(T_prop, 200 * 1024, L, d, LAM_size) for L in x]
    plt.plot(x, y3, label='BW=200 KiBps', linestyle='dotted', color='blue')
    y4 = [formulas.N_max_d(T_prop, 500 * 1024, L, d, LAM_size) for L in x]
    plt.plot(x, y4, label='BW=500 KiBps', linestyle='solid', color='yellow')
    y5 = [formulas.N_max_d(T_prop, 1024 * 1024, L, d, LAM_size) for L in x]
    plt.plot(x, y5, label='BW=1 MiBps', linestyle='dashdot', color='grey')
    y6 = [formulas.N_max_d(T_prop, 5 * 1024 * 1024, L, d, LAM_size) for L in x]
    plt.plot(x, y6, label='BW=5 MiBps', linestyle='solid', color='cyan')
    y7 = [formulas.N_max_d(T_prop, 10 * 1024 * 1024, L, d, LAM_size) for L in x]
    plt.plot(x, y7, label='BW=10 MiBps', linestyle='dashed', color='black')
    y8 = [formulas.N_max_d(T_prop, 20 * 1024 * 1024, L, d, LAM_size) for L in x]
    plt.plot(x, y8, label='BW=20 MiBps', linestyle='dotted', color='purple')

    # plt.title(f'Maximum number of nodes for distance (d) between sender and receiver. LAM_size = {LAM_size}')

    plt.xlabel('Area Length/Width (L) in meters')
    plt.ylabel('Number of Nodes')
    plt.yticks(range(0, 20001, 1000))

    plt.xlim([1000, 5000])
    plt.ylim([0, 20000])

    # Add a grid
    plt.grid(alpha=.4)

    # Add a Legend
    plt.legend()

    # Show the plot
    plt.savefig(saveloc, bbox_inches='tight')
    plt.close()


def plot_bw_fixed_length(saveloc):
    LAM_prd = 5
    f_prd = 0.1
    T_prop = LAM_prd * f_prd
    d = 50

    x = np.array(range(1, 1000, 10))
    y1 = [formulas.N_max_d(T_prop, BW * 1024 * 1024, 5000, 50, 350) for BW in x]
    plt.plot(x, y1, label='L=5000m', linestyle='solid', color='red')
    y2 = [formulas.N_max_d(T_prop, BW * 1024 * 1024, 10000, 50, 350) for BW in x]
    plt.plot(x, y2, label='L=10000m', linestyle='dashed', color='purple')
    y3 = [formulas.N_max_d(T_prop, BW * 1024 * 1024, 15000, 50, 350) for BW in x]
    plt.plot(x, y3, label='L=15000m', linestyle='dotted', color='green')
    y4 = [formulas.N_max_d(T_prop, BW * 1024 * 1024, 20000, 50, 350) for BW in x]
    plt.plot(x, y4, label='L=20000m', linestyle='dashdot', color='yellow')

    # plt.title(f'Maximum number of nodes for distance (d) between sender and receiver. LAM_size = {LAM_size}')

    plt.xlabel('Bandwidth in Mebibytes per second')
    plt.ylabel('Number of Nodes')
    #plt.yticks(range(0, 20001, 1000))

    plt.xlim([0, 1000])
    #plt.ylim([0, 20000])

    # Add a grid
    plt.grid(alpha=.4)

    # Add a Legend
    plt.legend()

    # Show the plot
    plt.savefig(saveloc, bbox_inches='tight')
    plt.close()


def plot_distance(saveloc, LAM_size=350):
    BW = 10 * 1000 * 1024
    LAM_prd = 5
    f_prd = 0.1
    T_prop = LAM_prd * f_prd

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

    # plt.title(f'Maximum number of nodes for distance (d) between sender and receiver. LAM_size = {LAM_size}')

    plt.xlabel('Area Length/Width (L) in meters')
    plt.ylabel('Number of Nodes')
    #plt.yticks(range(500, 4501, 500))

    plt.xlim([1000, 5000])
    #plt.ylim([0, 4500])

    # Add a grid
    plt.grid(alpha=.4)

    # Add a Legend
    plt.legend()

    # Show the plot
    plt.savefig(saveloc, bbox_inches='tight')
    plt.close()


def plot_distance_mbits(saveloc, LAM_size=350):
    BW = 10 * 1000 * (1024/8)
    LAM_prd = 5
    f_prd = 0.1
    T_prop = LAM_prd * f_prd

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

    # plt.title(f'Maximum number of nodes for distance (d) between sender and receiver. LAM_size = {LAM_size}')

    plt.xlabel('Area Length/Width (L) in meters')
    plt.ylabel('Number of Nodes')
    plt.yticks(range(500, 4501, 500))

    plt.xlim([1000, 5000])
    plt.ylim([0, 4500])

    # Add a grid
    plt.grid(alpha=.4)

    # Add a Legend
    plt.legend()

    # Show the plot
    plt.savefig(saveloc, bbox_inches='tight')
    plt.close()


def plot():
    plot_size(f'graphs/a2/LAM_size.pdf')
    plot_size_fixed_length(f'graphs/a2/LAM_size_fixed_length.pdf')
    plot_bw(f'graphs/a2/bw.pdf')
    plot_bw_fixed_length(f'graphs/a2/bw_fixed_length.pdf')
    plot_distance(f'graphs/a2/10mbps.pdf')
    plot_distance_mbits(f'graphs/a2/10mbitps.pdf')


def main():
    os.makedirs('graphs/a2', exist_ok=True)

    plot()


if __name__ == "__main__":
    main()

