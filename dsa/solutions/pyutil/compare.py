'''
Collection of comparator functions & their respective assertion functions
'''

from collections import Counter
from typing import Iterable, Sequence, Any, Callable


# Core sequence and set comparisons
def same_sequence(a: Sequence[Any], b: Sequence[Any]) -> bool:
    """
    Return True if sequences are element-wise equal in order.
    """
    return list(a) == list(b)


def assert_same_sequence(a: Sequence[Any], b: Sequence[Any]) -> None:
    if list(a) != list(b):
        raise AssertionError(
            f"Sequences differ:\n"
            f"Expected: {b}\n"
            f"Actual:   {a}"
        )


def same_set(a: Iterable[Any], b: Iterable[Any]) -> bool:
    """
    Return True if a and b contain the same unique elements, ignoring multiplicity.
    """
    return set(a) == set(b)


def assert_same_set(a: Iterable[Any], b: Iterable[Any]) -> None:
    sa, sb = set(a), set(b)
    if sa != sb:
        raise AssertionError(
            f"Sets differ:\n"
            f"Expected: {sb}\n"
            f"Actual:   {sa}"
        )


def same_multiset(a: Iterable[Any], b: Iterable[Any]) -> bool:
    """
    Return True if a and b contain the same elements with the same multiplicities,
    regardless of order.
    """
    return Counter(a) == Counter(b)


def assert_same_multiset(a: Iterable[Any], b: Iterable[Any]) -> None:
    ca, cb = Counter(a), Counter(b)
    if ca != cb:
        raise AssertionError(
            f"Multisets differ:\n"
            f"Expected: {cb}\n"
            f"Actual:   {ca}"
        )


# Matrix / 2D Structure Comparisons
def same_matrix(a: Sequence[Sequence[Any]], b: Sequence[Sequence[Any]]) -> bool:
    """
    Return True if two 2D matrices are equal row-by-row.
    """
    return len(a) == len(b) and all(
        same_sequence(row_a, row_b) for row_a, row_b in zip(a, b)
    )


def assert_same_matrix(a: Sequence[Sequence[Any]], b: Sequence[Sequence[Any]]) -> None:
    if not same_matrix(a, b):
        raise AssertionError(
            f"Matrices differ:\n"
            f"Expected: {b}\n"
            f"Actual:   {a}"
        )
