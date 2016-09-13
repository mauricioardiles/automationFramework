import unittest
from ejemploUTlibro import SearchTests
from ejemploUTlibroPruebaReporte import SearchTestsReporte

no_reporte = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
si_reporte = unittest.TestLoader().loadTestsFromTestCase(SearchTestsReporte)

smoke_tests = unittest.TestSuite([no_reporte, si_reporte])

unittest.TextTestRunner(verbosity=2).run(smoke_tests)