from grafanalib.core import (
    CELSIUS_FORMAT, Dashboard, Graph, GridPos, Repeat, RowPanel, SHORT_FORMAT,
    Target, Template, Templating, YAxes, YAxis,
)

chip_template = Template(
    default="All", name="chip", label="Chip", query="label_values(chip)",
    includeAll=True)

template_list = [
    Template(
        default="", name="instance", label="Machine",
        query="label_values(instance)"),
    chip_template,
]


dashboard = Dashboard(
    title="Temperature",
    templating=Templating(template_list),
    panels=[
        RowPanel(
            title="New Row",
            gridPos=GridPos(h=1, w=24, x=0, y=8),
        ),
        Graph(
            title="$chip",
            dataSource="Prometheus",
            targets=[
                Target(
                    expr=(
                        "sensors_temp_input{" +
                        'instance="$instance",chip="$chip"}'
                    ),
                    legendFormat="{{feature}}",
                    refId="A"),
            ],
            repeat=Repeat("v", "chip"),
            yAxes=YAxes(
                YAxis(format=CELSIUS_FORMAT),
                YAxis(format=SHORT_FORMAT),
            ),
            gridPos=GridPos(h=10, w=24, x=0, y=9),
        ),
    ],
).auto_panel_ids()
