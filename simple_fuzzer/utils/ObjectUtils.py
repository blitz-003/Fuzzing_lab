import hashlib
import pickle
import os


def dump_object(path, obj):
    """
    Serialize the given object and save it to the specified path.
    """
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)  # Create the directory if it doesn't exist
    
    with open(path, 'wb') as f:
        pickle.dump(obj, f)


def load_object(path: str):
    with open(path, 'rb') as f:
        return pickle.load(f)


def get_md5_of_object(obj):
    serialized_obj = pickle.dumps(obj)
    md5_hash = hashlib.md5()
    md5_hash.update(serialized_obj)
    return md5_hash.hexdigest()
