from aws_cdk import (
    aws_iam as iam,
    aws_s3 as s3,
    aws_glue as glue,
    core
)


class CsvCrawlerStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, 'csv-bucket')

        glue_role = iam.Role(
            self,
            'glue-role',
            assumed_by=iam.ServicePrincipal('glue.amazonaws.com'),
            managed_policies=[iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSGlueServiceRole'),
            iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3FullAccess')]
        )

        crawler = glue.CfnCrawler(
            self, 
            'csv-crawler', 
            role=glue_role.role_arn,
            database_name='csv_db',
            targets={
                's3Targets': [{"path": f"s3://{bucket.bucket_name}/csv/"}],
            }
        )
