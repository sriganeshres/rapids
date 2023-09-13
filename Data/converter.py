import gzip
import shutil

with gzip.open('../Data/gplus_combined.txt.gz', 'rb') as f_in:
    with open('../Data/gplus_combined.tar', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
