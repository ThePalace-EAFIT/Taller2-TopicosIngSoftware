def build_public_url(bucket: str, region: str, key: str) -> str:

    bucket = bucket.strip()
    region = region.strip()
    key = key.lstrip("/")
    return f"https://{bucket}.s3.{region}.amazonaws.com/{key}"