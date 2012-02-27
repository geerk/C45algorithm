import math
import utils


def freq(table, col, v):
    """ Returns counts of variant _v_
        in column _col_ of table _table_.
    """
    return table[col].count(v)


def info(table, res_col):
    """ Calculates the entropy of the table _table_
        where result column = _res_col_.
    """
    s = 0 # sum
    for v in utils.deldup(table[result_col]):
        p = freq(table, result_col, v) / float(len(table[result_col]))
        s += p * math.log(p, 2)
    return -s


def infox(table, col, res_col):
    """ Calculates the entropy of the table _table_
        after dividing it on the subtables by column _col_.
    """
    s = 0 # sum
    for subt in utils.get_subtables(table, col):
        s += (float(len(subt[col])) / len(table[col])) * info(subt, result)
    return s
    


def gain(table, x, res_col):
    """ The criterion for selecting attributes for splitting.
    """
    return info(table, result) - infox(table, x, result)
