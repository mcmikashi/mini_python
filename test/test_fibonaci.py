import unittest

import sys

from pathlib import Path
# insert at 1, 0 is the script path (or '' in REPL)
test_path = Path("module").absolute()

sys.path.append(str(test_path))

print(sys.path)

from fibonaci import fibonacci

class fibonacciTest(unittest.TestCase):
    
    def test_zeros_un_deux(self):
        self.assertEqual(fibonacci(0),0)
        self.assertEqual(fibonacci(1),1)
        self.assertEqual(fibonacci(2),1)
        
    def test_basic(self):
        self.assertEqual(fibonacci(4),3)
        self.assertEqual(fibonacci(8),21)
        self.assertEqual(fibonacci(11),89)
        self.assertEqual(fibonacci(16),987)
        self.assertEqual(fibonacci(40),102334155)
        self.assertEqual(fibonacci(64),10610209857723 )
        self.assertEqual(fibonacci(94),19740274219868223167 )
        self.assertEqual(fibonacci(200),280571172992510140037611932413038677189525 )

if __name__ == '__main__':
    unittest.main()    
