#!/usr/bin/env python3

from aws_cdk import core

from csv_crawler.csv_crawler_stack import CsvCrawlerStack


app = core.App()
CsvCrawlerStack(app, "csv-crawler", env={'region': 'us-west-2'})

app.synth()
