from google.cloud import storage

class GCP:
    def __init__(self):
        self.storage_client = storage.Client()

    def upload_to_gcs(self, bucket_name, local_file_path, destination_blob_name):
        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(local_file_path)
        print(f"File {local_file_path} uploaded to {destination_blob_name} in {bucket_name}.")

    def download_from_gcs(self, bucket_name, source_blob_name, destination_file_path):
        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_path)
        print(f"File {source_blob_name} downloaded to {destination_file_path}.")

