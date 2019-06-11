class Group(object):

    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def __str__(self):
      return str(self.users)

    __repr__ = __str__





def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against

    """

    print ('True') if user in group.get_users() else print ('False')


# Create Groups. Name of group self.name
parent_group = Group("parent")
child_group = Group("child")
sub_child_group = Group("subchild")

# Adding Group
parent_group.add_group(child_group)
child_group.add_group(sub_child_group)


# Add User
sub_child_user = "sub_child_user"
sub_child_group.add_user(sub_child_user)


# True
is_user_in_group(sub_child_user, sub_child_group)

# False
is_user_in_group(sub_child_user, parent_group)
is_user_in_group(sub_child_user, child_group)


print("________________________")

# Test Case 2
# Add User
# true
sub_child_user = "sub_child_user"
sub_child_group.add_user(sub_child_user)
is_user_in_group(sub_child_user, sub_child_group)

# Test Case 2
# Add User
# true
sub_child_user_two = "sub_child_user"
sub_child_group.add_user(sub_child_user_two)
is_user_in_group(sub_child_user, sub_child_group)

# Test Case 3
# Add User
# True
sub_child_user_three = "sub_child_user"
child_group.add_user(sub_child_user_three)
is_user_in_group(sub_child_user, child_group)
