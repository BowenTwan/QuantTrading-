import numpy as np

from pandas import Series, to_numeric

from .pandas_vb_common import lib, tm


class ToNumeric:

    params = ["ignore", "coerce"]
    param_names = ["errors"]

    def setup(self, errors):
        N = 10000
        self.float = Series(np.random.randn(N))
        self.numstr = self.float.astype("str")
        self.str = Series(tm.makeStringIndex(N))

    def time_from_float(self, errors):
        to_numeric(self.float, errors=errors)

    def time_from_numeric_str(self, errors):
        to_numeric(self.numstr, errors=errors)

    def time_from_str(self, errors):
        to_numeric(self.str, errors=errors)


class ToNumericDowncast:

    param_names = ["dtype", "downcast"]
    params = [
        [
            "string-float",
            "string-int",
            "string-nint",
            "datetime64",
            "int-list",
            "int32",
        ],
        [None, "integer", "signed", "unsigned", "float"],
    ]

    N = 500000
    N2 = int(N / 2)

    data_dict = {
        "string-int": ["1"] * N2 + [2] * N2,
        "string-nint": ["-1"] * N2 + [2] * N2,
        "datetime64": np.repeat(
            np.array(["1970-01-01", "1970-01-02"], dtype="datetime64[D]"), N
        ),
        "string-float": ["1.1"] * N2 + [2] * N2,
        "int-list": [1] * N2 + [2] * N2,
        "int32": np.repeat(np.int32(1), N),
    }

    def setup(self, dtype, downcast):
        self.data = self.data_dict[dtype]

    def time_downcast(self, dtype, downcast):
        to_numeric(self.data, downcast=downcast)


class MaybeConvertNumeric:
    def setup_cache(self):
        N = 10 ** 6
        arr = np.repeat([2 ** 63], N) + np.arange(N).astype("uint64")
        data = arr.astype(object)
        data[1::2] = arr[1::2].astype(str)
        data[-1] = -1
        return data

    def time_convert(self, data):
        lib.maybe_convert_numeric(data, set(), coerce_numeric=False)


from .pandas_vb_common import setup  # noqa: F401 isort:skip
