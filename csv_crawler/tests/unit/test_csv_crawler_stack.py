import json
import pytest

from aws_cdk import core
from csv_crawler.csv_crawler_stack import CsvCrawlerStack


def get_template():
    app = core.App()
    CsvCrawlerStack(app, "csv-crawler")
    return json.dumps(app.synth().get_stack("csv-crawler").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
