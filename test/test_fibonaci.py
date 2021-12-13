import unittest

import sys

from pathlib import Path
# insert at 1, 0 is the script path (or '' in REPL)
test_path = Path("module").absolute()

print(test_path)

sys.path.append(str(test_path))

print(sys.path)

from fibonaci import fibonaci

class FibonaciTest(unittest.TestCase):
    
    def test_zeros_un_deux(self):
        self.assertEqual(fibonaci(0),0)
        self.assertEqual(fibonaci(1),1)
        self.assertEqual(fibonaci(2),1)
        
    def test_basic(self):
        self.assertEqual(fibonaci(4),3)
        self.assertEqual(fibonaci(8),21)
        self.assertEqual(fibonaci(11),89)
        self.assertEqual(fibonaci(16),987)
        self.assertEqual(fibonaci(40),102334155)
        self.assertEqual(fibonaci(64),10610209857723 )
        self.assertEqual(fibonaci(94),19740274219868223167 )
        self.assertEqual(fibonaci(200),280571172992510140037611932413038677189525 )
if __name__ == '__main__':
    unittest.main()    
