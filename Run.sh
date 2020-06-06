xhost local:root
docker run --network hw03 -p 1884:1884 -it -e DISPLAY=$DISPLAY --privileged -v /tmp:/tmp --rm --env QT_X11_NO_MITSHM=1 facedetector
