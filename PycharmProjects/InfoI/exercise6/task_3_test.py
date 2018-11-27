from unittest import TestCase

from  task_3 import transfer_from_to, create_account

"""transfer_from_to
    Input: dictionary with account names and balances, sender and receiver informaiton
    Output: updated dictionary
    Conditions for the function to work: existing account, sender has enough money
    Else: unmodified dictionary
   create_account:
    Input: dictionary with account names, balances, initial balance, and balance of new account
    Output: Updated dictionary
    Conditions for the function to work: No existing account, Name is not a empty string,
    non-negative inital balance
    Else: unmodified dictionary

    What has to be tested:
    - If conditions not met (not enough money, transferring negative amounts, inexisting account or
    inexisting accounts, empty names, negative balances) - return unmodified dictionary
    - If conditions are met - return modified dictionary
    """


class Task3Test(TestCase):
    """
    Task 3: Accounts
    """
    def test_nonempty_accoutns(accs):
        assert accs != {}

    def test_valid_accounts():
        for i in [account_from, account_to]:
            assert i != None

    def test_nonnegative_account(value):
        assert value >= 0

    def compare_dictionaries_transfer(self):
        if value < 0 or accs == {} or account_from == None or account_to == None:
        self.assertDictEqual(dict(self.accs) == self.accounts)


    def test_nonnegative_initial_balance(initial_balance):
        assert initial_balance >= 0

    def test_nonempty_name(name):
        assert name != None


    def test_create_account(self):
        if accs=={} or name == None or inital_balance <0:
            self.assertDictEqual(dict(self.accs) == self.accounts)








