import CSP_4_04_Stupid_Password_generator as HW
def stupid_password(n,l):
    password=[]
    letters="abcdefghijklmnopqrstuvwxyz"
    for d1 in range(1, n+1):
        for d2 in range(1, n+1):
            for d3 in letters[:l]:
                for d4 in letters[:l]:
                    for d5 in range(1,n+1):
                        if d5>d1 and d5>d2:
                            password.append(str(d1)+str(d2)+d3+d4+str(d5))
    return password
print (stupid_password(2,2))



