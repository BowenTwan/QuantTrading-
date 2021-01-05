import warnings

import numpy as np

from pandas import Categorical, DataFrame, Series

from .pandas_vb_common import tm


class Construction:

    params = ["str", "string"]
    param_names = ["dtype"]

    def setup(self, dtype):
        self.series_arr = tm.rands_array(nchars=10, size=10 ** 5)
        self.frame_arr = self.series_arr.reshape((50_000, 2)).copy()

        # GH37371. Testing construction of string series/frames from ExtensionArrays
        self.series_cat_arr = Categorical(self.series_arr)
        self.frame_cat_arr = Categorical(self.frame_arr)

    def time_series_construction(self, dtype):
        Series(self.series_arr, dtype=dtype)

    def peakmem_series_construction(self, dtype):
        Series(self.series_arr, dtype=dtype)

    def time_frame_construction(self, dtype):
        DataFrame(self.frame_arr, dtype=dtype)

    def peakmem_frame_construction(self, dtype):
        DataFrame(self.frame_arr, dtype=dtype)

    def time_cat_series_construction(self, dtype):
        Series(self.series_cat_arr, dtype=dtype)

    def peakmem_cat_series_construction(self, dtype):
        Series(self.series_cat_arr, dtype=dtype)

    def time_cat_frame_construction(self, dtype):
        DataFrame(self.frame_cat_arr, dtype=dtype)

    def peakmem_cat_frame_construction(self, dtype):
        DataFrame(self.frame_cat_arr, dtype=dtype)


class Methods:
    def setup(self):
        self.s = Series(tm.makeStringIndex(10 ** 5))

    def time_center(self):
        self.s.str.center(100)

    def time_count(self):
        self.s.str.count("A")

    def time_endswith(self):
        self.s.str.endswith("A")

    def time_extract(self):
        with warnings.catch_warnings(record=True):
            self.s.str.extract("(\\w*)A(\\w*)")

    def time_findall(self):
        self.s.str.findall("[A-Z]+")

    def time_find(self):
        self.s.str.find("[A-Z]+")

    def time_rfind(self):
        self.s.str.rfind("[A-Z]+")

    def time_get(self):
        self.s.str.get(0)

    def time_len(self):
        self.s.str.len()

    def time_join(self):
        self.s.str.join(" ")

    def time_match(self):
        self.s.str.match("A")

    def time_normalize(self):
        self.s.str.normalize("NFC")

    def time_pad(self):
        self.s.str.pad(100, side="both")

    def time_partition(self):
        self.s.str.partition("A")

    def time_rpartition(self):
        self.s.str.rpartition("A")

    def time_replace(self):
        self.s.str.replace("A", "\x01\x01")

    def time_translate(self):
        self.s.str.translate({"A": "\x01\x01"})

    def time_slice(self):
        self.s.str.slice(5, 15, 2)

    def time_startswith(self):
        self.s.str.startswith("A")

    def time_strip(self):
        self.s.str.strip("A")

    def time_rstrip(self):
        self.s.str.rstrip("A")

    def time_lstrip(self):
        self.s.str.lstrip("A")

    def time_title(self):
        self.s.str.title()

    def time_upper(self):
        self.s.str.upper()

    def time_lower(self):
        self.s.str.lower()

    def time_wrap(self):
        self.s.str.wrap(10)

    def time_zfill(self):
        self.s.str.zfill(10)


class Repeat:

    params = ["int", "array"]
    param_names = ["repeats"]

    def setup(self, repeats):
        N = 10 ** 5
        self.s = Series(tm.makeStringIndex(N))
        repeat = {"int": 1, "array": np.random.randint(1, 3, N)}
        self.values = repeat[repeats]

    def time_repeat(self, repeats):
        self.s.str.repeat(self.values)


class Cat:

    params = ([0, 3], [None, ","], [None, "-"], [0.0, 0.001, 0.15])
    param_names = ["other_cols", "sep", "na_rep", "na_frac"]

    def setup(self, other_cols, sep, na_rep, na_frac):
        N = 10 ** 5
        mask_gen = lambda: np.random.choice([True, False], N, p=[1 - na_frac, na_frac])
        self.s = Series(tm.makeStringIndex(N)).where(mask_gen())
        if other_cols == 0:
            # str.cat self-concatenates only for others=None
            self.others = None
        else:
            self.others = DataFrame(
                {i: tm.makeStringIndex(N).where(mask_gen()) for i in range(other_cols)}
            )

    def time_cat(self, other_cols, sep, na_rep, na_frac):
        # before the concatenation (one caller + other_cols columns), the total
        # expected fraction of rows containing any NaN is:
        # reduce(lambda t, _: t + (1 - t) * na_frac, range(other_cols + 1), 0)
        # for other_cols=3 and na_frac=0.15, this works out to ~48%
        self.s.str.cat(others=self.others, sep=sep, na_rep=na_rep)


class Contains:

    params = [True, False]
    param_names = ["regex"]

    def setup(self, regex):
        self.s = Series(tm.makeStringIndex(10 ** 5))

    def time_contains(self, regex):
        self.s.str.contains("A", regex=regex)


class Split:

    params = [True, False]
    param_names = ["expand"]

    def setup(self, expand):
        self.s = Series(tm.makeStringIndex(10 ** 5)).str.join("--")

    def time_split(self, expand):
        self.s.str.split("--", expand=expand)

    def time_rsplit(self, expand):
        self.s.str.rsplit("--", expand=expand)


class Dummies:
    def setup(self):
        self.s = Series(tm.makeStringIndex(10 ** 5)).str.join("|")

    def time_get_dummies(self):
        self.s.str.get_dummies("|")


class Encode:
    def setup(self):
        self.ser = Series(tm.makeUnicodeIndex())

    def time_encode_decode(self):
        self.ser.str.encode("utf-8").str.decode("utf-8")


class Slice:
    def setup(self):
        self.s = Series(["abcdefg", np.nan] * 500000)

    def time_vector_slice(self):
        # GH 2602
        self.s.str[:5]
