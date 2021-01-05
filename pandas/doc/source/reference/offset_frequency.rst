{{ header }}

.. _api.dateoffsets:

============
Date offsets
============
.. currentmodule:: pandas.tseries.offsets

DateOffset
----------
.. autosummary::
   :toctree: api/

    DateOffset

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    DateOffset.freqstr
    DateOffset.kwds
    DateOffset.name
    DateOffset.nanos
    DateOffset.normalize
    DateOffset.rule_code
    DateOffset.n

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    DateOffset.apply
    DateOffset.apply_index
    DateOffset.copy
    DateOffset.isAnchored
    DateOffset.onOffset
    DateOffset.is_anchored
    DateOffset.is_on_offset
    DateOffset.__call__

BusinessDay
-----------

.. autosummary::
   :toctree: api/

    BusinessDay

Alias:

.. autosummary::
   :toctree: api/
   :template: autosummary/class_without_autosummary.rst

   BDay

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    BusinessDay.freqstr
    BusinessDay.kwds
    BusinessDay.name
    BusinessDay.nanos
    BusinessDay.normalize
    BusinessDay.rule_code
    BusinessDay.n
    BusinessDay.weekmask
    BusinessDay.holidays
    BusinessDay.calendar

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    BusinessDay.apply
    BusinessDay.apply_index
    BusinessDay.copy
    BusinessDay.isAnchored
    BusinessDay.onOffset
    BusinessDay.is_anchored
    BusinessDay.is_on_offset
    BusinessDay.__call__

BusinessHour
------------
.. autosummary::
   :toctree: api/

    BusinessHour

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    BusinessHour.freqstr
    BusinessHour.kwds
    BusinessHour.name
    BusinessHour.nanos
    BusinessHour.normalize
    BusinessHour.rule_code
    BusinessHour.n
    BusinessHour.start
    BusinessHour.end
    BusinessHour.weekmask
    BusinessHour.holidays
    BusinessHour.calendar

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    BusinessHour.apply
    BusinessHour.apply_index
    BusinessHour.copy
    BusinessHour.isAnchored
    BusinessHour.onOffset
    BusinessHour.is_anchored
    BusinessHour.is_on_offset
    BusinessHour.__call__

CustomBusinessDay
-----------------

.. autosummary::
   :toctree: api/

    CustomBusinessDay

Alias:

.. autosummary::
   :toctree: api/
   :template: autosummary/class_without_autosummary.rst

   CDay

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    CustomBusinessDay.freqstr
    CustomBusinessDay.kwds
    CustomBusinessDay.name
    CustomBusinessDay.nanos
    CustomBusinessDay.normalize
    CustomBusinessDay.rule_code
    CustomBusinessDay.n
    CustomBusinessDay.weekmask
    CustomBusinessDay.calendar
    CustomBusinessDay.holidays

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    CustomBusinessDay.apply_index
    CustomBusinessDay.apply
    CustomBusinessDay.copy
    CustomBusinessDay.isAnchored
    CustomBusinessDay.onOffset
    CustomBusinessDay.is_anchored
    CustomBusinessDay.is_on_offset
    CustomBusinessDay.__call__

CustomBusinessHour
------------------
.. autosummary::
   :toctree: api/

    CustomBusinessHour

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    CustomBusinessHour.freqstr
    CustomBusinessHour.kwds
    CustomBusinessHour.name
    CustomBusinessHour.nanos
    CustomBusinessHour.normalize
    CustomBusinessHour.rule_code
    CustomBusinessHour.n
    CustomBusinessHour.weekmask
    CustomBusinessHour.calendar
    CustomBusinessHour.holidays
    CustomBusinessHour.start
    CustomBusinessHour.end

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    CustomBusinessHour.apply
    CustomBusinessHour.apply_index
    CustomBusinessHour.copy
    CustomBusinessHour.isAnchored
    CustomBusinessHour.onOffset
    CustomBusinessHour.is_anchored
    CustomBusinessHour.is_on_offset
    CustomBusinessHour.__call__

MonthEnd
--------
.. autosummary::
   :toctree: api/

    MonthEnd

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    MonthEnd.freqstr
    MonthEnd.kwds
    MonthEnd.name
    MonthEnd.nanos
    MonthEnd.normalize
    MonthEnd.rule_code
    MonthEnd.n

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    MonthEnd.apply
    MonthEnd.apply_index
    MonthEnd.copy
    MonthEnd.isAnchored
    MonthEnd.onOffset
    MonthEnd.is_anchored
    MonthEnd.is_on_offset
    MonthEnd.__call__

MonthBegin
----------
.. autosummary::
   :toctree: api/

    MonthBegin

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    MonthBegin.freqstr
    MonthBegin.kwds
    MonthBegin.name
    MonthBegin.nanos
    MonthBegin.normalize
    MonthBegin.rule_code
    MonthBegin.n

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    MonthBegin.apply
    MonthBegin.apply_index
    MonthBegin.copy
    MonthBegin.isAnchored
    MonthBegin.onOffset
    MonthBegin.is_anchored
    MonthBegin.is_on_offset
    MonthBegin.__call__

BusinessMonthEnd
----------------

.. autosummary::
   :toctree: api/

    BusinessMonthEnd

Alias:

.. autosummary::
   :toctree: api/
   :template: autosummary/class_without_autosummary.rst

   BMonthEnd

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    BusinessMonthEnd.freqstr
    BusinessMonthEnd.kwds
    BusinessMonthEnd.name
    BusinessMonthEnd.nanos
    BusinessMonthEnd.normalize
    BusinessMonthEnd.rule_code
    BusinessMonthEnd.n

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    BusinessMonthEnd.apply
    BusinessMonthEnd.apply_index
    BusinessMonthEnd.copy
    BusinessMonthEnd.isAnchored
    BusinessMonthEnd.onOffset
    BusinessMonthEnd.is_anchored
    BusinessMonthEnd.is_on_offset
    BusinessMonthEnd.__call__

BusinessMonthBegin
------------------

.. autosummary::
   :toctree: api/

    BusinessMonthBegin

Alias:

.. autosummary::
   :toctree: api/
   :template: autosummary/class_without_autosummary.rst

   BMonthBegin

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    BusinessMonthBegin.freqstr
    BusinessMonthBegin.kwds
    BusinessMonthBegin.name
    BusinessMonthBegin.nanos
    BusinessMonthBegin.normalize
    BusinessMonthBegin.rule_code
    BusinessMonthBegin.n

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    BusinessMonthBegin.apply
    BusinessMonthBegin.apply_index
    BusinessMonthBegin.copy
    BusinessMonthBegin.isAnchored
    BusinessMonthBegin.onOffset
    BusinessMonthBegin.is_anchored
    BusinessMonthBegin.is_on_offset
    BusinessMonthBegin.__call__

CustomBusinessMonthEnd
----------------------

.. autosummary::
   :toctree: api/

    CustomBusinessMonthEnd

Alias:

.. autosummary::
   :toctree: api/
   :template: autosummary/class_without_autosummary.rst

   CBMonthEnd

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    CustomBusinessMonthEnd.freqstr
    CustomBusinessMonthEnd.kwds
    CustomBusinessMonthEnd.m_offset
    CustomBusinessMonthEnd.name
    CustomBusinessMonthEnd.nanos
    CustomBusinessMonthEnd.normalize
    CustomBusinessMonthEnd.rule_code
    CustomBusinessMonthEnd.n
    CustomBusinessMonthEnd.weekmask
    CustomBusinessMonthEnd.calendar
    CustomBusinessMonthEnd.holidays

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    CustomBusinessMonthEnd.apply
    CustomBusinessMonthEnd.apply_index
    CustomBusinessMonthEnd.copy
    CustomBusinessMonthEnd.isAnchored
    CustomBusinessMonthEnd.onOffset
    CustomBusinessMonthEnd.is_anchored
    CustomBusinessMonthEnd.is_on_offset
    CustomBusinessMonthEnd.__call__

CustomBusinessMonthBegin
------------------------

.. autosummary::
   :toctree: api/

    CustomBusinessMonthBegin

Alias:

.. autosummary::
   :toctree: api/
   :template: autosummary/class_without_autosummary.rst

   CBMonthBegin

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    CustomBusinessMonthBegin.freqstr
    CustomBusinessMonthBegin.kwds
    CustomBusinessMonthBegin.m_offset
    CustomBusinessMonthBegin.name
    CustomBusinessMonthBegin.nanos
    CustomBusinessMonthBegin.normalize
    CustomBusinessMonthBegin.rule_code
    CustomBusinessMonthBegin.n
    CustomBusinessMonthBegin.weekmask
    CustomBusinessMonthBegin.calendar
    CustomBusinessMonthBegin.holidays

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    CustomBusinessMonthBegin.apply
    CustomBusinessMonthBegin.apply_index
    CustomBusinessMonthBegin.copy
    CustomBusinessMonthBegin.isAnchored
    CustomBusinessMonthBegin.onOffset
    CustomBusinessMonthBegin.is_anchored
    CustomBusinessMonthBegin.is_on_offset
    CustomBusinessMonthBegin.__call__

SemiMonthEnd
------------
.. autosummary::
   :toctree: api/

    SemiMonthEnd

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    SemiMonthEnd.freqstr
    SemiMonthEnd.kwds
    SemiMonthEnd.name
    SemiMonthEnd.nanos
    SemiMonthEnd.normalize
    SemiMonthEnd.rule_code
    SemiMonthEnd.n
    SemiMonthEnd.day_of_month

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    SemiMonthEnd.apply
    SemiMonthEnd.apply_index
    SemiMonthEnd.copy
    SemiMonthEnd.isAnchored
    SemiMonthEnd.onOffset
    SemiMonthEnd.is_anchored
    SemiMonthEnd.is_on_offset
    SemiMonthEnd.__call__

SemiMonthBegin
--------------
.. autosummary::
   :toctree: api/

    SemiMonthBegin

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    SemiMonthBegin.freqstr
    SemiMonthBegin.kwds
    SemiMonthBegin.name
    SemiMonthBegin.nanos
    SemiMonthBegin.normalize
    SemiMonthBegin.rule_code
    SemiMonthBegin.n
    SemiMonthBegin.day_of_month

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    SemiMonthBegin.apply
    SemiMonthBegin.apply_index
    SemiMonthBegin.copy
    SemiMonthBegin.isAnchored
    SemiMonthBegin.onOffset
    SemiMonthBegin.is_anchored
    SemiMonthBegin.is_on_offset
    SemiMonthBegin.__call__

Week
----
.. autosummary::
   :toctree: api/

    Week

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    Week.freqstr
    Week.kwds
    Week.name
    Week.nanos
    Week.normalize
    Week.rule_code
    Week.n
    Week.weekday

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    Week.apply
    Week.apply_index
    Week.copy
    Week.isAnchored
    Week.onOffset
    Week.is_anchored
    Week.is_on_offset
    Week.__call__

WeekOfMonth
-----------
.. autosummary::
   :toctree: api/

    WeekOfMonth

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    WeekOfMonth.freqstr
    WeekOfMonth.kwds
    WeekOfMonth.name
    WeekOfMonth.nanos
    WeekOfMonth.normalize
    WeekOfMonth.rule_code
    WeekOfMonth.n
    WeekOfMonth.week

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    WeekOfMonth.apply
    WeekOfMonth.apply_index
    WeekOfMonth.copy
    WeekOfMonth.isAnchored
    WeekOfMonth.onOffset
    WeekOfMonth.is_anchored
    WeekOfMonth.is_on_offset
    WeekOfMonth.__call__
    WeekOfMonth.weekday

LastWeekOfMonth
---------------
.. autosummary::
   :toctree: api/

    LastWeekOfMonth

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    LastWeekOfMonth.freqstr
    LastWeekOfMonth.kwds
    LastWeekOfMonth.name
    LastWeekOfMonth.nanos
    LastWeekOfMonth.normalize
    LastWeekOfMonth.rule_code
    LastWeekOfMonth.n
    LastWeekOfMonth.weekday
    LastWeekOfMonth.week

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    LastWeekOfMonth.apply
    LastWeekOfMonth.apply_index
    LastWeekOfMonth.copy
    LastWeekOfMonth.isAnchored
    LastWeekOfMonth.onOffset
    LastWeekOfMonth.is_anchored
    LastWeekOfMonth.is_on_offset
    LastWeekOfMonth.__call__

BQuarterEnd
-----------
.. autosummary::
   :toctree: api/

    BQuarterEnd

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    BQuarterEnd.freqstr
    BQuarterEnd.kwds
    BQuarterEnd.name
    BQuarterEnd.nanos
    BQuarterEnd.normalize
    BQuarterEnd.rule_code
    BQuarterEnd.n
    BQuarterEnd.startingMonth

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    BQuarterEnd.apply
    BQuarterEnd.apply_index
    BQuarterEnd.copy
    BQuarterEnd.isAnchored
    BQuarterEnd.onOffset
    BQuarterEnd.is_anchored
    BQuarterEnd.is_on_offset
    BQuarterEnd.__call__

BQuarterBegin
-------------
.. autosummary::
   :toctree: api/

    BQuarterBegin

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    BQuarterBegin.freqstr
    BQuarterBegin.kwds
    BQuarterBegin.name
    BQuarterBegin.nanos
    BQuarterBegin.normalize
    BQuarterBegin.rule_code
    BQuarterBegin.n
    BQuarterBegin.startingMonth

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    BQuarterBegin.apply
    BQuarterBegin.apply_index
    BQuarterBegin.copy
    BQuarterBegin.isAnchored
    BQuarterBegin.onOffset
    BQuarterBegin.is_anchored
    BQuarterBegin.is_on_offset
    BQuarterBegin.__call__

QuarterEnd
----------
.. autosummary::
   :toctree: api/

    QuarterEnd

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    QuarterEnd.freqstr
    QuarterEnd.kwds
    QuarterEnd.name
    QuarterEnd.nanos
    QuarterEnd.normalize
    QuarterEnd.rule_code
    QuarterEnd.n
    QuarterEnd.startingMonth

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    QuarterEnd.apply
    QuarterEnd.apply_index
    QuarterEnd.copy
    QuarterEnd.isAnchored
    QuarterEnd.onOffset
    QuarterEnd.is_anchored
    QuarterEnd.is_on_offset
    QuarterEnd.__call__

QuarterBegin
------------
.. autosummary::
   :toctree: api/

    QuarterBegin

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    QuarterBegin.freqstr
    QuarterBegin.kwds
    QuarterBegin.name
    QuarterBegin.nanos
    QuarterBegin.normalize
    QuarterBegin.rule_code
    QuarterBegin.n
    QuarterBegin.startingMonth

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    QuarterBegin.apply
    QuarterBegin.apply_index
    QuarterBegin.copy
    QuarterBegin.isAnchored
    QuarterBegin.onOffset
    QuarterBegin.is_anchored
    QuarterBegin.is_on_offset
    QuarterBegin.__call__

BYearEnd
--------
.. autosummary::
   :toctree: api/

    BYearEnd

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    BYearEnd.freqstr
    BYearEnd.kwds
    BYearEnd.name
    BYearEnd.nanos
    BYearEnd.normalize
    BYearEnd.rule_code
    BYearEnd.n
    BYearEnd.month

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    BYearEnd.apply
    BYearEnd.apply_index
    BYearEnd.copy
    BYearEnd.isAnchored
    BYearEnd.onOffset
    BYearEnd.is_anchored
    BYearEnd.is_on_offset
    BYearEnd.__call__

BYearBegin
----------
.. autosummary::
   :toctree: api/

    BYearBegin

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    BYearBegin.freqstr
    BYearBegin.kwds
    BYearBegin.name
    BYearBegin.nanos
    BYearBegin.normalize
    BYearBegin.rule_code
    BYearBegin.n
    BYearBegin.month

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    BYearBegin.apply
    BYearBegin.apply_index
    BYearBegin.copy
    BYearBegin.isAnchored
    BYearBegin.onOffset
    BYearBegin.is_anchored
    BYearBegin.is_on_offset
    BYearBegin.__call__

YearEnd
-------
.. autosummary::
   :toctree: api/

    YearEnd

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    YearEnd.freqstr
    YearEnd.kwds
    YearEnd.name
    YearEnd.nanos
    YearEnd.normalize
    YearEnd.rule_code
    YearEnd.n
    YearEnd.month

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    YearEnd.apply
    YearEnd.apply_index
    YearEnd.copy
    YearEnd.isAnchored
    YearEnd.onOffset
    YearEnd.is_anchored
    YearEnd.is_on_offset
    YearEnd.__call__

YearBegin
---------
.. autosummary::
   :toctree: api/

    YearBegin

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    YearBegin.freqstr
    YearBegin.kwds
    YearBegin.name
    YearBegin.nanos
    YearBegin.normalize
    YearBegin.rule_code
    YearBegin.n
    YearBegin.month

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    YearBegin.apply
    YearBegin.apply_index
    YearBegin.copy
    YearBegin.isAnchored
    YearBegin.onOffset
    YearBegin.is_anchored
    YearBegin.is_on_offset
    YearBegin.__call__

FY5253
------
.. autosummary::
   :toctree: api/

    FY5253

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    FY5253.freqstr
    FY5253.kwds
    FY5253.name
    FY5253.nanos
    FY5253.normalize
    FY5253.rule_code
    FY5253.n
    FY5253.startingMonth
    FY5253.variation
    FY5253.weekday

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    FY5253.apply
    FY5253.apply_index
    FY5253.copy
    FY5253.get_rule_code_suffix
    FY5253.get_year_end
    FY5253.isAnchored
    FY5253.onOffset
    FY5253.is_anchored
    FY5253.is_on_offset
    FY5253.__call__

FY5253Quarter
-------------
.. autosummary::
   :toctree: api/

    FY5253Quarter

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    FY5253Quarter.freqstr
    FY5253Quarter.kwds
    FY5253Quarter.name
    FY5253Quarter.nanos
    FY5253Quarter.normalize
    FY5253Quarter.rule_code
    FY5253Quarter.n
    FY5253Quarter.qtr_with_extra_week
    FY5253Quarter.startingMonth
    FY5253Quarter.variation
    FY5253Quarter.weekday

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    FY5253Quarter.apply
    FY5253Quarter.apply_index
    FY5253Quarter.copy
    FY5253Quarter.get_rule_code_suffix
    FY5253Quarter.get_weeks
    FY5253Quarter.isAnchored
    FY5253Quarter.onOffset
    FY5253Quarter.is_anchored
    FY5253Quarter.is_on_offset
    FY5253Quarter.year_has_extra_week
    FY5253Quarter.__call__

Easter
------
.. autosummary::
   :toctree: api/

    Easter

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    Easter.freqstr
    Easter.kwds
    Easter.name
    Easter.nanos
    Easter.normalize
    Easter.rule_code
    Easter.n

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    Easter.apply
    Easter.apply_index
    Easter.copy
    Easter.isAnchored
    Easter.onOffset
    Easter.is_anchored
    Easter.is_on_offset
    Easter.__call__

Tick
----
.. autosummary::
   :toctree: api/

    Tick

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    Tick.delta
    Tick.freqstr
    Tick.kwds
    Tick.name
    Tick.nanos
    Tick.normalize
    Tick.rule_code
    Tick.n

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    Tick.copy
    Tick.isAnchored
    Tick.onOffset
    Tick.is_anchored
    Tick.is_on_offset
    Tick.__call__
    Tick.apply
    Tick.apply_index

Day
---
.. autosummary::
   :toctree: api/

    Day

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    Day.delta
    Day.freqstr
    Day.kwds
    Day.name
    Day.nanos
    Day.normalize
    Day.rule_code
    Day.n

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    Day.copy
    Day.isAnchored
    Day.onOffset
    Day.is_anchored
    Day.is_on_offset
    Day.__call__
    Day.apply
    Day.apply_index

Hour
----
.. autosummary::
   :toctree: api/

    Hour

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    Hour.delta
    Hour.freqstr
    Hour.kwds
    Hour.name
    Hour.nanos
    Hour.normalize
    Hour.rule_code
    Hour.n

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    Hour.copy
    Hour.isAnchored
    Hour.onOffset
    Hour.is_anchored
    Hour.is_on_offset
    Hour.__call__
    Hour.apply
    Hour.apply_index

Minute
------
.. autosummary::
   :toctree: api/

    Minute

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    Minute.delta
    Minute.freqstr
    Minute.kwds
    Minute.name
    Minute.nanos
    Minute.normalize
    Minute.rule_code
    Minute.n

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    Minute.copy
    Minute.isAnchored
    Minute.onOffset
    Minute.is_anchored
    Minute.is_on_offset
    Minute.__call__
    Minute.apply
    Minute.apply_index

Second
------
.. autosummary::
   :toctree: api/

    Second

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    Second.delta
    Second.freqstr
    Second.kwds
    Second.name
    Second.nanos
    Second.normalize
    Second.rule_code
    Second.n

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    Second.copy
    Second.isAnchored
    Second.onOffset
    Second.is_anchored
    Second.is_on_offset
    Second.__call__
    Second.apply
    Second.apply_index

Milli
-----
.. autosummary::
   :toctree: api/

    Milli

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    Milli.delta
    Milli.freqstr
    Milli.kwds
    Milli.name
    Milli.nanos
    Milli.normalize
    Milli.rule_code
    Milli.n

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    Milli.copy
    Milli.isAnchored
    Milli.onOffset
    Milli.is_anchored
    Milli.is_on_offset
    Milli.__call__
    Milli.apply
    Milli.apply_index

Micro
-----
.. autosummary::
   :toctree: api/

    Micro

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    Micro.delta
    Micro.freqstr
    Micro.kwds
    Micro.name
    Micro.nanos
    Micro.normalize
    Micro.rule_code
    Micro.n

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    Micro.copy
    Micro.isAnchored
    Micro.onOffset
    Micro.is_anchored
    Micro.is_on_offset
    Micro.__call__
    Micro.apply
    Micro.apply_index

Nano
----
.. autosummary::
   :toctree: api/

    Nano

Properties
~~~~~~~~~~
.. autosummary::
   :toctree: api/

    Nano.delta
    Nano.freqstr
    Nano.kwds
    Nano.name
    Nano.nanos
    Nano.normalize
    Nano.rule_code
    Nano.n

Methods
~~~~~~~
.. autosummary::
   :toctree: api/

    Nano.copy
    Nano.isAnchored
    Nano.onOffset
    Nano.is_anchored
    Nano.is_on_offset
    Nano.__call__
    Nano.apply
    Nano.apply_index

.. _api.frequencies:

===========
Frequencies
===========
.. currentmodule:: pandas.tseries.frequencies

.. _api.offsets:

.. autosummary::
   :toctree: api/

   to_offset
