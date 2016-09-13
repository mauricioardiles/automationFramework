import unittest
from utils import HTMLTestRunner
import os
from ejemploUTlibro import SearchTests
from ejemploUTlibroPruebaReporte import SearchTestsReporte

dir1 = os.getcwd()

no_reporte = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
si_reporte = unittest.TestLoader().loadTestsFromTestCase(SearchTestsReporte)

smoke_tests = unittest.TestSuite([no_reporte, si_reporte])

outfile = open(dir1 + "\\testReport.html", "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description= 'testing an example')

runner.run(smoke_tests)