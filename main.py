

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
    :return:
    """
    return N * Tver_gsig


def T_prop(N, LAM_size, MaxNumTx, BW):
    return (N**2 * LAM_size) / (MaxNumTx * BW)


