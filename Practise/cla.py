# Testing command line arguments
import sys
import argparse
print(sys.argv[1])
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="name of input image")
ap.add_argument("-s", "--scale", type=float, default=1.05)
ap.add_argument("-p", "--path", help="path to the input image")
args = vars(ap.parse_args())
print(args["image"])
print(args["path"])
print(args["scale"])
