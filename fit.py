from math import exp, log
import argparse as ap

adc_res = 10
u_ref = 3.3
rx = 8.03

def adc2u(adc_val, u_ref, adc_res):
    return (u_ref / ((2**adc_res) - 1)) * adc_val

def adc2r(adc_val, u_ref, adc_res, rx):
	return ((u_ref * rx) / adc2u(adc_val, u_ref, adc_res)) - rx

def main():

    f = open('adc2u.dat' ,'w+')
    f.write("#adc_val      u       r\n")
    for x in range(1, 2**adc_res):
        line = '%-10d %4f %12f\n' % (x, adc2u(x, u_ref, adc_res), adc2r(x, u_ref, adc_res, rx))
        f.write(line)
    f.close()

if __name__ == "__main__":
    main()