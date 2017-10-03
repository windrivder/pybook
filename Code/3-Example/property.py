from decimal import Decimal


class Fees(object):

    def __init__(self):
        """Constructor"""
        self._fee = None

    def get_fee(self):
        """
        Return the current fee
        """
        return self._fee

    def set_fee(self, value):
        """
        Set the fee
        """
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value

    fee = property(get_fee, set_fee)


class NewFees(object):

    def __init__(self, fee):
        """Constructor"""
        self._fee = fee

    @property
    def fee(self):
        """
        The fee property - the getter
        """
        return self._fee

    @fee.setter
    def fee(self, value):
        """
        The setter of the fee property
        """
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value


if __name__ == '__main__':
    f = NewFees('1')
    print(f.fee)
    f.fee = '2'
    print(f.fee)
