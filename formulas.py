import math


def T_top(T_prop, T_ver):
    """
Time to construct topology
    :param T_prop: Time to transmit all LAMs to all nodes
    :param T_ver: Time to verify all group signatures
    :return: T_prop + T_ver
    """
    return T_prop + T_ver


def T_ver(N, Tver_gsig):
    """
Time to verify all N group signatures
    :param N: Number of group signatures
    :param Tver_gsig: Time to verify a single group signature
    :return: N * Tver_gsig
    """
    return N * Tver_gsig


def T_prop(N, LAM_size, MaxNumTx, BW):
    """
Time to transmit all LAMs to all nodes
    :param N: Number of group signatures
    :param LAM_size: Size of a LAM (unit should match BW)
    :param MaxNumTx: Maximum number of simultaneous transmissions
    :param BW: Bandwidth of the wireless channel, in data transmitted per second (e.g., 10 MBps)
    :return: (N**2 * LAM_size) / (MaxNumTx * BW)
    """
    return (N**2 * LAM_size) / (MaxNumTx * BW)


def SIR(d, D, alpha):
    """
Signal interference
    :param d: Distance between sender and receiver
    :param D: Distance between interferer and receiver
    :param alpha: Power loss exponent, assumes values between 2 and 4
    :return: (d**-alpha)/(2*(D-d)**-alpha + (D-d/2)**-alpha + D**-alpha + (D+d/2)**-alpha + (D+d)**-alpha)
    """
    if alpha < 2 or alpha > 4:
        raise ValueError("alpha must be between 2 and 4")
    na = -alpha
    return (d**na)/(2*(D-d)**na + (D-d/2)**na + D**na + (D+d/2)**na + (D+d)**na)


def D_min(alpha, z_0, d):
    """
Minimum distance to interferer
    :param alpha: Power loss exponent, assumes values between 2 and 4
    :param z_0: Capture threshold (1 = perfect capture, inf = no capture)
    :param d: Distance between sender and receiver
    :return: (6*z_0*d)**(1/alpha)
    """
    if alpha < 2 or alpha > 4:
        raise ValueError("alpha must be between 2 and 4")
    return (6*z_0*d)**(1/alpha)


def MaxNumTx(L, D_min):
    """
Maximum number of simultaneous transmissions
    :param L: For area Length and Width (assuming area=L**2)
    :param D_min: Minimum distance to interferer, satisfying SIR
    :return:
    """
    return (2*L**2)/(math.sqrt(3) * D_min**2)


def d_avg(N, lm):
    """
Average distance between nodes according to a Poisson process
    :param N: Number of nodes
    :param lm: Number of nodes per unit area (m**2)
    :return: (128/(45*math.pi))*math.sqrt(N/(lm*math.pi))
    """
    return (128/(45*math.pi))*math.sqrt(N/(lm*math.pi))


def T_prop_assum_Dmin(d, LAM_size, N, BW, L):
    return (60*d*LAM_size*N**2*math.sqrt(3))/(2*BW*L**2)


def T_prop_assum(N, LAM_size, BW, L, lm):
    return (N**(5/2)*LAM_size*256)/(BW*L**2*math.pi**(3/2)*math.sqrt(3*lm))


def N_max(L, LAM_prd, f_prd, BW, LAM_size, lm):
    return L**(4/5)*math.sqrt((LAM_prd*f_prd*BW*(math.pi**(3/2)*math.sqrt(3*lm)))/(LAM_size*256))


def N_max_full(alpha, lm, T_prop, L, BW, LAM_size, z_0):
    return (
        (T_prop * 2 * L**2 * BW)
        / (LAM_size*math.sqrt(3)*((768*z_0)/(45*math.pi*math.sqrt(lm*math.pi)))**(2/alpha))
    )**(1/(2+1/alpha))

