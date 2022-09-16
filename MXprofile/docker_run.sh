#!/bin/bash

confirm() {
  echo -en "\n\nDo you agree to use AIC-IIOT [y/n]? "
  read REPLY
  case $REPLY in
    [Yy]) ;;
    [Nn]) exit 0 ;;
    *) confirm ;;
  esac
    REPLY=''
}

confirm


if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <image>"
    exit 2
fi

HERE=$(pwd) # Absolute path of current directory

user=`whoami`
uid=`id -u`
gid=`id -g`

#echo "$user $uid $gid"

IMAGE_NAME="${1:-$CPU_IMAGE_TAG}"


xclmgmt_driver="$(find /dev -name xclmgmt\*)"
docker_devices=""
for i in ${xclmgmt_driver} ;
do
  docker_devices+="--device=$i "
done

render_driver="$(find /dev/dri -name renderD\*)"
for i in ${render_driver} ;
do
  docker_devices+="--device=$i "
done

##############################

docker run \
  $docker_devices \
  -e USER=$user -e UID=$uid -e GID=$gid \
  -v /dev/shm:/dev/shm \
  -v $HERE:/workspace \
  -w /workspace \
  -it \
  --rm \
  --network=host \
  $IMAGE_NAME \
  bash

