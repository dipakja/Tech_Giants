import unittest
from main import get_cpu_power_usage, get_memory_power_usage, get_nic_power_usage, get_tdp

class TestTelemetryFunctions(unittest.TestCase):

    def test_get_cpu_power_usage(self):
        cpu_usage = get_cpu_power_usage()
        self.assertTrue(isinstance(cpu_usage, float))

    def test_get_memory_power_usage(self):
        memory_usage = get_memory_power_usage()
        self.assertTrue(isinstance(memory_usage, float))

    def test_get_nic_power_usage(self):
        nic_usage = get_nic_power_usage()
        self.assertTrue(isinstance(nic_usage, int))

    def test_get_tdp(self):
        tdp = get_tdp()
        self.assertTrue(tdp is None or isinstance(tdp, float))

if __name__ == '__main__':
    unittest.main()
