import sys

def main():
    # Define the probabilities
    P_B_t = 0.3041095890410959
    P_B_f = 0.6958904109589041
    P_C_t = 0.16986301369863013
    P_C_f = 0.8301369863013699
    P_G_t_given_B_t = 0.9279279279279279
    P_G_f_given_B_t = 0.07207207207207211
    P_G_t_given_B_f = 0.11811023622047243
    P_G_f_given_B_f = 0.8818897637795275
    P_F_t_given_G_t_C_t = 0.041666666666666664
    P_F_f_given_G_t_C_t = 0.9583333333333334
    P_F_t_given_G_t_C_f = 0.7064220183486238
    P_F_f_given_G_t_C_f = 0.29357798165137616
    P_F_t_given_G_f_C_t = 0.3157894736842105
    P_F_f_given_G_f_C_t = 0.6842105263157895
    P_F_t_given_G_f_C_f = 0.9587628865979382
    P_F_f_given_G_f_C_f = 0.04123711340206182


    # To calculate other probabilities, change the values of the variables.
    # Define the evidence variables
    B = True
    C = False

    # Define the query variable
    F = True

    # Define the prior probability of F
    P_F = 0

    # Enumerate over all possible values of G
    for G in [True, False]:
        # Calculate the conditional probability of G given B
        if B:
            P_G_given_B = P_G_t_given_B_t if G else P_G_f_given_B_t
        else:
            P_G_given_B = P_G_t_given_B_f if G else P_G_f_given_B_f

        # Calculate the conditional probability of F given G and C
        if G:
            if C:
                P_F_given_G_C = P_F_t_given_G_t_C_t if F else P_F_f_given_G_t_C_t
            else:
                P_F_given_G_C = P_F_t_given_G_t_C_f if F else P_F_f_given_G_t_C_f
        else:
            if C:
                P_F_given_G_C = P_F_t_given_G_f_C_t if F else P_F_f_given_G_f_C_t
            else:
                P_F_given_G_C = P_F_t_given_G_f_C_f if F else P_F_f_given_G_f_C_f

        # Calculate the joint probability of B, C, G, and F
        P = P_B_t if B else P_B_f
        P *= P_C_t if C else P_C_f
        P *= P_G_given_B
        P *= P_F_given_G_C

        # Update the prior probability of F
        P_F += P

    # Normalize the posterior probability of F
    P_F /= (P_F + (1 - P_F))

    print("The probability of F being true given B=true and C=false is:", P_F)


if __name__ == '__main__':
    main()