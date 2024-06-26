"""Tests for specparam.core.reports."""

import os

from specparam.tests.settings import TEST_REPORTS_PATH

from specparam.core.reports import *

###################################################################################################
###################################################################################################

def test_save_model_report(tfm, skip_if_no_mpl):

    file_name = 'test_report'

    save_model_report(tfm, file_name, TEST_REPORTS_PATH)

    assert os.path.exists(os.path.join(TEST_REPORTS_PATH, file_name + '.pdf'))

def test_save_group_report(tfg, skip_if_no_mpl):

    file_name = 'test_group_report'

    save_group_report(tfg, file_name, TEST_REPORTS_PATH)

    assert os.path.exists(os.path.join(TEST_REPORTS_PATH, file_name + '.pdf'))
