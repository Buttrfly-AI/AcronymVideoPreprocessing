nohup python load_videos.py --metadata vox-metadata.csv --format .mp4 --out_folder vox --workers 8 &

wait

nohup python crop_vox.py --workers 8 --device_ids 0 --format .mp4 --dataset_version 2