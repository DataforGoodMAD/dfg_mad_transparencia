from typing import Union
from datetime import datetime, timedelta
from click.types import DateTime
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import click


def run_crawler(start_urls) -> None:
    process = CrawlerProcess(get_project_settings())
    process.crawl(
        "boe_spider",
        domain="boe.es",
        start_urls=start_urls,
    )
    process.start()  # the script will block here until the crawling finishes


@click.group()
def cli():
    pass


@cli.command()
@click.argument("start_urls", nargs=-1)
def urls(start_urls="https://boe.es/diario_boe/ultimo.php"):
    run_crawler(start_urls)


def _build_urls(from_date: datetime, to_date: datetime):
    urls = []
    base_url = "https://boe.es/boe/dias"
    processing_date = from_date
    while processing_date < to_date:
        date_str = processing_date.strftime("%Y/%m/%d")
        urls.append(f"{base_url}/{date_str}")
        processing_date += timedelta(days=1)
    print(urls)
    return urls


@cli.command()
@click.option(
    "--from_date",
    "-f",
    required=True,
    type=click.DateTime(formats=["%Y-%m-%d"]),
    help="date to start searching. Format must be YYYY-MM-DD",
)
@click.option(
    "--to_date",
    "-t",
    required=True,
    type=click.DateTime(formats=["%Y-%m-%d"]),
    help="date to start searching. Format must be YYYY-MM-DD",
)
def calendar(from_date, to_date):
    start_urls = _build_urls(from_date, to_date)
    run_crawler(start_urls)


if __name__ == "__main__":
    cli()
