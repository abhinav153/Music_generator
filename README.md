# Music_generator
Music generator using genetic algorithms

In this project i used genetic algorithms to create patterns on music. My projectly is mainly inspired by one of the [video](https://www.youtube.com/watch?v=aOsET8KapQQ&t=337s) on youtube on the same topic with slight modifications.

## Genetic algorithm(SSA Simple Genetic Algorithm)
In computer science and operations research, a genetic algorithm (GA) is a metaheuristic inspired by the process of natural selection that belongs to the larger class of evolutionary algorithms (EA). Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problems by relying on biologically inspired operators such as mutation, crossover and selection.

### Project structure
genetic.py - contains code for  genetic operations of crossover and selection<br>
main.py - main file to be executed for genetation of musical patterns<br>
music_synthesizer.py - contains code for actual creation of music using pyo library<br>

## Use
> Execute the line python main.py <br>

This will start the script<br>
Script will ask for three parameters<br>
Notes/Beat per second<br>
No of individuals in intial population<br>
Np - percentage of individuals to take for creating a mating pool to create a successive generation<br>
No of successive generations the script should produce<br>

## Explanation

### Initializaton
A genetic algorithms initially creates a new population , the population consits of individuals or solutions to the problem, here my solutions are binary coded solutions , each individual has a mapping to their binary string which represents a solution. The binary string is of the length (beats per second * no of notes),this binary string can divided into groups of 4 bits,this 4 groups 4 beats when converted to base 10 system represents values which are then used to generate some basic musical patters using pyo methods. When generating the individual population this values are genrated at random hence some random musical patterns will be developed. You will be asked to rate this muscial patterns out of a scale of 0-5. After you are done rating this musical patterns, the script will move on to genrating a new succesive generation

### Succesive generations
**Seletion**
Based on the Np parameters given initially, top Np % of individuals will be taken as individuals for generating the next generation. Out of these selection individuals pairs of two will be made to create parent grousp which will in whole comprise  a mating pool.<br>
**Crossover**
Now for all pairs within a mating pool, their genomes will be taken and divided into gene segents of length 4 bits. For each of these gene segments of length 4 bits , a random number between 0 and 3 would be generated, based on the number generatedm the 4 bits of a particular gene segmented would be split into two halves based on kth position and the resulting halves will be exchanged
For eg. consider <br>
parent_1 with genome 11110101 <br>
parent_2 with genome 00001111 <br>
Their gene segments would be 1111 | 0101 and 0000 | 1111 respectively <br>
for the 1st gene segment 1111 for parent_1 and 0000 for parent_2 , say k=2 is generated <br>
1111 will be split into  11 | 11 and 0000 will be split into 00 | 00 <br>
these split halves will be exchanged to create a new gene segment for two different offspring <br>
1100 & 0011 <br>
Same procedure will be repeated for all gene segments , and will be manually rated. The procedure will go on for sprecified number of succesive generations to be generated and hopefull at the end some pleasing musical patterns will be created


### Reference
Please look at these series of [videos](https://www.youtube.com/watch?v=Fs5ZIjp1hUk&t=460s) if you want to learn more about genetic algorithms

