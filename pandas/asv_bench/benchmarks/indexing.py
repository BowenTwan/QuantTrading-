"""
These benchmarks are for Series and DataFrame indexing methods.  For the
lower-level methods directly on Index and subclasses, see index_object.py,
indexing_engine.py, and index_cached.py
"""
import itertools
import string
import warnings

import numpy as np

from pandas import (
    CategoricalIndex,
    DataFrame,
    Float64Index,
    IndexSlice,
    Int64Index,
    IntervalIndex,
    MultiIndex,
    Series,
    UInt64Index,
    concat,
    date_range,
    option_context,
    period_range,
)

from .pandas_vb_common import tm


class NumericSeriesIndexing:

    params = [
        (Int64Index, UInt64Index, Float64Index),
        ("unique_monotonic_inc", "nonunique_monotonic_inc"),
    ]
    param_names = ["index_dtype", "index_structure"]

    def setup(self, index, index_structure):
        N = 10 ** 6
        indices = {
            "unique_monotonic_inc": index(range(N)),
            "nonunique_monotonic_inc": index(
                list(range(55)) + [54] + list(range(55, N - 1))
            ),
        }
        self.data = Series(np.random.rand(N), index=indices[index_structure])
        self.array = np.arange(10000)
        self.array_list = self.array.tolist()

    def time_getitem_scalar(self, index, index_structure):
        self.data[800000]

    def time_getitem_slice(self, index, index_structure):
        self.data[:800000]

    def time_getitem_list_like(self, index, index_structure):
        self.data[[800000]]

    def time_getitem_array(self, index, index_structure):
        self.data[self.array]

    def time_getitem_lists(self, index, index_structure):
        self.data[self.array_list]

    def time_iloc_array(self, index, index_structure):
        self.data.iloc[self.array]

    def time_iloc_list_like(self, index, index_structure):
        self.data.iloc[[800000]]

    def time_iloc_scalar(self, index, index_structure):
        self.data.iloc[800000]

    def time_iloc_slice(self, index, index_structure):
        self.data.iloc[:800000]

    def time_loc_array(self, index, index_structure):
        self.data.loc[self.array]

    def time_loc_list_like(self, index, index_structure):
        self.data.loc[[800000]]

    def time_loc_scalar(self, index, index_structure):
        self.data.loc[800000]

    def time_loc_slice(self, index, index_structure):
        self.data.loc[:800000]


class NonNumericSeriesIndexing:

    params = [
        ("string", "datetime", "period"),
        ("unique_monotonic_inc", "nonunique_monotonic_inc", "non_monotonic"),
    ]
    param_names = ["index_dtype", "index_structure"]

    def setup(self, index, index_structure):
        N = 10 ** 6
        if index == "string":
            index = tm.makeStringIndex(N)
        elif index == "datetime":
            index = date_range("1900", periods=N, freq="s")
        elif index == "period":
            index = period_range("1900", periods=N, freq="s")
        index = index.sort_values()
        assert index.is_unique and index.is_monotonic_increasing
        if index_structure == "nonunique_monotonic_inc":
            index = index.insert(item=index[2], loc=2)[:-1]
        elif index_structure == "non_monotonic":
            index = index[::2].append(index[1::2])
            assert len(index) == N
        self.s = Series(np.random.rand(N), index=index)
        self.lbl = index[80000]
        # warm up index mapping
        self.s[self.lbl]

    def time_getitem_label_slice(self, index, index_structure):
        self.s[: self.lbl]

    def time_getitem_pos_slice(self, index, index_structure):
        self.s[:80000]

    def time_getitem_scalar(self, index, index_structure):
        self.s[self.lbl]

    def time_getitem_list_like(self, index, index_structure):
        self.s[[self.lbl]]


class DataFrameStringIndexing:
    def setup(self):
        index = tm.makeStringIndex(1000)
        columns = tm.makeStringIndex(30)
        with warnings.catch_warnings(record=True):
            self.df = DataFrame(np.random.randn(1000, 30), index=index, columns=columns)
        self.idx_scalar = index[100]
        self.col_scalar = columns[10]
        self.bool_indexer = self.df[self.col_scalar] > 0
        self.bool_obj_indexer = self.bool_indexer.astype(object)
        self.boolean_indexer = (self.df[self.col_scalar] > 0).astype("boolean")

    def time_loc(self):
        self.df.loc[self.idx_scalar, self.col_scalar]

    def time_getitem_scalar(self):
        self.df[self.col_scalar][self.idx_scalar]

    def time_boolean_rows(self):
        self.df[self.bool_indexer]

    def time_boolean_rows_object(self):
        self.df[self.bool_obj_indexer]

    def time_boolean_rows_boolean(self):
        self.df[self.boolean_indexer]


class DataFrameNumericIndexing:
    def setup(self):
        self.idx_dupe = np.array(range(30)) * 99
        self.df = DataFrame(np.random.randn(100000, 5))
        self.df_dup = concat([self.df, 2 * self.df, 3 * self.df])
        self.bool_indexer = [True] * 50000 + [False] * 50000

    def time_iloc_dups(self):
        self.df_dup.iloc[self.idx_dupe]

    def time_loc_dups(self):
        self.df_dup.loc[self.idx_dupe]

    def time_iloc(self):
        self.df.iloc[:100, 0]

    def time_loc(self):
        self.df.loc[:100, 0]

    def time_bool_indexer(self):
        self.df[self.bool_indexer]


class Take:

    params = ["int", "datetime"]
    param_names = ["index"]

    def setup(self, index):
        N = 100000
        indexes = {
            "int": Int64Index(np.arange(N)),
            "datetime": date_range("2011-01-01", freq="S", periods=N),
        }
        index = indexes[index]
        self.s = Series(np.random.rand(N), index=index)
        self.indexer = np.random.randint(0, N, size=N)

    def time_take(self, index):
        self.s.take(self.indexer)


class MultiIndexing:
    def setup(self):
        mi = MultiIndex.from_product([range(1000), range(1000)])
        self.s = Series(np.random.randn(1000000), index=mi)
        self.df = DataFrame(self.s)

        n = 100000
        with warnings.catch_warnings(record=True):
            self.mdt = DataFrame(
                {
                    "A": np.random.choice(range(10000, 45000, 1000), n),
                    "B": np.random.choice(range(10, 400), n),
                    "C": np.random.choice(range(1, 150), n),
                    "D": np.random.choice(range(10000, 45000), n),
                    "x": np.random.choice(range(400), n),
                    "y": np.random.choice(range(25), n),
                }
            )
        self.idx = IndexSlice[20000:30000, 20:30, 35:45, 30000:40000]
        self.mdt = self.mdt.set_index(["A", "B", "C", "D"]).sort_index()

    def time_index_slice(self):
        self.mdt.loc[self.idx, :]


class IntervalIndexing:
    def setup_cache(self):
        idx = IntervalIndex.from_breaks(np.arange(1000001))
        monotonic = Series(np.arange(1000000), index=idx)
        return monotonic

    def time_getitem_scalar(self, monotonic):
        monotonic[80000]

    def time_loc_scalar(self, monotonic):
        monotonic.loc[80000]

    def time_getitem_list(self, monotonic):
        monotonic[80000:]

    def time_loc_list(self, monotonic):
        monotonic.loc[80000:]


class CategoricalIndexIndexing:

    params = ["monotonic_incr", "monotonic_decr", "non_monotonic"]
    param_names = ["index"]

    def setup(self, index):
        N = 10 ** 5
        values = list("a" * N + "b" * N + "c" * N)
        indices = {
            "monotonic_incr": CategoricalIndex(values),
            "monotonic_decr": CategoricalIndex(reversed(values)),
            "non_monotonic": CategoricalIndex(list("abc" * N)),
        }
        self.data = indices[index]
        self.data_unique = CategoricalIndex(
            ["".join(perm) for perm in itertools.permutations(string.printable, 3)]
        )

        self.int_scalar = 10000
        self.int_list = list(range(10000))

        self.cat_scalar = "b"
        self.cat_list = ["a", "c"]

    def time_getitem_scalar(self, index):
        self.data[self.int_scalar]

    def time_getitem_slice(self, index):
        self.data[: self.int_scalar]

    def time_getitem_list_like(self, index):
        self.data[[self.int_scalar]]

    def time_getitem_list(self, index):
        self.data[self.int_list]

    def time_getitem_bool_array(self, index):
        self.data[self.data == self.cat_scalar]

    def time_get_loc_scalar(self, index):
        self.data.get_loc(self.cat_scalar)

    def time_get_indexer_list(self, index):
        self.data_unique.get_indexer(self.cat_list)


class MethodLookup:
    def setup_cache(self):
        s = Series()
        return s

    def time_lookup_iloc(self, s):
        s.iloc

    def time_lookup_loc(self, s):
        s.loc


class GetItemSingleColumn:
    def setup(self):
        self.df_string_col = DataFrame(np.random.randn(3000, 1), columns=["A"])
        self.df_int_col = DataFrame(np.random.randn(3000, 1))

    def time_frame_getitem_single_column_label(self):
        self.df_string_col["A"]

    def time_frame_getitem_single_column_int(self):
        self.df_int_col[0]


class IndexSingleRow:
    params = [True, False]
    param_names = ["unique_cols"]

    def setup(self, unique_cols):
        arr = np.arange(10 ** 7).reshape(-1, 10)
        df = DataFrame(arr)
        dtypes = ["u1", "u2", "u4", "u8", "i1", "i2", "i4", "i8", "f8", "f4"]
        for i, d in enumerate(dtypes):
            df[i] = df[i].astype(d)

        if not unique_cols:
            # GH#33032 single-row lookups with non-unique columns were
            #  15x slower than with unique columns
            df.columns = ["A", "A"] + list(df.columns[2:])

        self.df = df

    def time_iloc_row(self, unique_cols):
        self.df.iloc[10000]

    def time_loc_row(self, unique_cols):
        self.df.loc[10000]


class AssignTimeseriesIndex:
    def setup(self):
        N = 100000
        idx = date_range("1/1/2000", periods=N, freq="H")
        self.df = DataFrame(np.random.randn(N, 1), columns=["A"], index=idx)

    def time_frame_assign_timeseries_index(self):
        self.df["date"] = self.df.index


class InsertColumns:
    def setup(self):
        self.N = 10 ** 3
        self.df = DataFrame(index=range(self.N))

    def time_insert(self):
        np.random.seed(1234)
        for i in range(100):
            self.df.insert(0, i, np.random.randn(self.N), allow_duplicates=True)

    def time_assign_with_setitem(self):
        np.random.seed(1234)
        for i in range(100):
            self.df[i] = np.random.randn(self.N)

    def time_assign_list_like_with_setitem(self):
        np.random.seed(1234)
        self.df[list(range(100))] = np.random.randn(self.N, 100)

    def time_assign_list_of_columns_concat(self):
        df = DataFrame(np.random.randn(self.N, 100))
        concat([self.df, df], axis=1)


class ChainIndexing:

    params = [None, "warn"]
    param_names = ["mode"]

    def setup(self, mode):
        self.N = 1000000

    def time_chained_indexing(self, mode):
        with warnings.catch_warnings(record=True):
            with option_context("mode.chained_assignment", mode):
                df = DataFrame({"A": np.arange(self.N), "B": "foo"})
                df2 = df[df.A > self.N // 2]
                df2["C"] = 1.0


from .pandas_vb_common import setup  # noqa: F401 isort:skip
