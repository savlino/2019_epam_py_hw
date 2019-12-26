"""
creates decorator for class that counts instances
and allows to return and reset this value
"""


def instances_counter(cls):
    """Some code"""
    setattr(cls, 'ins_cnt', 0)

    def __init__(self):
        cls.ins_cnt += 1
        cls.__init__

    def get_created_instances(self=None):
        return cls.ins_cnt

    def reset_instances_counter(self=None):
        return cls.ins_cnt
        cls.ins_cnt = 0

    setattr(cls, '__init__', __init__)
    setattr(cls, 'get_created_instances', get_created_instances)
    setattr(cls, 'reset_instances_counter', reset_instances_counter)
    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':
    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
