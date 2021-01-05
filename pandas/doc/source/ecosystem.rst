:orphan:

.. _ecosystem:

{{ header }}

****************
pandas ecosystem
****************

Increasingly, packages are being built on top of pandas to address specific needs
in data preparation, analysis and visualization.
This is encouraging because it means pandas is not only helping users to handle
their data tasks but also that it provides a better starting point for developers to
build powerful and more focused data tools.
The creation of libraries that complement pandas' functionality also allows pandas
development to remain focused around it's original requirements.

This is an inexhaustive list of projects that build on pandas in order to provide
tools in the PyData space. For a list of projects that depend on pandas,
see the
`libraries.io usage page for pandas <https://libraries.io/pypi/pandas/usage>`_
or `search pypi for pandas <https://pypi.org/search/?q=pandas>`_.

We'd like to make it easier for users to find these projects, if you know of other
substantial projects that you feel should be on this list, please let us know.

.. _ecosystem.data_cleaning_and_validation:

Data cleaning and validation
----------------------------

`Pyjanitor <https://github.com/ericmjl/pyjanitor/>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pyjanitor provides a clean API for cleaning data, using method chaining.

`Engarde <https://engarde.readthedocs.io/en/latest/>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Engarde is a lightweight library used to explicitly state assumptions about your datasets
and check that they're *actually* true.

`pandas-path <https://github.com/drivendataorg/pandas-path/>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since Python 3.4, `pathlib <https://docs.python.org/3/library/pathlib.html>`_ has been
included in the Python standard library. Path objects provide a simple
and delightful way to interact with the file system. The pandas-path package enables the
Path API for pandas through a custom accessor ``.path``. Getting just the filenames from
a series of full file paths is as simple as ``my_files.path.name``. Other convenient operations like
joining paths, replacing file extensions, and checking if files exist are also available.

.. _ecosystem.stats:

Statistics and machine learning
-------------------------------

`pandas-tfrecords <https://pypi.org/project/pandas-tfrecords/>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Easy saving pandas dataframe to tensorflow tfrecords format and reading tfrecords to pandas.

`Statsmodels <https://www.statsmodels.org/>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Statsmodels is the prominent Python "statistics and econometrics library" and it has
a long-standing special relationship with pandas. Statsmodels provides powerful statistics,
econometrics, analysis and modeling functionality that is out of pandas' scope.
Statsmodels leverages pandas objects as the underlying data container for computation.

`sklearn-pandas <https://github.com/paulgb/sklearn-pandas>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use pandas DataFrames in your `scikit-learn <https://scikit-learn.org/>`__
ML pipeline.

`Featuretools <https://github.com/featuretools/featuretools/>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Featuretools is a Python library for automated feature engineering built on top of pandas. It excels at transforming temporal and relational datasets into feature matrices for machine learning using reusable feature engineering "primitives". Users can contribute their own primitives in Python and share them with the rest of the community.

`Compose <https://github.com/FeatureLabs/compose>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compose is a machine learning tool for labeling data and prediction engineering. It allows you to structure the labeling process by parameterizing prediction problems and transforming time-driven relational data into target values with cutoff times that can be used for supervised learning.

.. _ecosystem.visualization:

Visualization
-------------

`Altair <https://altair-viz.github.io/>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Altair is a declarative statistical visualization library for Python.
With Altair, you can spend more time understanding your data and its
meaning. Altair's API is simple, friendly and consistent and built on
top of the powerful Vega-Lite JSON specification. This elegant
simplicity produces beautiful and effective visualizations with a
minimal amount of code. Altair works with pandas DataFrames.


`Bokeh <https://bokeh.pydata.org>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bokeh is a Python interactive visualization library for large datasets that natively uses
the latest web technologies. Its goal is to provide elegant, concise construction of novel
graphics in the style of Protovis/D3, while delivering high-performance interactivity over
large data to thin clients.

`Pandas-Bokeh <https://github.com/PatrikHlobil/Pandas-Bokeh>`__ provides a high level API
for Bokeh that can be loaded as a native pandas plotting backend via

.. code:: python

    pd.set_option("plotting.backend", "pandas_bokeh")

It is very similar to the matplotlib plotting backend, but provides interactive
web-based charts and maps.


`Seaborn <https://seaborn.pydata.org>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Seaborn is a Python visualization library based on
`matplotlib <https://matplotlib.org>`__. It provides a high-level, dataset-oriented
interface for creating attractive statistical graphics. The plotting functions
in seaborn understand pandas objects and leverage pandas grouping operations
internally to support concise specification of complex visualizations. Seaborn
also goes beyond matplotlib and pandas with the option to perform statistical
estimation while plotting, aggregating across observations and visualizing the
fit of statistical models to emphasize patterns in a dataset.

`plotnine <https://github.com/has2k1/plotnine/>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hadley Wickham's `ggplot2 <https://ggplot2.tidyverse.org/>`__ is a foundational exploratory visualization package for the R language.
Based on `"The Grammar of Graphics" <https://www.cs.uic.edu/~wilkinson/TheGrammarOfGraphics/GOG.html>`__ it
provides a powerful, declarative and extremely general way to generate bespoke plots of any kind of data.
Various implementations to other languages are available.
A good implementation for Python users is `has2k1/plotnine <https://github.com/has2k1/plotnine/>`__.

`IPython vega <https://github.com/vega/ipyvega>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`IPython Vega <https://github.com/vega/ipyvega>`__ leverages `Vega
<https://github.com/trifacta/vega>`__ to create plots within Jupyter Notebook.

`Plotly <https://plot.ly/python>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Plotly’s <https://plot.ly/>`__ `Python API <https://plot.ly/python/>`__ enables interactive figures and web shareability. Maps, 2D, 3D, and live-streaming graphs are rendered with WebGL and `D3.js <https://d3js.org/>`__. The library supports plotting directly from a pandas DataFrame and cloud-based collaboration. Users of `matplotlib, ggplot for Python, and Seaborn <https://plot.ly/python/matplotlib-to-plotly-tutorial/>`__ can convert figures into interactive web-based plots. Plots can be drawn in `IPython Notebooks <https://plot.ly/ipython-notebooks/>`__ , edited with R or MATLAB, modified in a GUI, or embedded in apps and dashboards. Plotly is free for unlimited sharing, and has `cloud <https://plot.ly/product/plans/>`__, `offline <https://plot.ly/python/offline/>`__, or `on-premise <https://plot.ly/product/enterprise/>`__ accounts for private use.

`Qtpandas <https://github.com/draperjames/qtpandas>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Spun off from the main pandas library, the `qtpandas <https://github.com/draperjames/qtpandas>`__
library enables DataFrame visualization and manipulation in PyQt4 and PySide applications.

`D-Tale <https://github.com/man-group/dtale>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

D-Tale is a lightweight web client for visualizing pandas data structures. It
provides a rich spreadsheet-style grid which acts as a wrapper for a lot of
pandas functionality (query, sort, describe, corr...) so users can quickly
manipulate their data. There is also an interactive chart-builder using Plotly
Dash allowing users to build nice portable visualizations. D-Tale can be
invoked with the following command

.. code:: python

    import dtale

    dtale.show(df)

D-Tale integrates seamlessly with Jupyter notebooks, Python terminals, Kaggle
& Google Colab. Here are some demos of the `grid <http://alphatechadmin.pythonanywhere.com/>`__
and `chart-builder <http://alphatechadmin.pythonanywhere.com/charts/4?chart_type=surface&query=&x=date&z=Col0&agg=raw&cpg=false&y=%5B%22security_id%22%5D>`__.

`hvplot <https://hvplot.holoviz.org/index.html>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

hvPlot is a high-level plotting API for the PyData ecosystem built on `HoloViews <https://holoviews.org/>`__.
It can be loaded as a native pandas plotting backend via

.. code:: python

    pd.set_option("plotting.backend", "hvplot")

.. _ecosystem.ide:

IDE
------

`IPython <https://ipython.org/documentation.html>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IPython is an interactive command shell and distributed computing
environment. IPython tab completion works with pandas methods and also
attributes like DataFrame columns.

`Jupyter Notebook / Jupyter Lab <https://jupyter.org>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jupyter Notebook is a web application for creating Jupyter notebooks.
A Jupyter notebook is a JSON document containing an ordered list
of input/output cells which can contain code, text, mathematics, plots
and rich media.
Jupyter notebooks can be converted to a number of open standard output formats
(HTML, HTML presentation slides, LaTeX, PDF, ReStructuredText, Markdown,
Python) through 'Download As' in the web interface and ``jupyter convert``
in a shell.

pandas DataFrames implement ``_repr_html_`` and ``_repr_latex`` methods
which are utilized by Jupyter Notebook for displaying
(abbreviated) HTML or LaTeX tables. LaTeX output is properly escaped.
(Note: HTML tables may or may not be
compatible with non-HTML Jupyter output formats.)

See :ref:`Options and Settings <options>` and
:ref:`Available Options <options.available>`
for pandas ``display.`` settings.

`Quantopian/qgrid <https://github.com/quantopian/qgrid>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

qgrid is "an interactive grid for sorting and filtering
DataFrames in IPython Notebook" built with SlickGrid.

`Spyder <https://www.spyder-ide.org/>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Spyder is a cross-platform PyQt-based IDE combining the editing, analysis,
debugging and profiling functionality of a software development tool with the
data exploration, interactive execution, deep inspection and rich visualization
capabilities of a scientific environment like MATLAB or Rstudio.

Its `Variable Explorer <https://docs.spyder-ide.org/variableexplorer.html>`__
allows users to view, manipulate and edit pandas ``Index``, ``Series``,
and ``DataFrame`` objects like a "spreadsheet", including copying and modifying
values, sorting, displaying a "heatmap", converting data types and more.
pandas objects can also be renamed, duplicated, new columns added,
copied/pasted to/from the clipboard (as TSV), and saved/loaded to/from a file.
Spyder can also import data from a variety of plain text and binary files
or the clipboard into a new pandas DataFrame via a sophisticated import wizard.

Most pandas classes, methods and data attributes can be autocompleted in
Spyder's `Editor <https://docs.spyder-ide.org/editor.html>`__ and
`IPython Console <https://docs.spyder-ide.org/ipythonconsole.html>`__,
and Spyder's `Help pane <https://docs.spyder-ide.org/help.html>`__ can retrieve
and render Numpydoc documentation on pandas objects in rich text with Sphinx
both automatically and on-demand.


.. _ecosystem.api:

API
---

`pandas-datareader <https://github.com/pydata/pandas-datareader>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``pandas-datareader`` is a remote data access library for pandas (PyPI:``pandas-datareader``).
It is based on functionality that was located in ``pandas.io.data`` and ``pandas.io.wb`` but was
split off in v0.19.
See more in the  `pandas-datareader docs <https://pandas-datareader.readthedocs.io/en/latest/>`_:

The following data feeds are available:

 * Google Finance
 * Tiingo
 * Morningstar
 * IEX
 * Robinhood
 * Enigma
 * Quandl
 * FRED
 * Fama/French
 * World Bank
 * OECD
 * Eurostat
 * TSP Fund Data
 * Nasdaq Trader Symbol Definitions
 * Stooq Index Data
 * MOEX Data

`Quandl/Python <https://github.com/quandl/Python>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Quandl API for Python wraps the Quandl REST API to return
pandas DataFrames with timeseries indexes.

`Pydatastream <https://github.com/vfilimonov/pydatastream>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PyDatastream is a Python interface to the
`Refinitiv Datastream (DWS) <https://www.refinitiv.com/en/products/datastream-macroeconomic-analysis>`__
REST API to return indexed pandas DataFrames with financial data.
This package requires valid credentials for this API (non free).

`pandaSDMX <https://pandasdmx.readthedocs.io>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pandaSDMX is a library to retrieve and acquire statistical data
and metadata disseminated in
`SDMX <https://www.sdmx.org>`_ 2.1, an ISO-standard
widely used by institutions such as statistics offices, central banks,
and international organisations. pandaSDMX can expose datasets and related
structural metadata including data flows, code-lists,
and data structure definitions as pandas Series
or MultiIndexed DataFrames.

`fredapi <https://github.com/mortada/fredapi>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fredapi is a Python interface to the `Federal Reserve Economic Data (FRED) <https://fred.stlouisfed.org/>`__
provided by the Federal Reserve Bank of St. Louis. It works with both the FRED database and ALFRED database that
contains point-in-time data (i.e. historic data revisions). fredapi provides a wrapper in Python to the FRED
HTTP API, and also provides several convenient methods for parsing and analyzing point-in-time data from ALFRED.
fredapi makes use of pandas and returns data in a Series or DataFrame. This module requires a FRED API key that
you can obtain for free on the FRED website.

`dataframe_sql <https://github.com/zbrookle/dataframe_sql>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``dataframe_sql`` is a Python package that translates SQL syntax directly into
operations on pandas DataFrames. This is useful when migrating from a database to
using pandas or for users more comfortable with SQL looking for a way to interface
with pandas.


.. _ecosystem.domain:

Domain specific
---------------

`Geopandas <https://github.com/kjordahl/geopandas>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Geopandas extends pandas data objects to include geographic information which support
geometric operations. If your work entails maps and geographical coordinates, and
you love pandas, you should take a close look at Geopandas.

`xarray <https://github.com/pydata/xarray>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

xarray brings the labeled data power of pandas to the physical sciences by
providing N-dimensional variants of the core pandas data structures. It aims to
provide a pandas-like and pandas-compatible toolkit for analytics on multi-
dimensional arrays, rather than the tabular data for which pandas excels.


.. _ecosystem.io:

IO
--

`BCPandas <https://github.com/yehoshuadimarsky/bcpandas>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BCPandas provides high performance writes from pandas to Microsoft SQL Server,
far exceeding the performance of the native ``df.to_sql`` method. Internally, it uses
Microsoft's BCP utility, but the complexity is fully abstracted away from the end user.
Rigorously tested, it is a complete replacement for ``df.to_sql``.


.. _ecosystem.out-of-core:

Out-of-core
-------------

`Blaze <https://blaze.pydata.org/>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Blaze provides a standard API for doing computations with various
in-memory and on-disk backends: NumPy, pandas, SQLAlchemy, MongoDB, PyTables,
PySpark.

`Dask <https://dask.readthedocs.io/en/latest/>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dask is a flexible parallel computing library for analytics. Dask
provides a familiar ``DataFrame`` interface for out-of-core, parallel and distributed computing.

`Dask-ML <https://dask-ml.readthedocs.io/en/latest/>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dask-ML enables parallel and distributed machine learning using Dask alongside existing machine learning libraries like Scikit-Learn, XGBoost, and TensorFlow.

`Koalas <https://koalas.readthedocs.io/en/latest/>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Koalas provides a familiar pandas DataFrame interface on top of Apache Spark. It enables users to leverage multi-cores on one machine or a cluster of machines to speed up or scale their DataFrame code.

`Modin <https://github.com/modin-project/modin>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``modin.pandas`` DataFrame is a parallel and distributed drop-in replacement
for pandas. This means that you can use Modin with existing pandas code or write
new code with the existing pandas API. Modin can leverage your entire machine or
cluster to speed up and scale your pandas workloads, including traditionally
time-consuming tasks like ingesting data (``read_csv``, ``read_excel``,
``read_parquet``, etc.).

.. code:: python

    # import pandas as pd
    import modin.pandas as pd

    df = pd.read_csv("big.csv")  # use all your cores!

`Odo <http://odo.pydata.org>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Odo provides a uniform API for moving data between different formats. It uses
pandas own ``read_csv`` for CSV IO and leverages many existing packages such as
PyTables, h5py, and pymongo to move data between non pandas formats. Its graph
based approach is also extensible by end users for custom formats that may be
too specific for the core of odo.

`Pandarallel <https://github.com/nalepae/pandarallel>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pandarallel provides a simple way to parallelize your pandas operations on all your CPUs by changing only one line of code.
If also displays progress bars.

.. code:: python

    from pandarallel import pandarallel

    pandarallel.initialize(progress_bar=True)

    # df.apply(func)
    df.parallel_apply(func)


`Vaex <https://docs.vaex.io/>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Increasingly, packages are being built on top of pandas to address specific needs in data preparation, analysis and visualization. Vaex is a Python library for Out-of-Core DataFrames (similar to pandas), to visualize and explore big tabular datasets. It can calculate statistics such as mean, sum, count, standard deviation etc, on an N-dimensional grid up to a billion (10\ :sup:`9`) objects/rows per second. Visualization is done using histograms, density plots and 3d volume rendering, allowing interactive exploration of big data. Vaex uses memory mapping, zero memory copy policy and lazy computations for best performance (no memory wasted).

 * vaex.from_pandas
 * vaex.to_pandas_df

.. _ecosystem.extensions:

Extension data types
--------------------

pandas provides an interface for defining
:ref:`extension types <extending.extension-types>` to extend NumPy's type
system. The following libraries implement that interface to provide types not
found in NumPy or pandas, which work well with pandas' data containers.

`Cyberpandas`_
~~~~~~~~~~~~~~

Cyberpandas provides an extension type for storing arrays of IP Addresses. These
arrays can be stored inside pandas' Series and DataFrame.

`Pandas-Genomics`_
~~~~~~~~~~~~~~~~~~

Pandas-Genomics provides extension types and extension arrays for working with genomics data

`Pint-Pandas`_
~~~~~~~~~~~~~~

``Pint-Pandas <https://github.com/hgrecco/pint-pandas>`` provides an extension type for
storing numeric arrays with units. These arrays can be stored inside pandas'
Series and DataFrame. Operations between Series and DataFrame columns which
use pint's extension array are then units aware.

.. _ecosystem.accessors:

Accessors
---------

A directory of projects providing
:ref:`extension accessors <extending.register-accessors>`. This is for users to
discover new accessors and for library authors to coordinate on the namespace.

=============== ============ ==================================== ===============================================================
Library         Accessor     Classes                              Description
=============== ============ ==================================== ===============================================================
`cyberpandas`_  ``ip``       ``Series``                           Provides common operations for working with IP addresses.
`pdvega`_       ``vgplot``   ``Series``, ``DataFrame``            Provides plotting functions from the Altair_ library.
`pandas_path`_  ``path``     ``Index``, ``Series``                Provides `pathlib.Path`_ functions for Series.
`pint-pandas`_  ``pint``     ``Series``, ``DataFrame``            Provides units support for numeric Series and DataFrames.
`composeml`_    ``slice``    ``DataFrame``                        Provides a generator for enhanced data slicing.
`datatest`_     ``validate`` ``Series``, ``DataFrame``, ``Index`` Provides validation, differences, and acceptance managers.
=============== ============ ==================================== ===============================================================

.. _cyberpandas: https://cyberpandas.readthedocs.io/en/latest
.. _pdvega: https://altair-viz.github.io/pdvega/
.. _Altair: https://altair-viz.github.io/
.. _pandas-genomics: https://pandas-genomics.readthedocs.io/en/latest/
.. _pandas_path: https://github.com/drivendataorg/pandas-path/
.. _pathlib.Path: https://docs.python.org/3/library/pathlib.html
.. _pint-pandas: https://github.com/hgrecco/pint-pandas
.. _composeml: https://github.com/FeatureLabs/compose
.. _datatest: https://datatest.readthedocs.io/
