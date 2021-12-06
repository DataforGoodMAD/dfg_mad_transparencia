from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument(
    "start_urls",
    nargs=-1,
)
def urls(start_urls="https://boe.es/diario_boe/ultimo.php"):
    process = CrawlerProcess(get_project_settings())
    process.crawl(
        "boe_spider",
        domain="boe.es",
        start_urls=start_urls,
    )
    process.start()  # the script will block here until the crawling is finished


def _parse_interval():
    pass


def _build_urls(datetime_list):
    pass


@cli.command()
@click.argument(
    "from_to",
)
def calendar(from_to):
    from_str, to_str = from_to
    print(from_str, to_str)


if __name__ == "__main__":
    cli()
