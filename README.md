# life_line_chart
Generate ancestor and descendants (genealogy) chart. SVG export is supported.

## Getting started

Install the module and the requiredments. Open a gedcom file and generate a ancestor life line chart.

### Prerequisites

You will need a gedcom file. You can use the automatically generated one from the tests directory in this repository ([tests/autogenerated.ged]).

```python
from life_line_chart import DescendantGraph, AncestorGraph, get_gedcom_instance_container
individual_id = '@I249@'
graph = AncestorGraph(
    instance_container=lambda: get_gedcom_instance_container(
        'tests/autogenerated.ged'),
    formatting={'total_height': 800, 'vertical_step_size':20}
)
graph.set_chart_configuration({'root_individuals': [
    {'individual_id': individual_id, 'generations': 8}
]})
graph.update_chart()
graph.paint_and_save(individual_id, 'example_1.svg')


individual_id = '@I2@'
graph = DescendantGraph(
    instance_container=lambda: get_gedcom_instance_container(
        'tests/autogenerated.ged'),
    formatting={
        'total_height': 800,
        'vertical_step_size':50,
        'relative_line_thickness':0.3}
)
graph.set_chart_configuration({'root_individuals': [
    {'individual_id': individual_id, 'generations': 2}
]})
graph.update_chart()
graph.paint_and_save(individual_id, 'example_2.svg')
```

![example_1.svg](example_1.svg)
![example_2.svg](example_2.svg)




### Installing

[requirements.txt](requirements.txt)

Then you will need the following modules:
- svgwrite (i.e. pyparsing)
- pillow (for tests with photos)

```
pip install -r requirements.txt
```

### Building

```
python setup.py bdist_wheel
```

Automatically generating example gedcom files requires the module
- names

Building a wheel requires with setup.py requires:
- shutil
- glob
- setuptools
- distutils
- wheel

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

<!-- ## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc -->
