# planetary-atmosphere-observations

This repository contains observations of planetary atmospheres. The observations are stored in `yaml` format. For example,

```yaml
# Some Titan observations
CH4:
- citation: Cui et al. (2009)
  DOI: 10.1016/j.icarus.2008.12.005
  notes: Table 3
  data:
  - {alt: 981, mix: 0.0131, mix-low: 0.013, mix-high: 0.0132}
  - {alt: 1025, mix: 0.0178, mix-low: 0.0177, mix-high: 0.0179}
  - {alt: 1077, mix: 0.022, mix-low: 0.0219, mix-high: 0.0221}
  - {alt: 1151, mix: 0.03, mix-low: 0.0299, mix-high: 0.0301}
- citation: Vuitton et al. (2006)
  DOI: 10.1086/507467
  notes: Table 1, column labeled "This Model"
  data:
  - {alt: 1100, mix: 3e-2}
```

`alt` is in kilometers, and `mix` is the mean mixing ratio at `alt`. `mix-low` and `mix-high` are the upper and lower bound uncertainty in the measurement. Upper and lower bounds in `alt` can be denoted with `alt-low`, and `alt-high`. For example, a data entry with both altitude and concentration uncertainty would look like the following.

```yaml
- {alt: 981, alt-low: 900, alt-high: 1000, mix: 0.0131, mix-low: 0.013, mix-high: 0.0132}
```

For gas giants, `alt` doesn't make any sense, because there is no defined surface. So, concentrations are given as a function of pressure in bars. For example,

```yaml
CH3:
- citation: Moses et al. (2000)
  DOI: 10.1006/icar.1999.6320
  notes: Table 1
  data:
  - {P: 2.0e-07, mix: 1e-7}
```

Every observation has a specific citation. We only consider how a species concentration changes over altitude, and ignore latitudinal/longitudinal variations.

I suggest parsing this data with a yaml parsing package such as [PyYAML](https://pyyaml.org/).