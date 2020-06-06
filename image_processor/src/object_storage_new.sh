
echo $ACCESS_KEY_ID:$SECRET_ACCESS_KEY > ~/.passwd-s3fs

chmod 600 ~/.passwd-s3fs

mkdir /mnt/s3test

s3fs face-detector-cos-standard-kb7 /mnt/s3test/ -o passwd_file=~/.passwd-s3fs -o url=http://s3.us-east.cloud-object-storage.appdomain.cloud/ -o use_path_request_style -o dbglevel=info

df -h

ls /mnt/s3test

cat ~/.passwd-s3fs

python3 picture_receiver.py

