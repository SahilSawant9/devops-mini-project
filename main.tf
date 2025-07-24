provider "aws" {
  access_key                  = "test"
  secret_key                  = "test"
  region                      = "us-east-1"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
  s3_use_path_style           = true

  endpoints {
    s3 = "http://localhost:4566"
  }
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-terraform-bucket"
}
resource "aws_s3_bucket_object" "example" {
  bucket = aws_s3_bucket.my_bucket.bucket
  key    = "example.txt"
  source = "${path.module}/example.txt"
  etag   = filemd5("${path.module}/example.txt")
}
resource "aws_s3_bucket_object" "second" {
  bucket = aws_s3_bucket.my_bucket.bucket
  key    = "second.txt"
  source = "${path.module}/second.txt"
  etag   = filemd5("${path.module}/second.txt")
}
