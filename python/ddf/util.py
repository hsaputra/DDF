from __future__ import unicode_literals
import numpy as np
import json


"""
Mapping from DDF types to python types
"""
TYPE_MAPPING = {'integer': int,
                'int': int,
                'tinyint': int,
                'smallint': int,
                'bigint': long,
                'long': long,
                'double': float,
                'float': float,
                # TODO: Find a way to handle decimal better.
                'decimal': float,
                'boolean': bool,
                'logical': bool,
                'string': unicode,
                'array': list,
                'struct': object,
                'timestamp': int,
                'blob': object
                }


def to_bool(x):
    """
    Try our best to make x into a boolean value
    :param x: the value to be converted
    :return: a boolean value
    """
    if x is None:
        return None
    if isinstance(x, (bool, np.bool_)):
        return x
    if isinstance(x, (str, unicode)):
        return x.lower() in ['yes', 'true']
    if isinstance(x, (int, long)):
        return x != 0
    if isinstance(x, (float, np.float)):
        return abs(x) > 1e-10
    raise ValueError('Could not convert into bool with value {} of type {}'.format(x, type(x)))


def to_python_type(t):
    tmp = t.split(".")
    t = tmp[len(tmp) - 1]
    return 'str' if t not in TYPE_MAPPING else TYPE_MAPPING[t]


def convert_column_types(df, column_types, raise_on_error=False):
    """
    Convert a dataframe into data types specified in column_types
    :param df: a data frame containing the sampled data
    :type df: pd.DataFrame
    :param column_types: the types of columns, in pE terminology
    :param raise_on_error:
    :return: a correctly typed data frame
    """
    if len(df.columns) != len(column_types):
        raise ValueError('Expect a list of column types of the same length with the number of columns in df')

    for i, c in enumerate(df.columns):
        dest_type = to_python_type(column_types[i])
        if dest_type is bool:
            df[c] = df[c].apply(to_bool)
        elif dest_type is list or column_types[i] == 'struct':
            # json
            df[c] = df[c].apply(lambda x: json.loads(x) if isinstance(x, (str, unicode)) else x)
        elif dest_type is float:
            # NaN is encoded as "null"
            df[c] = df[c].convert_objects(convert_numeric=True)

        # convert type
        df[c] = df[c].astype(dest_type, raise_on_error=raise_on_error)
    return df
