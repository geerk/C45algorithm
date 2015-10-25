from collections import OrderedDict


def deldup(li):
    """ Deletes duplicates from list _li_
        and return new list with unique values.
    """
    return list(OrderedDict.fromkeys(li))


def is_mono(t):
    """ Returns True if all values of _t_ are equal
        and False otherwise.
    """
    for i in t:
        if i != t[0]:
            return False
    return True


def get_indexes(table, col, v):
    """ Returns indexes of values _v_ in column _col_
        of _table_.
    """
    li = []
    start = 0
    for row in table[col]:
        if row == v:
            index = table[col].index(row, start)
            li.append(index)
            start = index + 1
    return li


def get_values(t, col, indexes):
    """ Returns values of _indexes_ in column _col_
        of the table _t_.
    """
    return [t[col][i] for i in range(len(t[col])) if i in indexes]


def del_values(t, ind):
    """ Creates the new table with values of _ind_.
    """
    return {k: [v[i] for i in range(len(v)) if i in ind] for k, v in t.items()}


def print_list_tree(tree, tab=''):
    """ Prints list of nested lists in
        hierarchical form.
    """
    print('%s[' % tab)
    for node in tree:
        if isinstance(node, basestring):
            print('%s  %s' % (tab, node))
        else:
            print_list_tree(node, tab + '  ')
    print('%s]' % tab)


def formalize_rules(list_rules):
    """ Gives an list of rules where
        facts are separeted by coma.
        Returns string with rules in
        convinient form (such as
        'If' and 'Then' words, etc.).
    """
    text = ''
    for r in list_rules:
        t = [i for i in r.split(',') if i]
        text += 'If %s,\n' % t[0]
        for i in t[1:-1]:
            text += '   %s,\n' % i
        text += 'Then: %s.\n' % t[-1]
    return text


def get_subtables(t, col):
    """ Returns subtables of the table _t_
        divided by values of the column _col_.
    """
    return [del_values(t, get_indexes(t, col, v)) for v in deldup(t[col])]
