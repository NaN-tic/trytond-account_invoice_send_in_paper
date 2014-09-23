# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Invoice', 'Party']
__metaclass__ = PoolMeta


class Invoice:
    __name__ = 'account.invoice'

    send_in_paper = fields.Function(fields.Boolean('Send in paper'),
        'get_send_in_paper', searcher='search_send_in_paper')


class Party:
    __name__ = 'party.party'

    send_in_paper = fields.Boolean('Send in paper',
        help='Indicates wether the partner wants to receive the invoice in '
        'paper or not.')
