# Command History

```sh
cdk init sample-app --language python

# take screenshot of project tree

source .venv/bin/activate
pip install --upgrade pip

pip install -r requirements.txt

pip install aws-cdk.aws-glue

# set up aws cli :)
λ  which aws
/usr/local/bin/aws

cdk ls

cdk deploy csv-crawler

λ  aws s3 ls  
2021-02-27 10:28:00 cdktoolkit-stagingbucket-1wdkn4be1gwgw
2021-02-27 10:32:37 csv-crawler-csvbuckete3c1c3b8-1kgq8cmtaf65h
...

λ  aws glue list-crawlers 
{
    "CrawlerNames": [
        "csvcrawler-K97ENFxAYqre"
    ]
}
```

List Packages:

```sh
pip list
Package                            Version Location
---------------------------------- ------- -------------------------------------------------------------------------
attrs                              20.3.0
aws-cdk.assets                     1.91.0
aws-cdk.aws-applicationautoscaling 1.91.0
aws-cdk.aws-autoscaling-common     1.91.0
aws-cdk.aws-cloudwatch             1.91.0
aws-cdk.aws-codeguruprofiler       1.91.0
aws-cdk.aws-ec2                    1.91.0
aws-cdk.aws-ecr                    1.91.0
aws-cdk.aws-ecr-assets             1.91.0
aws-cdk.aws-efs                    1.91.0
aws-cdk.aws-events                 1.91.0
aws-cdk.aws-iam                    1.91.0
aws-cdk.aws-kms                    1.91.0
aws-cdk.aws-lambda                 1.91.0
aws-cdk.aws-logs                   1.91.0
aws-cdk.aws-s3                     1.91.0
aws-cdk.aws-s3-assets              1.91.0
aws-cdk.aws-sns                    1.91.0
aws-cdk.aws-sns-subscriptions      1.91.0
aws-cdk.aws-sqs                    1.91.0
aws-cdk.aws-ssm                    1.91.0
aws-cdk.cloud-assembly-schema      1.91.0
aws-cdk.core                       1.91.0
aws-cdk.cx-api                     1.91.0
aws-cdk.region-info                1.91.0
cattrs                             1.1.2
constructs                         3.3.43
csv-crawler                        0.0.1   /home/johannes/Documents/src/aws-glue-cdk-project/csv_crawler/csv_crawler
iniconfig                          1.1.1
jsii                               1.22.0
packaging                          20.9
pip                                21.0.1
pluggy                             0.13.1
publication                        0.0.3
py                                 1.10.0
pyparsing                          2.4.7
pytest                             6.2.2
python-dateutil                    2.8.1
setuptools                         47.1.0
six                                1.15.0
toml                               0.10.2
typing-extensions                  3.7.4.3
```
