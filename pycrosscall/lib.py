# -*- coding: utf-8 -*-


import random


def get_randhashstr(dig):

	return (('%0' + str(dig) + 'x') % random.randrange(16**dig))


def generate_session_id():

	return get_randhashstr(8)
