#!/bin/bash
up_dir=$(readlink -f ..)
data_dir=${up_dir}/challenges
sudo docker run --env-file .env -v $data_dir:/data -it advent
