from odoo.tests.common import TransactionCase
from odoo.addons.academic2.tests.common import Academic2Common

from odoo.exceptions import UserError
from odoo.tests import tagged

import logging
_logger = logging.getLogger(__name__)

@tagged('post_install', '-at_install')
class CourseTestCase(Academic2Common):

	def test_vit_course_count(cls):
		_logger.info(' -------------------- test record count -----------------------------------------')
		cls.assertEqual(
		    4,
		    len(cls.courses)
		)