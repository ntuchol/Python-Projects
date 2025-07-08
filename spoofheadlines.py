import random

# Example words for rule-based generation
nouns = ["cats", "politicians", "celebrities", "zombies"]
adjectives = ["outrageous", "hilarious", "baffling", "shocking"]
verbs = ["demand", "boycott", "invent", "discover"]

# Rule-based headline template
headline_template = "Breaking News: [adjective] [nouns] [verbs] [something surprising]"

# Generate a random headline
adjective = random.choice(adjectives)
noun = random.choice(nouns)
verb = random.choice(verbs)
surprising_event = "the secret to eternal youth"  # You can replace this with random phrases or use Markov chains for more complexity

spoof_headline = headline_template.replace("[adjective]", adjective)
spoof_headline = spoof_headline.replace("[nouns]", noun)
spoof_headline = spoof_headline.replace("[verbs]", verb)
spoof_headline = spoof_headline.replace("[something surprising]", surprising_event)

print(spoof_headline)
