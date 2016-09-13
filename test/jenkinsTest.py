import unittest
from xmlrunner import xmlrunner
from ejemploUTlibro import SearchTests
from ejemploUTlibroPruebaReporte import SearchTestsReporte


no_reporte = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
si_reporte = unittest.TestLoader().loadTestsFromTestCase(SearchTestsReporte)
smoke_tests = unittest.TestSuite([no_reporte, si_reporte])
# run the suite
xmlrunner.XMLTestRunner(verbosity=2, output='test-reports').run(smoke_tests)