from google.cloud import storage

BUCKET_NAME = "wagon-data-hack4nature"

def upload_to_gcp(filename, service_folder_name="unknow_source"):
	storage_location = f"{service_folder_name}/{filename}"
	local_model_filename = f"raw_data/{filename}"
	client = storage.Client()
	bucket = client.bucket(BUCKET_NAME)
	blob = bucket.blob(storage_location)
	blob.upload_from_filename(local_model_filename)
	return True

def download_from_gcp(filename, service_folder_name):
	storage_location = f"{service_folder_name}/{filename}"
	local_model_filename = file
	client = storage.Client()
	bucket = client.bucket(BUCKET_NAME)
	blob = bucket.blob(storage_location)
	blob.download_from_filename(local_model_filename)
	return True

def delete_from_gcp(filename, service_folder_name):
	storage_location = f"{service_folder_name}/{filename}"
	client = storage.Client()
	bucket = storage_client.bucket(BUCKET_NAME)
	blob = bucket.blob(storage_location)
	blob.delete()
	return True