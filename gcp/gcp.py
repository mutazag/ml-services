from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name)
    """Uploads a file to the bicket."""
    storage_client = storage.Client()