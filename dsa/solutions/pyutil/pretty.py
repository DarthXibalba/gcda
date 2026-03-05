"""
Collection of pretty print functions
"""

from __future__ import annotations

from collections import deque
from dataclasses import is_dataclass, asdict
from pprint import pformat
from typing import Any, Iterable, Sequence, Mapping, Optional


# ----------------------------
# Core formatting primitives
# ----------------------------

def pretty(obj: Any, *, width: int = 100, compact: bool = True, sort_dicts: bool = True) -> str:
    """
    Generic pretty formatter for arbitrary Python objects.
    Uses pprint formatting; handles dataclasses by converting to dict.
    """
    if is_dataclass(obj):
        obj = asdict(obj)
    return pformat(obj, width=width, compact=compact, sort_dicts=sort_dicts)


def truncate_middle(s: str, *, max_len: int = 200) -> str:
    """
    Truncate a long string in the middle to preserve both prefix and suffix.
    """
    if len(s) <= max_len:
        return s
    half = (max_len - 3) // 2
    return f"{s[:half]}...{s[-half:]}"


# ----------------------------
# Arrays and sequences
# ----------------------------

def pretty_list(
    xs: Sequence[Any],
    *,
    show_index: bool = False,
    max_items: int = 40,
    item_width: int = 16
) -> str:
    """
    Pretty-print a 1D sequence.
    - show_index: prints indices above values (useful for pointer problems).
    - max_items: truncates long sequences with an ellipsis.
    - item_width: column width when show_index=True.
    """
    n = len(xs)
    if n == 0:
        return "[]"

    if n > max_items:
        head = list(xs[: max_items // 2])
        tail = list(xs[-max_items // 2 :])
        view = head + ["..."] + tail
    else:
        view = list(xs)

    if not show_index:
        return pretty(view)

    # index header + values aligned in columns
    def fmt_cell(v: Any) -> str:
        s = str(v)
        s = truncate_middle(s, max_len=item_width - 1)
        return s.rjust(item_width)

    idx_cells = [fmt_cell(i) for i in range(len(view))]
    val_cells = [fmt_cell(v) for v in view]
    return "\n".join([
        "idx:" + "".join(idx_cells),
        "val:" + "".join(val_cells),
    ])


def pretty_window(
    xs: Sequence[Any],
    *,
    left: int,
    right: int,
    pointers: Optional[Mapping[str, int]] = None,
    max_items: int = 60
) -> str:
    """
    Pretty-print a sequence with a highlighted window [left, right] and optional pointer markers.
    Intended for sliding window / two pointers debugging.
    """
    n = len(xs)
    if n == 0:
        return "[]"

    # build a compact view if huge
    if n > max_items:
        # show slice around window
        pad = max(5, (max_items - (right - left + 1)) // 2)
        start = max(0, left - pad)
        end = min(n, right + pad + 1)
        view = xs[start:end]
        offset = start
        prefix = "..." if start > 0 else ""
        suffix = "..." if end < n else ""
    else:
        view = xs
        offset = 0
        prefix = suffix = ""

    # value line
    values = [str(v) for v in view]
    # marker line for window and pointers
    markers = [" " * len(s) for s in values]

    for i in range(len(view)):
        gi = i + offset
        if left <= gi <= right:
            markers[i] = "^" * max(1, len(values[i]))

    if pointers:
        for name, idx in pointers.items():
            if offset <= idx < offset + len(view):
                j = idx - offset
                markers[j] = name[: max(1, len(values[j]))].ljust(max(1, len(values[j])))

    val_line = " ".join(values)
    mark_line = " ".join(markers)
    return "\n".join([
        prefix + val_line + suffix,
        prefix + mark_line + suffix,
        f"window=[{left}, {right}] pointers={dict(pointers) if pointers else {}} offset={offset}",
    ])


# ----------------------------
# Matrices / grids
# ----------------------------

def pretty_matrix(
    grid: Sequence[Sequence[Any]],
    *,
    max_rows: int = 25,
    max_cols: int = 25,
    cell_width: int = 6,
    show_coords: bool = False
) -> str:
    """
    Pretty-print a 2D matrix with aligned columns.
    Truncates large matrices and optionally prints row/col coordinates.
    """
    if not grid:
        return "[]"

    rows = len(grid)
    cols = max((len(r) for r in grid), default=0)

    # crop
    r_view = min(rows, max_rows)
    c_view = min(cols, max_cols)

    def cell(v: Any) -> str:
        s = str(v)
        s = truncate_middle(s, max_len=cell_width - 1)
        return s.rjust(cell_width)

    lines = []
    if show_coords:
        header = " " * (cell_width + 2) + "".join(cell(c) for c in range(c_view))
        if c_view < cols:
            header += "  ..."
        lines.append(header)

    for i in range(r_view):
        row = grid[i]
        row_cells = [cell(row[j]) if j < len(row) else cell("") for j in range(c_view)]
        line = "".join(row_cells)
        if c_view < cols:
            line += "  ..."
        if show_coords:
            line = f"{str(i).rjust(cell_width)} |" + line
        lines.append(line)

    if r_view < rows:
        lines.append("...")

    return "\n".join(lines)


# ----------------------------
# Linked list (cycle-safe)
# ----------------------------

def pretty_linked_list(
    head: Any,
    *,
    next_attr: str = "next",
    val_attr: str = "val",
    max_nodes: int = 60
) -> str:
    """
    Pretty-print a singly linked list.
    - Detects cycles by object identity.
    - Works with typical LeetCode ListNode {val, next}.
    """
    if head is None:
        return "None"

    parts = []
    seen = set()
    node = head
    steps = 0

    while node is not None and steps < max_nodes:
        node_id = id(node)
        if node_id in seen:
            parts.append(f"(cycle to {getattr(node, val_attr, '?')})")
            break
        seen.add(node_id)

        parts.append(str(getattr(node, val_attr, node)))
        node = getattr(node, next_attr, None)
        steps += 1

    if steps >= max_nodes and node is not None:
        parts.append("...")

    return " -> ".join(parts)


# ----------------------------
# Binary tree (level order + simple ASCII)
# ----------------------------

def tree_to_level_order(
    root: Any,
    *,
    left_attr: str = "left",
    right_attr: str = "right",
    val_attr: str = "val",
    max_nodes: int = 200
) -> list[Any]:
    """
    Serialize a binary tree to a LeetCode-style level-order list with None placeholders,
    trimming trailing Nones. Intended for debugging and comparisons.
    """
    if root is None:
        return []

    out: list[Any] = []
    q = deque([root])
    count = 0

    while q and count < max_nodes:
        node = q.popleft()
        count += 1

        if node is None:
            out.append(None)
            continue

        out.append(getattr(node, val_attr, node))
        q.append(getattr(node, left_attr, None))
        q.append(getattr(node, right_attr, None))

    # trim trailing Nones
    while out and out[-1] is None:
        out.pop()

    if q:
        out.append("...")

    return out


def pretty_tree_level_order(root: Any, **kwargs: Any) -> str:
    """
    Pretty-print a binary tree as a level-order list (LeetCode-style).
    """
    return pretty(tree_to_level_order(root, **kwargs))


def pretty_tree_ascii(
    root: Any,
    *,
    left_attr: str = "left",
    right_attr: str = "right",
    val_attr: str = "val",
    max_depth: int = 8
) -> str:
    """
    Simple ASCII tree printer (sideways).
    Right subtree on top, left subtree on bottom.
    Truncates beyond max_depth to avoid huge output.
    """
    lines: list[str] = []

    def rec(node: Any, prefix: str, is_left: bool, depth: int) -> None:
        if node is None:
            return
        if depth > max_depth:
            lines.append(prefix + ("└── " if is_left else "┌── ") + "...")
            return

        right = getattr(node, right_attr, None)
        left = getattr(node, left_attr, None)

        if right is not None:
            rec(right, prefix + ("│   " if is_left else "    "), False, depth + 1)

        lines.append(prefix + ("└── " if is_left else "┌── ") + str(getattr(node, val_attr, node)))

        if left is not None:
            rec(left, prefix + ("    " if is_left else "│   "), True, depth + 1)

    rec(root, "", True, 1)
    return "\n".join(lines) if lines else "None"


# ----------------------------
# Diff helpers (expected vs actual)
# ----------------------------

def first_mismatch(a: Sequence[Any], b: Sequence[Any]) -> Optional[int]:
    """
    Return the first index where sequences a and b differ.
    Return None if they match completely (including length).
    """
    n = min(len(a), len(b))
    for i in range(n):
        if a[i] != b[i]:
            return i
    if len(a) != len(b):
        return n
    return None


def pretty_sequence_diff(expected: Sequence[Any], actual: Sequence[Any], *, context: int = 3) -> str:
    """
    Produce a compact diff for two sequences by showing the first mismatch
    and nearby context.
    """
    i = first_mismatch(expected, actual)
    if i is None:
        return "No differences."

    start = max(0, i - context)
    end = i + context + 1

    exp_slice = list(expected[start:end])
    act_slice = list(actual[start:end])

    return "\n".join([
        f"First mismatch at index {i}",
        f"expected[{start}:{end}] = {exp_slice}",
        f"actual  [{start}:{end}] = {act_slice}",
        f"expected length={len(expected)} actual length={len(actual)}",
    ])


# ----------------------------
# Optional print wrappers (convenience)
# ----------------------------

def debug(label: str, obj: Any) -> None:
    """
    Convenience printer: prints a label and a pretty-formatted object.
    Useful for quick instrumentation during debugging.
    """
    print(f"{label}:\n{pretty(obj)}")
