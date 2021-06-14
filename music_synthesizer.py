from pyo import *
import random
import numpy as np




class MyInstrument(EventInstrument):
    def __init__(self, **args):
        EventInstrument.__init__(self, **args)

        # self.freq is derived from the 'degree' argument.
        self.phase = Phasor([self.freq, self.freq * 1.003])

        # self.dur is derived from the 'beat' argument.
        self.duty = Expseg([(0, 0.05), (self.dur, 0.5)], exp=4).play()

        self.osc = Compare(self.phase, self.duty, mode="<", mul=1, add=-0.5)

        # EventInstrument created the amplitude envelope as self.env.
        self.filt = ButLP(self.osc, freq=5000, mul=self.env).out()


def create_music(beats_per_second,no_of_beats,beat_list = None):
	# We tell the Events object which instrument to use with the 'instr' argument.
	beat_freqs = []
	if beat_list == None:

		for i in range(no_of_beats*int(beats_per_second)):
			beat_freqs.append(random.randrange(5,21))
	else:
		beat_freqs = beat_list
	#print(beat_freqs)
	e = Events(
	    instr=MyInstrument,
	    degree=EventSeq(values =beat_freqs),
	    beat=1 / beats_per_second,
	    db=-12,
	    attack=0.001,
	    decay=0.05,
	    sustain=0.5,
	    release=0.005,
	)
	return e,beat_freqs


def encode_genome(beat_freqs):
	array =  np.array(beat_freqs) - 5
	#print(array)
	binary_converter = lambda x : bin(x)
	array = np.array([binary_converter(i)[2:].zfill(4) for i in array])
	encoded = ''.join(list(array))

	return encoded

def decode_genome(genome):
	beat_freqs = []
	for i in range(0,len(genome),4):
		gene = genome[i:i+4]
		#print(gene)
		value = int(gene,2)
		beat_freqs.append(value)

	return beat_freqs





if __name__=='__main__':
	s = Server(duplex = 0)
	s.setOutputDevice(7)
	s.boot()
	s.start()

	beats_per_second = float(input('how many beats per second?'))
	no_of_beats = int(input('how many beats?'))
	a ,beat_freqs= create_music(beats_per_second,no_of_beats)
	a.play()
	print('encoded genome: ',new_individual)

	s.gui(locals())
