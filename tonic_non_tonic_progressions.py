from __future__ import annotations

from itertools import product
from typing import Iterable


F_SHARP_MINOR_DIATONIC = (
    "F#m",    # i
    "G#dim",  # ii°
    "A",      # III
    "Bm",     # iv
    "C#m",    # v
    "D",      # VI
    "E",      # VII
)

TONIC = "F#m"


def all_progressions(
    length: int,
    chord_pool: tuple[str, ...] = F_SHARP_MINOR_DIATONIC,
    exclude_start_on_tonic: bool = False,
) -> Iterable[tuple[str, ...]]:
    """
    Generate every possible progression of a given length
    from the supplied chord pool.
    """
    if length < 1:
        raise ValueError("length must be >= 1")

    for prog in product(chord_pool, repeat=length):
        if exclude_start_on_tonic and prog[0] == TONIC:
            continue
        yield prog


def tonic_start_progressions(
    length: int,
    chord_pool: tuple[str, ...] = F_SHARP_MINOR_DIATONIC,
    tonic: str = TONIC,
) -> Iterable[tuple[str, ...]]:
    """
    Generate every progression of a given length that starts on tonic.
    """
    if length < 1:
        raise ValueError("length must be >= 1")

    for prog in product(chord_pool, repeat=length):
        if prog[0] == tonic:
            yield prog


def non_tonic_start_progressions(
    length: int,
    chord_pool: tuple[str, ...] = F_SHARP_MINOR_DIATONIC,
    tonic: str = TONIC,
) -> Iterable[tuple[str, ...]]:
    """
    Generate every progression of a given length that does NOT start on tonic.
    """
    if length < 1:
        raise ValueError("length must be >= 1")

    for prog in product(chord_pool, repeat=length):
        if prog[0] != tonic:
            yield prog


def grouped_by_start_type(
    length: int,
    chord_pool: tuple[str, ...] = F_SHARP_MINOR_DIATONIC,
    tonic: str = TONIC,
) -> dict[str, list[tuple[str, ...]]]:
    """
    Return all progressions grouped into:
    - tonic_start
    - non_tonic_start
    """
    if length < 1:
        raise ValueError("length must be >= 1")

    tonic_group: list[tuple[str, ...]] = []
    non_tonic_group: list[tuple[str, ...]] = []

    for prog in product(chord_pool, repeat=length):
        if prog[0] == tonic:
            tonic_group.append(prog)
        else:
            non_tonic_group.append(prog)

    return {
        "tonic_start": tonic_group,
        "non_tonic_start": non_tonic_group,
    }


def progression_count(
    length: int,
    chord_pool: tuple[str, ...] = F_SHARP_MINOR_DIATONIC,
) -> int:
    if length < 1:
        raise ValueError("length must be >= 1")
    return len(chord_pool) ** length


def tonic_start_count(
    length: int,
    chord_pool: tuple[str, ...] = F_SHARP_MINOR_DIATONIC,
) -> int:
    if length < 1:
        raise ValueError("length must be >= 1")
    return len(chord_pool) ** (length - 1)


def non_tonic_start_count(
    length: int,
    chord_pool: tuple[str, ...] = F_SHARP_MINOR_DIATONIC,
) -> int:
    if length < 1:
        raise ValueError("length must be >= 1")
    return (len(chord_pool) - 1) * (len(chord_pool) ** (length - 1))


if __name__ == "__main__":
    length = 4

    print("TONIC START:\n")
    for prog in tonic_start_progressions(length=length):
        print(prog)

    print("\nNON-TONIC START:\n")
    for prog in non_tonic_start_progressions(length=length):
        print(prog)

    print("\nCOUNTS:")
    print("all:", progression_count(length))
    print("tonic start:", tonic_start_count(length))
    print("non-tonic start:", non_tonic_start_count(length))
