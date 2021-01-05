import string

import numpy as np

from pandas import DataFrame, MultiIndex, RangeIndex, date_range

from .pandas_vb_common import tm


class GetLoc:
    def setup(self):
        self.mi_large = MultiIndex.from_product(
            [np.arange(1000), np.arange(20), list(string.ascii_letters)],
            names=["one", "two", "three"],
        )
        self.mi_med = MultiIndex.from_product(
            [np.arange(1000), np.arange(10), list("A")], names=["one", "two", "three"]
        )
        self.mi_small = MultiIndex.from_product(
            [np.arange(100), list("A"), list("A")], names=["one", "two", "three"]
        )

    def time_large_get_loc(self):
        self.mi_large.get_loc((999, 19, "Z"))

    def time_large_get_loc_warm(self):
        for _ in range(1000):
            self.mi_large.get_loc((999, 19, "Z"))

    def time_med_get_loc(self):
        self.mi_med.get_loc((999, 9, "A"))

    def time_med_get_loc_warm(self):
        for _ in range(1000):
            self.mi_med.get_loc((999, 9, "A"))

    def time_string_get_loc(self):
        self.mi_small.get_loc((99, "A", "A"))

    def time_small_get_loc_warm(self):
        for _ in range(1000):
            self.mi_small.get_loc((99, "A", "A"))


class Duplicates:
    def setup(self):
        size = 65536
        arrays = [np.random.randint(0, 8192, size), np.random.randint(0, 1024, size)]
        mask = np.random.rand(size) < 0.1
        self.mi_unused_levels = MultiIndex.from_arrays(arrays)
        self.mi_unused_levels = self.mi_unused_levels[mask]

    def time_remove_unused_levels(self):
        self.mi_unused_levels.remove_unused_levels()


class Integer:
    def setup(self):
        self.mi_int = MultiIndex.from_product(
            [np.arange(1000), np.arange(1000)], names=["one", "two"]
        )
        self.obj_index = np.array(
            [
                (0, 10),
                (0, 11),
                (0, 12),
                (0, 13),
                (0, 14),
                (0, 15),
                (0, 16),
                (0, 17),
                (0, 18),
                (0, 19),
            ],
            dtype=object,
        )
        self.other_mi_many_mismatches = MultiIndex.from_tuples(
            [
                (-7, 41),
                (-2, 3),
                (-0.7, 5),
                (0, 0),
                (0, 1.5),
                (0, 340),
                (0, 1001),
                (1, -4),
                (1, 20),
                (1, 1040),
                (432, -5),
                (432, 17),
                (439, 165.5),
                (998, -4),
                (998, 24065),
                (999, 865.2),
                (999, 1000),
                (1045, -843),
            ]
        )

    def time_get_indexer(self):
        self.mi_int.get_indexer(self.obj_index)

    def time_get_indexer_and_backfill(self):
        self.mi_int.get_indexer(self.other_mi_many_mismatches, method="backfill")

    def time_get_indexer_and_pad(self):
        self.mi_int.get_indexer(self.other_mi_many_mismatches, method="pad")

    def time_is_monotonic(self):
        self.mi_int.is_monotonic


class Duplicated:
    def setup(self):
        n, k = 200, 5000
        levels = [np.arange(n), tm.makeStringIndex(n).values, 1000 + np.arange(n)]
        codes = [np.random.choice(n, (k * n)) for lev in levels]
        self.mi = MultiIndex(levels=levels, codes=codes)

    def time_duplicated(self):
        self.mi.duplicated()


class Sortlevel:
    def setup(self):
        n = 1182720
        low, high = -4096, 4096
        arrs = [
            np.repeat(np.random.randint(low, high, (n // k)), k)
            for k in [11, 7, 5, 3, 1]
        ]
        self.mi_int = MultiIndex.from_arrays(arrs)[np.random.permutation(n)]

        a = np.repeat(np.arange(100), 1000)
        b = np.tile(np.arange(1000), 100)
        self.mi = MultiIndex.from_arrays([a, b])
        self.mi = self.mi.take(np.random.permutation(np.arange(100000)))

    def time_sortlevel_int64(self):
        self.mi_int.sortlevel()

    def time_sortlevel_zero(self):
        self.mi.sortlevel(0)

    def time_sortlevel_one(self):
        self.mi.sortlevel(1)


class Values:
    def setup_cache(self):

        level1 = range(1000)
        level2 = date_range(start="1/1/2012", periods=100)
        mi = MultiIndex.from_product([level1, level2])
        return mi

    def time_datetime_level_values_copy(self, mi):
        mi.copy().values

    def time_datetime_level_values_sliced(self, mi):
        mi[:10].values


class CategoricalLevel:
    def setup(self):

        self.df = DataFrame(
            {
                "a": np.arange(1_000_000, dtype=np.int32),
                "b": np.arange(1_000_000, dtype=np.int64),
                "c": np.arange(1_000_000, dtype=float),
            }
        ).astype({"a": "category", "b": "category"})

    def time_categorical_level(self):
        self.df.set_index(["a", "b"])


class Equals:
    def setup(self):
        idx_large_fast = RangeIndex(100000)
        idx_small_slow = date_range(start="1/1/2012", periods=1)
        self.mi_large_slow = MultiIndex.from_product([idx_large_fast, idx_small_slow])

        self.idx_non_object = RangeIndex(1)

    def time_equals_non_object_index(self):
        self.mi_large_slow.equals(self.idx_non_object)


class SetOperations:

    params = [
        ("monotonic", "non_monotonic"),
        ("datetime", "int", "string"),
        ("intersection", "union", "symmetric_difference"),
    ]
    param_names = ["index_structure", "dtype", "method"]

    def setup(self, index_structure, dtype, method):
        N = 10 ** 5
        level1 = range(1000)

        level2 = date_range(start="1/1/2000", periods=N // 1000)
        dates_left = MultiIndex.from_product([level1, level2])

        level2 = range(N // 1000)
        int_left = MultiIndex.from_product([level1, level2])

        level2 = tm.makeStringIndex(N // 1000).values
        str_left = MultiIndex.from_product([level1, level2])

        data = {
            "datetime": dates_left,
            "int": int_left,
            "string": str_left,
        }

        if index_structure == "non_monotonic":
            data = {k: mi[::-1] for k, mi in data.items()}

        data = {k: {"left": mi, "right": mi[:-1]} for k, mi in data.items()}
        self.left = data[dtype]["left"]
        self.right = data[dtype]["right"]

    def time_operation(self, index_structure, dtype, method):
        getattr(self.left, method)(self.right)


from .pandas_vb_common import setup  # noqa: F401 isort:skip
