from datetime import timedelta

import dateutil
import numpy as np

from pandas import (
    DataFrame,
    Series,
    date_range,
    period_range,
    timedelta_range,
    to_datetime,
)

from pandas.tseries.frequencies import infer_freq

try:
    from pandas.plotting._matplotlib.converter import DatetimeConverter
except ImportError:
    from pandas.tseries.converter import DatetimeConverter


class DatetimeIndex:

    params = ["dst", "repeated", "tz_aware", "tz_local", "tz_naive"]
    param_names = ["index_type"]

    def setup(self, index_type):
        N = 100000
        dtidxes = {
            "dst": date_range(
                start="10/29/2000 1:00:00", end="10/29/2000 1:59:59", freq="S"
            ),
            "repeated": date_range(start="2000", periods=N / 10, freq="s").repeat(10),
            "tz_aware": date_range(start="2000", periods=N, freq="s", tz="US/Eastern"),
            "tz_local": date_range(
                start="2000", periods=N, freq="s", tz=dateutil.tz.tzlocal()
            ),
            "tz_naive": date_range(start="2000", periods=N, freq="s"),
        }
        self.index = dtidxes[index_type]

    def time_add_timedelta(self, index_type):
        self.index + timedelta(minutes=2)

    def time_normalize(self, index_type):
        self.index.normalize()

    def time_unique(self, index_type):
        self.index.unique()

    def time_to_time(self, index_type):
        self.index.time

    def time_get(self, index_type):
        self.index[0]

    def time_timeseries_is_month_start(self, index_type):
        self.index.is_month_start

    def time_to_date(self, index_type):
        self.index.date

    def time_to_pydatetime(self, index_type):
        self.index.to_pydatetime()

    def time_is_dates_only(self, index_type):
        self.index._is_dates_only


class TzLocalize:

    params = [None, "US/Eastern", "UTC", dateutil.tz.tzutc()]
    param_names = "tz"

    def setup(self, tz):
        dst_rng = date_range(
            start="10/29/2000 1:00:00", end="10/29/2000 1:59:59", freq="S"
        )
        self.index = date_range(start="10/29/2000", end="10/29/2000 00:59:59", freq="S")
        self.index = self.index.append(dst_rng)
        self.index = self.index.append(dst_rng)
        self.index = self.index.append(
            date_range(start="10/29/2000 2:00:00", end="10/29/2000 3:00:00", freq="S")
        )

    def time_infer_dst(self, tz):
        self.index.tz_localize(tz, ambiguous="infer")


class ResetIndex:

    params = [None, "US/Eastern"]
    param_names = "tz"

    def setup(self, tz):
        idx = date_range(start="1/1/2000", periods=1000, freq="H", tz=tz)
        self.df = DataFrame(np.random.randn(1000, 2), index=idx)

    def time_reest_datetimeindex(self, tz):
        self.df.reset_index()


class InferFreq:

    params = [None, "D", "B"]
    param_names = ["freq"]

    def setup(self, freq):
        if freq is None:
            self.idx = date_range(start="1/1/1700", freq="D", periods=10000)
            self.idx._data._freq = None
        else:
            self.idx = date_range(start="1/1/1700", freq=freq, periods=10000)

    def time_infer_freq(self, freq):
        infer_freq(self.idx)


class TimeDatetimeConverter:
    def setup(self):
        N = 100000
        self.rng = date_range(start="1/1/2000", periods=N, freq="T")

    def time_convert(self):
        DatetimeConverter.convert(self.rng, None, None)


class Iteration:

    params = [date_range, period_range, timedelta_range]
    param_names = ["time_index"]

    def setup(self, time_index):
        N = 10 ** 6
        if time_index is timedelta_range:
            self.idx = time_index(start=0, freq="T", periods=N)
        else:
            self.idx = time_index(start="20140101", freq="T", periods=N)
        self.exit = 10000

    def time_iter(self, time_index):
        for _ in self.idx:
            pass

    def time_iter_preexit(self, time_index):
        for i, _ in enumerate(self.idx):
            if i > self.exit:
                break


class ResampleDataFrame:

    params = ["max", "mean", "min"]
    param_names = ["method"]

    def setup(self, method):
        rng = date_range(start="20130101", periods=100000, freq="50L")
        df = DataFrame(np.random.randn(100000, 2), index=rng)
        self.resample = getattr(df.resample("1s"), method)

    def time_method(self, method):
        self.resample()


class ResampleSeries:

    params = (["period", "datetime"], ["5min", "1D"], ["mean", "ohlc"])
    param_names = ["index", "freq", "method"]

    def setup(self, index, freq, method):
        indexes = {
            "period": period_range(start="1/1/2000", end="1/1/2001", freq="T"),
            "datetime": date_range(start="1/1/2000", end="1/1/2001", freq="T"),
        }
        idx = indexes[index]
        ts = Series(np.random.randn(len(idx)), index=idx)
        self.resample = getattr(ts.resample(freq), method)

    def time_resample(self, index, freq, method):
        self.resample()


class ResampleDatetetime64:
    # GH 7754
    def setup(self):
        rng3 = date_range(
            start="2000-01-01 00:00:00", end="2000-01-01 10:00:00", freq="555000U"
        )
        self.dt_ts = Series(5, rng3, dtype="datetime64[ns]")

    def time_resample(self):
        self.dt_ts.resample("1S").last()


class AsOf:

    params = ["DataFrame", "Series"]
    param_names = ["constructor"]

    def setup(self, constructor):
        N = 10000
        M = 10
        rng = date_range(start="1/1/1990", periods=N, freq="53s")
        data = {
            "DataFrame": DataFrame(np.random.randn(N, M)),
            "Series": Series(np.random.randn(N)),
        }
        self.ts = data[constructor]
        self.ts.index = rng
        self.ts2 = self.ts.copy()
        self.ts2.iloc[250:5000] = np.nan
        self.ts3 = self.ts.copy()
        self.ts3.iloc[-5000:] = np.nan
        self.dates = date_range(start="1/1/1990", periods=N * 10, freq="5s")
        self.date = self.dates[0]
        self.date_last = self.dates[-1]
        self.date_early = self.date - timedelta(10)

    # test speed of pre-computing NAs.
    def time_asof(self, constructor):
        self.ts.asof(self.dates)

    # should be roughly the same as above.
    def time_asof_nan(self, constructor):
        self.ts2.asof(self.dates)

    # test speed of the code path for a scalar index
    # without *while* loop
    def time_asof_single(self, constructor):
        self.ts.asof(self.date)

    # test speed of the code path for a scalar index
    # before the start. should be the same as above.
    def time_asof_single_early(self, constructor):
        self.ts.asof(self.date_early)

    # test the speed of the code path for a scalar index
    # with a long *while* loop. should still be much
    # faster than pre-computing all the NAs.
    def time_asof_nan_single(self, constructor):
        self.ts3.asof(self.date_last)


class SortIndex:

    params = [True, False]
    param_names = ["monotonic"]

    def setup(self, monotonic):
        N = 10 ** 5
        idx = date_range(start="1/1/2000", periods=N, freq="s")
        self.s = Series(np.random.randn(N), index=idx)
        if not monotonic:
            self.s = self.s.sample(frac=1)

    def time_sort_index(self, monotonic):
        self.s.sort_index()

    def time_get_slice(self, monotonic):
        self.s[:10000]


class Lookup:
    def setup(self):
        N = 1500000
        rng = date_range(start="1/1/2000", periods=N, freq="S")
        self.ts = Series(1, index=rng)
        self.lookup_val = rng[N // 2]

    def time_lookup_and_cleanup(self):
        self.ts[self.lookup_val]
        self.ts.index._cleanup()


class ToDatetimeFromIntsFloats:
    def setup(self):
        self.ts_sec = Series(range(1521080307, 1521685107), dtype="int64")
        self.ts_sec_float = self.ts_sec.astype("float64")

        self.ts_nanosec = 1_000_000 * self.ts_sec
        self.ts_nanosec_float = self.ts_nanosec.astype("float64")

    # speed of int64 and float64 paths should be comparable

    def time_nanosec_int64(self):
        to_datetime(self.ts_nanosec, unit="ns")

    def time_nanosec_float64(self):
        to_datetime(self.ts_nanosec_float, unit="ns")

    def time_sec_int64(self):
        to_datetime(self.ts_sec, unit="s")

    def time_sec_float64(self):
        to_datetime(self.ts_sec_float, unit="s")


class ToDatetimeYYYYMMDD:
    def setup(self):
        rng = date_range(start="1/1/2000", periods=10000, freq="D")
        self.stringsD = Series(rng.strftime("%Y%m%d"))

    def time_format_YYYYMMDD(self):
        to_datetime(self.stringsD, format="%Y%m%d")


class ToDatetimeCacheSmallCount:

    params = ([True, False], [50, 500, 5000, 100000])
    param_names = ["cache", "count"]

    def setup(self, cache, count):
        rng = date_range(start="1/1/1971", periods=count)
        self.unique_date_strings = rng.strftime("%Y-%m-%d").tolist()

    def time_unique_date_strings(self, cache, count):
        to_datetime(self.unique_date_strings, cache=cache)


class ToDatetimeISO8601:
    def setup(self):
        rng = date_range(start="1/1/2000", periods=20000, freq="H")
        self.strings = rng.strftime("%Y-%m-%d %H:%M:%S").tolist()
        self.strings_nosep = rng.strftime("%Y%m%d %H:%M:%S").tolist()
        self.strings_tz_space = [
            x.strftime("%Y-%m-%d %H:%M:%S") + " -0800" for x in rng
        ]

    def time_iso8601(self):
        to_datetime(self.strings)

    def time_iso8601_nosep(self):
        to_datetime(self.strings_nosep)

    def time_iso8601_format(self):
        to_datetime(self.strings, format="%Y-%m-%d %H:%M:%S")

    def time_iso8601_format_no_sep(self):
        to_datetime(self.strings_nosep, format="%Y%m%d %H:%M:%S")

    def time_iso8601_tz_spaceformat(self):
        to_datetime(self.strings_tz_space)


class ToDatetimeNONISO8601:
    def setup(self):
        N = 10000
        half = int(N / 2)
        ts_string_1 = "March 1, 2018 12:00:00+0400"
        ts_string_2 = "March 1, 2018 12:00:00+0500"
        self.same_offset = [ts_string_1] * N
        self.diff_offset = [ts_string_1] * half + [ts_string_2] * half

    def time_same_offset(self):
        to_datetime(self.same_offset)

    def time_different_offset(self):
        to_datetime(self.diff_offset)


class ToDatetimeFormatQuarters:
    def setup(self):
        self.s = Series(["2Q2005", "2Q05", "2005Q1", "05Q1"] * 10000)

    def time_infer_quarter(self):
        to_datetime(self.s)


class ToDatetimeFormat:
    def setup(self):
        N = 100000
        self.s = Series(["19MAY11", "19MAY11:00:00:00"] * N)
        self.s2 = self.s.str.replace(":\\S+$", "")

        self.same_offset = ["10/11/2018 00:00:00.045-07:00"] * N
        self.diff_offset = [
            f"10/11/2018 00:00:00.045-0{offset}:00" for offset in range(10)
        ] * int(N / 10)

    def time_exact(self):
        to_datetime(self.s2, format="%d%b%y")

    def time_no_exact(self):
        to_datetime(self.s, format="%d%b%y", exact=False)

    def time_same_offset(self):
        to_datetime(self.same_offset, format="%m/%d/%Y %H:%M:%S.%f%z")

    def time_different_offset(self):
        to_datetime(self.diff_offset, format="%m/%d/%Y %H:%M:%S.%f%z")

    def time_same_offset_to_utc(self):
        to_datetime(self.same_offset, format="%m/%d/%Y %H:%M:%S.%f%z", utc=True)

    def time_different_offset_to_utc(self):
        to_datetime(self.diff_offset, format="%m/%d/%Y %H:%M:%S.%f%z", utc=True)


class ToDatetimeCache:

    params = [True, False]
    param_names = ["cache"]

    def setup(self, cache):
        N = 10000
        self.unique_numeric_seconds = list(range(N))
        self.dup_numeric_seconds = [1000] * N
        self.dup_string_dates = ["2000-02-11"] * N
        self.dup_string_with_tz = ["2000-02-11 15:00:00-0800"] * N

    def time_unique_seconds_and_unit(self, cache):
        to_datetime(self.unique_numeric_seconds, unit="s", cache=cache)

    def time_dup_seconds_and_unit(self, cache):
        to_datetime(self.dup_numeric_seconds, unit="s", cache=cache)

    def time_dup_string_dates(self, cache):
        to_datetime(self.dup_string_dates, cache=cache)

    def time_dup_string_dates_and_format(self, cache):
        to_datetime(self.dup_string_dates, format="%Y-%m-%d", cache=cache)

    def time_dup_string_tzoffset_dates(self, cache):
        to_datetime(self.dup_string_with_tz, cache=cache)


class DatetimeAccessor:

    params = [None, "US/Eastern", "UTC", dateutil.tz.tzutc()]
    param_names = "tz"

    def setup(self, tz):
        N = 100000
        self.series = Series(date_range(start="1/1/2000", periods=N, freq="T", tz=tz))

    def time_dt_accessor(self, tz):
        self.series.dt

    def time_dt_accessor_normalize(self, tz):
        self.series.dt.normalize()

    def time_dt_accessor_month_name(self, tz):
        self.series.dt.month_name()

    def time_dt_accessor_day_name(self, tz):
        self.series.dt.day_name()

    def time_dt_accessor_time(self, tz):
        self.series.dt.time

    def time_dt_accessor_date(self, tz):
        self.series.dt.date

    def time_dt_accessor_year(self, tz):
        self.series.dt.year


from .pandas_vb_common import setup  # noqa: F401 isort:skip
