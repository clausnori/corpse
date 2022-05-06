# coding:utf-8
import hashlib
import lib.common
from model import Model
from lib.common import pubkey_to_address
from database import AccountDB


def get_account():
    adb = AccountDB()
    return adb.find_one()
