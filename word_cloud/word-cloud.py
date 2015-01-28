"""
    Write a stand alone Python script that creates word clouds. To do this, you'll
    first need to build the data. Write code that takes a long string and builds
    its word cloud data in a dictionary, where the keys are the words and the values
    are the number of times the words occured. For example, if the input is:

    After beating the eggs, Dana read the next step

    The output should be

    {
        'after': 1,
        'beating': 1,
        'the': 2,
        'eggs': 1,
        'dana': 1,
        'next': 1,
        'step': 1
    }

    You may assume the input will only contain words and standard punctuation.
"""


class WordCloud(object):
    """ Make a word cloud. """

    def occurance_hash(self, input_str):
        """
            Return each unique word (case-insensitive) and its occurance count.
        """
        occ_hash = {}
        # Which characters should be removed?
        delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
        # Walk each word in the input_str.
        for word in input_str.split():
            # Clean the word of any not alphanum chars
            clean_word = word.translate(None, delchars)
            try:
                occ_hash[clean_word.lower()] += 1
            except KeyError:
                occ_hash[clean_word.lower()] = 1

        return occ_hash


if __name__ == '__main__':
    # Run the tests if this is called from the command line.
    wcld = WordCloud()
    ret = wcld.occurance_hash(
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi'
        'tincidunt arcu eget lacus blandit efficitur'
    )
    print ret
    ret = wcld.occurance_hash(
        'The quick brown fox jumped over the lazy dog.'
    )
    print ret
    ret = wcld.occurance_hash(
        'After beating the eggs, Dana read the next step'
    )
    print ret
