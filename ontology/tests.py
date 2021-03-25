import unittest
from trie import Trie

class TrieTest(unittest.TestCase):
    def test_count_words_starting_with_when_similar_words_are_inserted(self):
        t = Trie()
        t.insert("dogs")
        t.insert("dog")
        result = t.count_words_starting_with("dog")
        self.assertEqual(2,result)
        result = t.count_words_starting_with("dogs")
        self.assertEqual(1,result)

    def test_count_words_when_same_word_is_inserted_multiple_times(self):
        t = Trie()
        t.insert("dog")
        t.insert("dog")
        result = t.count_words_starting_with("dog")
        self.assertEqual(1,result)
        
    def test_count_words_when_no_word_is_in_trie(self):
        t = Trie()
        self.assertEqual(0,t.count_words_starting_with(""))
        self.assertEqual(0,t.count_words_starting_with("123"))
    
    def test_trie_is_case_insensitive(self):
        t = Trie()
        t.insert("DOG")
        self.assertTrue(t.contains("doG"))
        self.assertEqual(1,t.count_words_starting_with("dO"))
    
    
