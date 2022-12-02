- set LD library path in home directory; does **not** work if PascalX is in */SSD/scratch/rest_of_the_path*

    correct example (I added this line to *.bashrc*):
  ```
    export LD_LIBRARY_PATH="/SSD/home/hermione/PascalX/build/lib:$LD_LIBRARY_PATH"
  ```
- ref panel download command only works if run as a script; does not work directly in the terminal



    ex.
    ```
    #!/bin/bash

    cd /SSD/home/hermione/PascalX/misc/

    bash get1KGGRCh38.sh /HDD/data/andrea/ref_panel/ EUR 4 vcf

    ```

- in my case I had to `pip install fastnumbers` (the previous script failed at first)
  it would've been nice to check for missing dependencies before downloading all the files

- I also had to download those because the ref panel already downloaded in hermione did not work for me