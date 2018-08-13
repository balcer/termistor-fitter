from math import log
import argparse as ap

TABS = 273.15

def adc2t(adc_val, u_ref, adc_res, rx, beta, r25):
    u = (u_ref / ((2**adc_res) - 1)) * adc_val
    r = ((u_ref * rx) / u) - rx
    t = (1 / ((log(r / r25) / beta) + (1 / (TABS + 25)))) -TABS
    return u, r, t

def main():

	parser = ap.ArgumentParser()

	parser.add_argument("-a",
		"--adc_res",
		type = int,
		help = "ADC resolution (default 10 bits)",
		default = 10)

	parser.add_argument("-r",
		"--u_ref",
		type = float,
		help = "ADC reference voltage (default 3.3V)",
		default = 3.3)

	parser.add_argument("-rx",
		"--resistance",
		type = float,
		help = "resistance of resistor in series with termistor in Ohms (default 10k)",
		default = 10000)

	parser.add_argument("-b",
		"--beta",
		type = float,
		help = "thermistor beta coefficient in Kelwins (default 3900)",
		default = 3900)

	parser.add_argument("-r25",
		"--resistance_in_25C",
		type = float,
		help = "thermistor resistance in 25C in Ohms (default 10000)",
		default = 10000)

	args = parser.parse_args()

    f = open('data.dat', 'w+')
    f.write("#adc_val     u[V]      r[Ohms]           t[C]\n")
    for x in range(1, (2**args.adc_res) - 1):

        u, r , t = adc2te(x, args.u_ref, args.adc_res, args.resistance, args.beta, args.resistance_in_25C)

        line = '%-10d %10f %14f %14f\n' % (x, u, r, t)
        f.write(line)
    f.close()

if __name__ == "__main__":
	main()
