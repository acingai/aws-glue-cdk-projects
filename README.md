# AWS Glue CDK Project

## CSV Crawler

What do we need?

- S3 Bucket -> where we will upload our csv files
    - path: "s3://my-csv-bucket/csvs/"
- Glue Crawler -> crawl our S3 bucket

-> Let's have our `CSVCrawler` stack create these 2 resources together for us

Our resources are created. Let's go get our data now :)

I decided to work with the [`capital-bikeshare`](https://data.world/codefordc/capital-bikeshare) from `data.world`. I created a free account in order to download the dataset. The dataset was manually downloaded and unzipped.

## Resources

- [AWS CDK Workshop Python](https://cdkworkshop.com/30-python.html)
- [AWS CDK Python S3 API References](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_s3.html)
- [AWS CDK Python Glue CfnCrawler API References](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_glue/CfnCrawler.html)
- [AWS CDK Python Glue CfnCrawlerProps API References](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_glue/CfnCrawlerProps.html)
- [Stack Overflow Question 1](https://stackoverflow.com/questions/56434938/cdk-generating-empty-targets-for-cfncrawler)
