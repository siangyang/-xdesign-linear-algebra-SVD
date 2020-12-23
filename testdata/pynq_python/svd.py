from __future__ import print_function
import numpy as np
import sys
import struct

sys.path.append('/home/xilinx')
from pynq import Overlay
def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])
def hex_to_float(h):
    return float(struct.unpack('<f', struct.pack('<I', h))[0])

if __name__ == "main":
    print('Entry:', sys.argv[0])
    print('System argument(s):', len(sys.argv))

    print('Start of \"' + sys.argv[0] + "\"")

    ol = Overlay("/home/xilinx/IPBitFiles/svd.bit")
    regIP = ol.svd_top_0

    A_ROWS = 6
    A_COLS = 6
    A = np.random.rand(A_ROWS, A_COLS)
    U = np.zeros((A_ROWS, A_COLS))
    S = np.zeros((A_ROWS, A_COLS))
    V = np.zeros((A_ROWS, A_COLS))

    BASE_A = 0x100
    BASE_S = 0x200
    BASE_U = 0x300
    BASE_V = 0x400

    for r in range(A_ROWS):
        for c in range(A_COLS):
            regIP.write(BASE_A + 4*(A_ROWS*r+c), int(float_to_hex(A[r][c]), 0))

    for i in range(1000):
        for r in range(A_ROWS):
            for c in range(A_COLS):
                s = regIP.read(BASE_S + 4*(A_ROWS*r+c))
                u = regIP.read(BASE_U + 4*(A_ROWS*r+c))
                v = regIP.read(BASE_V + 4*(A_ROWS*r+c))

                S[r][c] = hex_to_float(s)
                U[r][c] = hex_to_float(u)
                V[r][c] = hex_to_float(v)

    print("==========Original A==========")
    print(A)
    print("==============================")

    print("==========Estmated U==========")
    print(U)
    print("==============================")

    print("==========Estmated S==========")
    print(S)
    print("==============================")

    print("==========Estmated V==========")
    print(V)
    print("==============================")

    recon_A = S.dot(U).dot(V)
    print("==========Reconst. A==========")
    print(recon_A)
    print("==============================")

    print("YOUR MSE :", ((recon_A-A)**2).mean())
    print("Exit process")
