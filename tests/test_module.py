
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.exceptions import UserError
from trytond.modules.company.tests import CompanyTestMixin


class AccountInvoiceSendInPaperTestCase(CompanyTestMixin, ModuleTestCase):
    'Test AccountInvoiceSendInPaper module'
    module = 'account_invoice_send_in_paper'

    @with_transaction()
    def test0010send_in_paper(self):
        'Test send in papaer'
        pool = Pool()
        Party = pool.get('party.party')
        Party.create([{'name': 'Send in paper'}])
        Party.create([{
                    'name': 'Explicit send in paper',
                    'send_in_paper': True,
                    }])
        with self.assertRaises(UserError) as cm:
            Party.create([{
                        'name': 'Not send in paper',
                        'send_in_paper': False,
                        }])
        self.assertEqual(cm.exception.message, ('Party "Not send in '
                'paper" is not marked as send in paper but has no email '
                'contact mechanism.'))
        Party.create([{
                    'name': 'Not send in paper',
                    'send_in_paper': False,
                    'contact_mechanisms': [('create', [{
                                    'type': 'email',
                                    'value': 'email@example.com',
                                    }])],
                    }])


del ModuleTestCase
