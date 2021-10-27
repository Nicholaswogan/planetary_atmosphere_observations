# planetary-atmosphere-observations

This repository contains observations of planetary atmospheres. The observations are stored in `yaml` format. For example,

```yaml
# Some Titan observations
CH4:
- citation: Cui et al. (2009)
  DOI: 10.1016/j.icarus.2008.12.005
  notes: Table 3
  data:
    - {alt: 981, mean: 0.0131, low: 0.0130, high: 0.0132}
    - {alt: 1025, mean: 0.0178, low: 0.0177, high: 0.0179}
    - {alt: 1077, mean: 0.0220, low: 0.0219, high: 0.0221}
    - {alt: 1151, mean: 0.0300, low: 0.0299, high: 0.0301}
- citation: Vuitton et al. (2006)
  DOI: 10.1086/507467
  notes: Table 1, column labeled "This Model"
  data:
    - {alt: 1100, mean: 3e-2}
```

`alt` is in Kilometers, and `mean` is the mean mixing ratio at `alt`. `low` and `high` are the one standard deviation error in the measurement. Every observation has a specific citation. We only consider how a species concentration changes over altitude, and ignore latitudinal/longitudinal variations.

I suggest parsing this data with a yaml parsing package such as [PyYAML](https://pyyaml.org/).