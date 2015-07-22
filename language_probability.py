from math import log

def calculate_probabilites(file):
	f = open(file)
	count = {}
	p_log = {}
	total = 0
	for l in f:
		k = l[1:4]
		v = int(l[5:])
		count[k] = v
		total += v

	total = float(total)

	for k in count:
		p = count[k] / total
		p_log[k] = log(p)

	return p_log

def calculate_probability(sentence, log_p):
	total = 0.0
	return sum( log_p.get(w, 0.0) for w in [sentence[i:i+3] for i in xrange(len(sentence) - 2)])

def language(sentence, trimmers_probabilities):
	language_probability = []
	for p in trimmers_probabilities:
		prob = calculate_probability(sentence, p[1])
		#print prob, sentence, p[0]
		language_probability.append((p[0], prob))

	language_probability = sorted(language_probability, key=lambda lp: lp[1])
	return language_probability[-1][0]


en_log_p = calculate_probabilites("en.counts.txt")
pt_log_p = calculate_probabilites("pt.counts.txt")

languages_log_p = [("portugues", pt_log_p), ("ingles", en_log_p)]

sentences = ["marrom bombom, marror e nossa cor, nossa cor marrom", "it is hot", "meu deus, sono", "quero cagar", "python is cool", "bayes is simple and cool", "jesus, cade meu pao?", "pasta, nuggets and coke it is all I need to be happy", "hi, how are you?", "oi nega", "tudo bem?", "pega no meu bilau e balanca", "i love you", "te amo", "penis", "meu bilau"]

#sentences = ["python is cool and awesome. I want to use it all day long"]

for s in sentences:
	print s, " - ", language(s, languages_log_p)
