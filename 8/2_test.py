import part_2
import unittest


class TestDay8Part2(unittest.TestCase):
      def test_score_of_highest_field(self):
        score_of_highest_field = part_2.score_of_highest_field('fixture.txt')
        self.assertEqual(score_of_highest_field, 8)
        print(part_2.score_of_highest_field('input.txt'))
