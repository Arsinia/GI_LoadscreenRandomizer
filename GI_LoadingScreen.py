import os
import glob
import subprocess
from PIL import Image

# Define the configuration file
config_file = "config.txt"

# Read the configuration file
with open(config_file, 'r') as f:
    lines = f.read().splitlines()
    target_resolution = tuple(map(int, lines[0].split(',')))
    input_dir = lines[1]
    output_dir = lines[2]
    ini_file = lines[3]

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get a list of all images in the input directory
input_files = all_files = glob.glob(input_dir + '/**/*.*', recursive=True)
input_files = [file for file in input_files if '\\-' not in file]

output_files_dds = []

# Iterate over the input files
for input_file in input_files:

    should_refresh = True

    # Define the output file path
    output_file, ext = os.path.splitext(input_file)
    output_file = os.path.join(output_dir, os.path.basename(output_file))
    output_file_png = output_file + ".png"
    output_file_dds = output_file + ".dds"

    output_files_dds.append(output_file_dds)

    # Check if the output file already exists
    if os.path.isfile(output_file_dds):
        # Check if the input file has been modified since the output file was created
        input_mtime = os.path.getmtime(input_file)
        output_mtime = os.path.getmtime(output_file_dds)

        should_refresh = input_mtime >= output_mtime


    if should_refresh:
        # Open the image using PIL
        im = Image.open(input_file)

        # Crop and scale the image to fit the target resolution
        # Ugh why isn't there a function to do this garbage for me
        x_coeff = target_resolution[0] / im.width
        y_coeff = target_resolution[1] / im.height
        coeff = x_coeff if x_coeff > y_coeff else y_coeff
        im = im.resize((round(im.width * coeff), round(im.height * coeff)), Image.BICUBIC)
        left = (im.width - target_resolution[0]) / 2
        top = (im.height - target_resolution[1]) / 2
        right = (im.width + target_resolution[0]) / 2
        bottom = (im.height + target_resolution[1]) / 2
        im = im.crop((left, top, right, bottom))
        im = im.transpose(Image.FLIP_TOP_BOTTOM)

        # Save the output file
        im.save(output_file_png, 'PNG', srgb=False)
        subprocess.run(["texconv.exe", "-f", "BC7_UNORM", "-y", "-sepalpha", "-srgb", "-m", "1", "-o", output_dir, output_file_png])
        os.remove(output_file_png)


with open(ini_file, "r") as f:
    ini_lines = f.readlines()
with open(ini_file, "w") as f:
    for line in ini_lines:
        if line.startswith("global $n_imgs"):
            line = f"global $n_imgs = {len(input_files)}\n"
        f.write(line)
        if line.startswith(";BEGIN_SCRIPT_GENERATED_SECTION"):
            break

    for i in range(len(input_files)):
        f.write(f"else if $is_load_prev && $curr_img == {i}\n")
        f.write(f"	this = ResourceLS.{i}\n")
    f.write("endif\n")
    for i, output_file_dds in enumerate(output_files_dds):
        f.write(f"[ResourceLS.{i}]\n")
        output_file_dds_windows = output_file_dds.replace('/', '\\')
        f.write(f"filename = {output_file_dds_windows}\n")
