from music_synthesizer import create_music,encode_genome,decode_genome
from pyo import *
from genetic import selection,crossover
import pandas as pd


if __name__ == '__main__':

	#lets initiate a server for sound generation
	s = Server(duplex = 0)
	s.setOutputDevice(7)
	s.boot()
	s.start()
	print('')
	print('')
	print('')
	print('')
	print('')
	# lets generate a population of individuals
	beats_per_second = float(input('how many beats per second?'))
	no_of_beats = int(input('how many beats?'))
	individuals_ini = int(input('how many individuals in intial population?'))
	print('')

	#setting algo parameters
	min_Np = 200/individuals_ini#to ensure atleast two indivuals selected for next generation
	Np = float(input('enter Np value, should be greater than or equal to  {:.2f} :'.format(min_Np)))
	number_of_generations = int(input('no of successive generations to run for? '))
	#lets play out each indvidual and see its encoded genome
	running = True
	individual=1
	population = {}
	while running:
	
		print('individual:',individual)
		a ,beat_freqs= create_music(beats_per_second,no_of_beats)
		population[individual] = [None,encode_genome(beat_freqs)]
		print('encoded_genome:',encode_genome(beat_freqs))
		a.play()
		s.gui(exit=False)
		a.stop()
		population[individual][0] =int(input('Rating ? = '))
		if individual == individuals_ini:
			running = False
		individual+=1
		print('')

	for generation in range(number_of_generations):

		print('Generation: ',generation+1)
		mating_pool = selection(population,Np)
		new_generation = crossover(mating_pool)
		for new_individual in new_generation:
			print('Individual:',individual)
			beat_list = decode_genome(new_individual)
			a,beat_freqs = create_music(beats_per_second,no_of_beats,beat_list)
			population[individual] = [None,new_individual]
			print('encoded_genome:',new_individual)
			a.play()
			s.gui(exit=False)
			a.stop()
			population[individual][0] =int(input('Rating ? = '))
			print('')
			individual+=1

	print('Final Population')
	df  = pd.DataFrame(population,index = ['Rating','Genome'])
	df = df.transpose()
	df.index.name = 'Individual'
	print(df)



