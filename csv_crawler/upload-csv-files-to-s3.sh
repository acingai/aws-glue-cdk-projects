#!/usr/bin/env bash

# Upload CSV files to S3

echo "Uploading csv files to S3..."

# s3 bucket/path
s3_bucket="csv-crawler-csvbuckete3c1c3b8-1kgq8cmtaf65h"
s3_path="s3://${s3_bucket}/csv/"

# local dataset
current_dir=$(pwd)
data_set_dir="${current_dir}/data/codefordc-capital-bikeshare"

for file in $(ls $data_set_dir)
do
    echo "Uploading $file..."
    file_full_path="${data_set_dir}/${file}"
    # echo "${file_full_path}"

    # echo "aws s3 cp ${file_full_path} ${s3_path}"
    aws s3 cp ${file_full_path} ${s3_path}
done

# Verify
echo -e "\nVerify files on S3:"
aws s3 ls ${s3_path}

echo "Completed uploading csv files to S3!"
