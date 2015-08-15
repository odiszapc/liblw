#! /bin/bash

gypGenerator=

# Load command-line arguments.
while [ "$1" != "" ]; do
    case $1 in
        -f | --format )
            shift
            gypGenerator=$1
            ;;
    esac
    shift
done

source scripts/common.sh
source scripts/install-all.sh
source scripts/run-gyp.sh

mkdir -p $BUILD_DIR         2>/dev/null
mkdir -p $DEPENDENCIES_DIR  2>/dev/null
mkdir -p $BIN_DIR           2>/dev/null

if install_all; then
    echo " -- All components installed."
else
    echo " !! Failed to install required components." 1>&2
fi

gypArgs="liblw.gyp --depth=. --generator-output=$BUILD_DIR -Goutput_dir=$BUILD_DIR"

if [ "$gypGenerator" != "" ]; then
    gypArgs="$gypArgs --format=$gypGenerator"
fi

# And then run gyp
run_gyp $gypArgs
