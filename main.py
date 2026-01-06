from google.cloud import storage

def main():
    client = storage.Client()
    bucket = client.bucket("my_bucket_anirutth")
    blob = bucket.blob("anirutth_data.csv.txt")

    csv_data = blob.download_as_text()
    print("CSV CONTENT:")
    print(csv_data)

if __name__ == "__main__":
    main()
