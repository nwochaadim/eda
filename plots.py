from pandas import read_csv
from matplotlib import pyplot
from pandas import Grouper
from pandas import DataFrame
from pandas import concat
series = read_csv('daily-minimum-temperatures.csv', header=0, index_col=0, parse_dates=True, squeeze=True)

## Simple Line Plot
series.plot()
pyplot.show()

## Changing Line Styles
series.plot(style="k.")
pyplot.show()

## Group by year and do a subplot
groups = series.groupby(Grouper(freq='A'))
years = DataFrame()
for name, group in groups:
    years[name.year] = group.values
years.plot(subplots=True, legend=False)
pyplot.show()

# Density plot similar to histogram but shows distribution better
series.plot(kind="kde")
pyplot.show()

# Box and whisker plots
groups = series.groupby(Grouper(freq='A'))
years = DataFrame()
for name, group in groups:
    years[name.year] = group.values
years.boxplot()
pyplot.show()

# Box and whisker plots per months of 1990
one_year = series['1990']
groups = one_year.groupby(Grouper(freq='M'))
months = concat([DataFrame({ name.month: group.values }) for name, group in groups], axis=1)
months = DataFrame(months)
months.columns = range(1,13)
months.boxplot()
pyplot.show()


# Heat maps
groups = series.groupby(Grouper(freq='A'))
years = DataFrame()
for name, group in groups:
	years[name.year] = group.values
years = years.T
pyplot.matshow(years, interpolation=None, aspect='auto')
pyplot.show()

# Lag Scatter plot
from pandas.plotting import lag_plot
series = read_csv('daily-minimum-temperatures.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
lag_plot(series)
pyplot.show()

# Auto correlation plot
from pandas.plotting import autocorrelation_plot
series = read_csv('daily-minimum-temperatures.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
autocorrelation_plot(series)
pyplot.show()
