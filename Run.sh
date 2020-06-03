xhost local:root
docker run -e DISPLAY=$DISPLAY --privileged -v /tmp:/tmp --rm --env QT_X11_NO_MITSHM=1 facedetector
