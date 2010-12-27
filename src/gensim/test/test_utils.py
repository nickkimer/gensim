#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU LGPL v2.1 - http://www.gnu.org/licenses/lgpl.html

"""
Automated tests for checking various utils functions
"""


import logging
import unittest

from gensim import utils


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
        level=logging.WARNING)


class TestIsCorpus(unittest.TestCase):

    def test_None(self):
        # test None
        print utils.isCorpus(None)
        result = utils.isCorpus(None)
        expected = (False, None)
        self.assertEqual(expected, result)

    def test_simple_lists_of_tuples(self):
        # test list words

        # one document, one word
        potentialCorpus = [[(0, 4.)]]
        result = utils.isCorpus(potentialCorpus)
        expected = (True, potentialCorpus)
        self.assertEqual(expected, result)

        # one document, several words
        potentialCorpus = [[(0, 4.), (1, 2.)]]
        result = utils.isCorpus(potentialCorpus)
        expected = (True, potentialCorpus)
        self.assertEqual(expected, result)

        potentialCorpus = [[(0, 4.), (1, 2.), (2, 5.), (3, 8.)]]
        result = utils.isCorpus(potentialCorpus)
        expected = (True, potentialCorpus)
        self.assertEqual(expected, result)

        # several documents, one word
        potentialCorpus = [[(0, 4.)], [(1, 2.)]]
        result = utils.isCorpus(potentialCorpus)
        expected = (True, potentialCorpus)
        self.assertEqual(expected, result)

        potentialCorpus = [[(0, 4.)], [(1, 2.)], [(2, 5.)], [(3, 8.)]]
        result = utils.isCorpus(potentialCorpus)
        expected = (True, potentialCorpus)
        self.assertEqual(expected, result)

    def test_int_tuples(self):
        potentialCorpus = [[(0, 4)]]
        result = utils.isCorpus(potentialCorpus)
        expected = (True, potentialCorpus)
        self.assertEqual(expected, result)

    def test_invalid_formats(self):
        # test invalid formats
        # these are no corpus, because they do not consists of 2-tuples with
        # the form(int, float).
        potentials = list()
        potentials.append(["human"])
        potentials.append("human")
        potentials.append(["human", "star"])
        potentials.append([1, 2, 3, 4, 5, 5])
        potentials.append([[(0, 'string')]])
        for noCorpus in potentials:
            result = utils.isCorpus(noCorpus)
            expected = (False, noCorpus)
            self.assertEqual(expected, result)


if __name__ == '__main__':
    logging.root.setLevel(logging.WARNING)
    unittest.main()
