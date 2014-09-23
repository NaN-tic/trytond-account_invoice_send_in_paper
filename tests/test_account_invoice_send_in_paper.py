# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends, install_module


class TestCase(unittest.TestCase):
    'Test module'

    def setUp(self):
        install_module('account_invoice_send_in_paper')

    def test0005views(self):
        'Test views'
        test_view('account_invoice_send_in_paper')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCase))
    return suite