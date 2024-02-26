"""Use NLP (nltk) to make dispersion plot."""
import matplotlib.pyplot as plt
from nltk.draw.dispersion import dispersion_plot
    
def text_to_string(filename):
    """Read a text file and return a string."""
    with open(filename) as infile:
        return infile.read()

corpus = text_to_string('hound.txt')
tokens = nltk.word_tokenize(corpus)
tokens = nltk.Text(tokens)  # NLTK wrapper for automatic text analysis.
words = ['Holmes', 'Watson', 'Mortimer', 'Henry', 'Barrymore', 'Stapleton', 'Selden', 'hound']
ax = dispersion_plot(tokens, words)
# Correct current bug in NLTK dispersion_plot that reverses label order by mistake:
ax.set_yticks(list(range(len(words))), reversed(words), color="C0")
