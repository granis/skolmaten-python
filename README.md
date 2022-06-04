# molskaten *also known as* skolmaten-python

Molskaten is a fork of skolmaten-python, my main purpose is to play around with ci/cd-stuff.

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/granis/skolmaten-python/master.svg)](https://results.pre-commit.ci/latest/github/granis/skolmaten-python/master)

This is a simple wrapper for the [skolmaten.se](https://skolmaten.se) service.

I wrote this becuase I needed a way to get the data for what I am going to eat in school for some stuff. So, why not publish it and help somebody else.

FOR NON-SWEDISH PEOPLE: [skolmaten.se](https://skolmaten.se) has data for what is going to be served in schools all over Sweden.

## Usage

```python

from molskaten import Molskaten

# You can find the id of your school by going to skolmaten.se, selecting your school, and looking in the address bar.
# For example this is what I see for polhemsskolan => https://skolmaten.se/polhemsskolan2/
schoolFood = Molskaten("polhemsskolan2")

weekly = schoolFood.getData()
print(weekly)

[{'date': datetime.datetime(2019, 10, 14, 0, 0), 'food': [u'Falukorv med potatismos', u'Potatisfrestelse med salladsost', u'ängsbiffar']}, ... {'date': datetime.datetime(2019, 10, 21, 0, 0), 'food': [u'Pastasås Arrabiata med linser och soltorkade tomater', u'Grönsakspaj']}]

```

## Todo

- [x] Basic weekly data.
- [ ] 100% Test coverage.
- [ ] Full documentation.
