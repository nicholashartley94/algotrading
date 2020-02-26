#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
# Copyright (C) 2020 Daniel Rodriguez
# Use of this source code is governed by the MIT License
###############################################################################
__all__ = [
    'SEED_AVG', 'SEED_LAST', 'SEED_SUM',
    '_INCPERIOD', '_DECPERIOD', '_MINIDX',
    '_SERIES',
]


SEED_AVG = 0
SEED_LAST = 1
SEED_SUM = 2


def _INCPERIOD(x, p=1):
    '''
    Forces an increase `p` in the minperiod of object `x`.

    Example: `ta-lib` calculates `+DM` a period of 1 too early, but calculates
    the depending `+DI` from the right starting point. Increasing the period,
    without changing the underlying already calculated `+DM` values, allows the
    `+DI` values to be right
    '''
    x._minperiod += p


def _DECPERIOD(x, p=1):
    '''
    Forces an increase `p` in the minperiod of object `x`.

    Example: `ta-lib` calculates `obv` already when the period is `1`,
    discarding the needed "close" to "previous close" comparison. The only way
    to take this into account is to decrease the delivery period of the
    comparison by 1 to start the calculation before (and using a fixed
    criterion as to what to do in the absence of a valid close to close
    comparison)
    '''
    x._minperiod -= p


def _MINIDX(x, p=0):
    '''
    Delivers the index to an array which corresponds to `_minperiod` offset by
    `p`. This allow direct manipulation of single values in arrays like in the
    `obv` scenario in which a seed value is needed for the 1st delivered value
    (in `ta-lib` mode) because no `close` to `previous close` comparison is
    possible.
    '''
    return x._minperiod - 1 + p


def _SERIES(x):
    '''Macro like function which makes clear that one is retrieving the actual
    underlying series and not something a wrapped version'''
    return x._series.rename(x._name, inplace=True)
