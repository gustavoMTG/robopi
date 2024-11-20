# check for updates
sudo apt-get update
sudo apt-get upgrade
# dependencies
sudo apt-get install build-essential cmake git unzip pkg-config \
    libjpeg-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev \
    libgtk2.0-dev libcanberra-gtk* libgtk-3-dev libgstreamer1.0-dev \
    gstreamer1.0-gtk3 libgstreamer-plugins-base1.0-dev gstreamer1.0-gl \
    libxvidcore-dev libx264-dev python3-dev python3-numpy python3-pip \
    libtbbmalloc2 libtbb-dev libdc1394-dev libv4l-dev v4l-utils \
    libopenblas-dev libatlas-base-dev libblas-dev liblapack-dev gfortran \
    libhdf5-dev libprotobuf-dev libgoogle-glog-dev libgflags-dev \
    protobuf-compiler

# ref: https://qengineering.eu/install-opencv-on-raspberry-64-os.html