import unittest
from trie import Trie
from tree import parse_topics_into_tree

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

class TreeParsingTest(unittest.TestCase):
    def test_parse_empty_string(self):
        for s in [" ","","      "]:
            result = parse_topics_into_tree("")
            self.assertIsNone(result)
    
    def test_parse_string_without_any_children(self):
        s = "Animals"
        result = parse_topics_into_tree(s)
        self.assertEqual(s,result.serialize())

    def test_parse_string_with_multiple_children(self):
        s = "Animals ( Reptiles Birds ( Eagles Pigeons Crows ) )"
        result = parse_topics_into_tree(s)
        self.assertEqual(s,result.serialize())
        s = "SSZSL ( SZSSjSSSj ( S ( SSjSSSS ( SSS ( j ( SSSSSjSS ) SSSjS SSSaSS ) ) ZSS Sj SSSjSSZSS Sjj ) SSSS ( jpSjSSS ( jSjSSZSSS ( Smj ) ) ) ) SSSSS ( SSSSSSpS ) SS )"
        
        result = parse_topics_into_tree(s)
        self.assertEqual(s,result.serialize())
    
    def test_parse_string_with_deeply_nested_children(self):
        s = "A ( B ( C ( D ) ) E F )"
        result = parse_topics_into_tree(s)
        self.assertEqual(s,result.serialize())
    

