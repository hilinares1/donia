import string

from odoo import api, fields, models, exceptions
import datetime
import logging
import os
import shutil, urllib3
import zipfile
import base64

_logger = logging.getLogger(__name__)


class LoadExcelFile(models.TransientModel):
    _name = 'wizard.load_file'


