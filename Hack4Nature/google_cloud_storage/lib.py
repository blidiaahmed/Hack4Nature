from google.cloud import storage

BUCKET_NAME = "wagon-data-hack4nature"
ORIGIN_DATA_FOLDER_NAME = "data_google_maps"
DATA_FOLDER_NAME = "labels"

def upload_to_gcp(file):
	storage_location = f"{ORIGIN_DATA_FOLDER_NAME}/{DATA_FOLDER_NAME}/{file}"
	local_model_filename = f"raw_data/{file}"
	client = storage.Client()
	bucket = client.bucket(BUCKET_NAME)
	blob = bucket.blob(storage_location)
	blob.upload_from_filename(local_model_filename)
	return True

def download_from_gcp(file):
	storage_location = f"{ORIGIN_DATA_FOLDER_NAME}/{DATA_FOLDER_NAME}/{file}"
	local_model_filename = file
	client = storage.Client()
	bucket = client.bucket(BUCKET_NAME)
	blob = bucket.blob(storage_location)
	blob.download_from_filename(local_model_filename)
	return True