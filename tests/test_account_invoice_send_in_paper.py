# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import POOL, DB_NAME, USER, CONTEXT
from trytond.transaction import Transaction
from trytond.exceptions import UserError


class TestCase(ModuleTestCase):
    'Test module'
    module = 'account_invoice_send_in_paper'

    def setUp(self):
        super(TestCase, self).setUp()
        self.party = POOL.get('party.party')

    def test0010send_in_paper(self):
        'Test send in papaer'
        with Transaction().start(DB_NAME, USER, context=CONTEXT):
            self.party.create([{'name': 'Send in paper'}])
            self.party.create([{
                        'name': 'Explicit send in paper',
                        'send_in_paper': True,
                        }])
            with self.assertRaises(UserError) as cm:
                self.party.create([{
                            'name': 'Not send in paper',
                            'send_in_paper': False,
                            }])
            self.assertEqual(cm.exception.message, (u'Party "Not send in '
                    'paper" is not marked as send in paper but has no email '
                    'contact mechanism.'))
            self.party.create([{
                        'name': 'Not send in paper',
                        'send_in_paper': False,
                        'contact_mechanisms': [('create', [{
                                        'type': 'email',
                                        'value': 'email@example.com',
                                        }])],
                        }])


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCase))
    return suite
