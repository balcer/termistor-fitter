from math import exp, log
import argparse as ap

tabs = 273.15

def adc2u(adc_val, u_ref, adc_res):
	return (u_ref / ((2**adc_res) - 1)) * adc_val

def adc2r(adc_val, u_ref, adc_res, rx):
	return ((u_ref * rx) / adc2u(adc_val, u_ref, adc_res)) - rx

def adc2t(adc_val, u_ref, adc_res, rx, beta, r25):
	return (1 / ((log(adc2r(adc_val, u_ref, adc_res, rx) / r25) / beta) + (1 / (tabs + 25))))

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
	args = parser.parse_args()

	f = open('adc2u.dat' ,'w+')
	f.write("#adc_val      u       r\n")
	for x in range(1, 2**args.adc_res):
		line = '%-10d %4f %12f\n' % (x, adc2u(x, args.u_ref, args.adc_res), adc2r(x, args.u_ref, args.adc_res, args.resistance))
		f.write(line)
	f.close()

if __name__ == "__main__":
	main()
