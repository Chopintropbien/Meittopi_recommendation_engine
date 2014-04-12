__author__ = 'andrei'


class Inst_Init_Exception(Exception):
    pass


class DB_Push_Exception(Exception):
    pass


class UID_overload_Exception(Exception):
    pass


def get_node_ID(Node):
    return str(Node).split('/')[-1][:-1]