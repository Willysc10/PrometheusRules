# test_prometheusrules.py
"""
Tests for PrometheusRules module.
"""

import unittest
from prometheusrules import PrometheusRules

class TestPrometheusRules(unittest.TestCase):
    """Test cases for PrometheusRules class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrometheusRules()
        self.assertIsInstance(instance, PrometheusRules)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrometheusRules()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
