import django_tables2 as tables
from django.utils.html import format_html


class ImageColumn(tables.Column):
    def render(self, value: list):
        images_html = ''
        for image_link in value:
            images_html += format_html(
                '<img src="{url}" class="zoom" height="60px", width="60px">',
                url=image_link
            )
        return format_html(images_html)


class MainTable(tables.Table):
    tail_number = tables.Column()
    serial_number = tables.Column()
    type_name = tables.Column(verbose_name="Type")
    year_of_production = tables.Column(
        verbose_name="Year",
        attrs={"td": {"width": "5%", "align": "center"}}
    )
    images = ImageColumn(attrs={"td": {"align": "center"}})

    class Meta:
        template_name = "django_tables2/bootstrap4.html"
        attrs = {
            "class": "table table-hover"
        }
        row_attrs = {
            "onClick": lambda record: "document.location.href='details/aircraft_id={0}';".format(record.get('aircraft_id'))
        }
