# Asfiya Misba - 1002028239
# AI - Assignment 3
# Spring 2023
import sys


def main():
    # Open file and read lines
    with open('training_data.txt', 'r') as f:
        lines = f.readlines()

    values = [[int(x) for x in line.strip().split()] for line in lines]
    total = 0
    counts = {'B': [0, 0], 'G': [0, 0], 'C': [0, 0], 'F': [0, 0]}
    for col_idx, col_name in enumerate(['B', 'G', 'C', 'F']):
        for row in values:
            counts[col_name][row[col_idx]] += 1

    total = 365
    P_B_t = counts['B'][1] / total
    P_B_f = 1 - P_B_t
    print('P(B=true) = ', P_B_t)
    print('P(B=false) = ', P_B_f)

    P_C_t = counts['C'][1] / total
    P_C_f = 1 - P_C_t
    print('P(C=true) = ', P_C_t)
    print('P(C=false) = ', P_C_f)

    count = 0
    for line in lines:
        values = line.split()
        if values[0] == '1' and values[1] == '1':
            count += 1

    P_G_t_given_B_t = (count / total) / P_B_t
    P_G_f_given_B_t = 1 - P_G_t_given_B_t
    print('P(G=true | B=true) = ', P_G_t_given_B_t)
    print('P(G=false | B=true) = ', P_G_f_given_B_t)

    count_gt_bf = 0
    for line in lines:
        values = line.split()
        if values[0] == '0' and values[1] == '1':
            count_gt_bf += 1

    prob_notb = counts['B'][0] / total
    P_G_t_given_B_f = (count_gt_bf / total) / prob_notb
    P_G_f_given_B_f = 1 - P_G_t_given_B_f
    print('P(G=true | B=false) = ', P_G_t_given_B_f)
    print('P(G=false | B=false) = ', P_G_f_given_B_f)

    countgc = 0
    countf = 0
    for line in lines:
        values = line.split()
        if values[1] == '1' and values[2] == '1':
            if values[3] == '1':
                countf += 1
            countgc += 1

    P_F_t_given_G_t_C_t = countf / countgc
    P_F_f_given_G_t_C_t = 1 - P_F_t_given_G_t_C_t
    print('P(F=true | G=true, C=true) = ', P_F_t_given_G_t_C_t)
    print('P(F=false | G=true, C=true) = ', P_F_f_given_G_t_C_t)

    countg_notc = 0
    countf = 0
    for line in lines:
        values = line.split()
        if values[1] == '1' and values[2] == '0':
            if values[3] == '1':
                countf += 1
            countg_notc += 1

    P_F_t_given_G_t_C_f = countf / countg_notc
    P_F_f_given_G_t_C_f = 1 - P_F_t_given_G_t_C_f
    print('P(F=true | G=true, C=false) = ', P_F_t_given_G_t_C_f)
    print('P(F=false | G=true, C=false) = ', P_F_f_given_G_t_C_f)

    count_notg_c = 0
    countf = 0
    for line in lines:
        values = line.split()
        if values[1] == '0' and values[2] == '1':
            if values[3] == '1':
                countf += 1
            count_notg_c += 1

    P_F_t_given_G_f_C_t = countf / count_notg_c
    P_F_f_given_G_f_C_t = 1 - P_F_t_given_G_f_C_t
    print('P(F=true | G=false, C=true) = ', P_F_t_given_G_f_C_t)
    print('P(F=false | G=false, C=true) = ', P_F_f_given_G_f_C_t)

    count_notg_notc = 0
    countf = 0
    for line in lines:
        values = line.split()
        if values[1] == '0' and values[2] == '0':
            if values[3] == '1':
                countf += 1
            count_notg_notc += 1

    P_F_t_given_G_f_C_f = countf / count_notg_notc
    P_F_f_given_G_f_C_f = 1 - P_F_t_given_G_f_C_f
    print('P(F=true | G=false, C=false) = ', P_F_t_given_G_f_C_f)
    print('P(F=false | G=false, C=false) = ', P_F_f_given_G_f_C_f)

    args = sys.argv[2:]
    jpd = 0
    if len(args) == 4:
        # Convert the input arguments to corresponding boolean values
        B = True if args[0] == 'Bt' else False
        G = True if args[1] == 'Gt' else False
        C = True if args[2] == 'Ct' else False
        F = True if args[3] == 'Ft' else False

        # B=t, G=t, C=t, F=t
        if B is True and G is True and C is True and F is True:
            jpd = P_B_t * P_C_t * P_G_t_given_B_t * P_F_t_given_G_t_C_t

        # B=t, G=t, C=t, F=f
        elif B is True and G is True and C is True and F is False:
            jpd = P_B_t * P_C_t * P_G_t_given_B_f * P_F_f_given_G_t_C_t

        # B=t, G=t, C=f, F=t
        elif B is True and G is True and C is False and F is True:
            jpd = P_B_t * P_C_f * P_G_t_given_B_t * P_F_t_given_G_t_C_f

        # B=t, G=t, C=f, F=f
        elif B is True and G is True and C is False and F is False:
            jpd = P_B_t * P_C_f * P_G_t_given_B_t * P_F_f_given_G_t_C_f

        # B=t, G=f, C=t, F=t
        elif B is True and G is False and C is True and F is True:
            jpd = P_B_t * P_C_t * P_G_f_given_B_t * P_F_t_given_G_f_C_t

        # B=t, G=f, C=t, F=f
        elif B is True and G is False and C is True and F is False:
            jpd = P_B_t * P_C_t * P_G_f_given_B_t * P_F_f_given_G_f_C_t

        # B=t, G=f, C=f, F=t
        elif B is True and G is False and C is False and F is True:
            jpd = P_B_t * P_C_f * P_G_f_given_B_t * P_F_t_given_G_f_C_f

        # B=t, G=f, C=f, F=f
        elif B is True and G is False and C is False and F is False:
            jpd = P_B_t * P_C_f * P_G_f_given_B_t * P_F_f_given_G_f_C_f

        # B=f, G=t, C=t, F=t
        elif B is False and G is True and C is True and F is True:
            jpd = P_B_f * P_C_t * P_G_t_given_B_f * P_F_t_given_G_t_C_t

        # B=f, G=t, C=t, F=f
        elif B is False and G is True and C is True and F is False:
            jpd = P_B_f * P_C_t * P_G_t_given_B_f * P_F_f_given_G_t_C_t

        # B=f, G=t, C=f, F=t
        elif B is False and G is True and C is False and F is True:
            jpd = P_B_f * P_C_f * P_G_t_given_B_f * P_F_t_given_G_t_C_f

        # B=f, G=t, C=f, F=f
        elif B is False and G is True and C is False and F is False:
            jpd = P_B_f * P_C_f * P_G_t_given_B_f * P_F_f_given_G_t_C_f

        # B=f, G=f, C=t, F=t
        elif B is False and G is False and C is True and F is True:
            jpd = P_B_f * P_C_t * P_G_f_given_B_f * P_F_t_given_G_f_C_t

        # B=f, G=f, C=t, F=f
        elif B is False and G is False and C is True and F is False:
            jpd = P_B_f * P_C_t * P_G_f_given_B_f * P_F_f_given_G_f_C_t

        # B=f, G=f, C=f, F=t
        elif B is False and G is False and C is False and F is True:
            jpd = P_B_f * P_C_f * P_G_f_given_B_f * P_F_t_given_G_f_C_f

        # B=f, G=f, C=f, F=f
        elif B is False and G is False and C is False and F is False:
            jpd = P_B_f * P_C_f * P_G_f_given_B_f * P_F_f_given_G_f_C_f

        else:
            print('Incorrect number of arguments. Please provide Bt/Bf Gt/Gf Ct/Cf Ft/Ff.')
        print('JPD = ', jpd)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <training_data>")
    main()
