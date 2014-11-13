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

    def get_send_in_paper(self, name):
        return self.party.send_in_paper

    @classmethod
    def search_send_in_paper(cls, name, clause):
        return [('party.send_in_paper',) + tuple(clause[1:])]


class Party:
    __name__ = 'party.party'

    send_in_paper = fields.Boolean('Send in paper',
        help='Indicates wether the partner wants to receive the invoice in '
        'paper or not.')

    @classmethod
    def __setup__(cls):
        super(Party, cls).__setup__()
        cls._error_messages.update({
                'no_email_and_in_paper': ('Party "%(party)s" is not marked as '
                    'send in paper but has no email contact mechanism.'),
                })

    @staticmethod
    def default_send_in_paper():
        return True

    @classmethod
    def validate(cls, parties):
        super(Party, cls).validate(parties)
        for party in parties:
            party.check_send_in_paper()

    def check_send_in_paper(self):
        if self.send_in_paper:
            return
        if not any(c.type == 'email' for c in self.contact_mechanisms):
            self.raise_user_error('no_email_and_in_paper', {
                    'party': self.rec_name,
                    })
