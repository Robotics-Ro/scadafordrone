import pxr.Tf

# Try a different method to get the version, which might be more robust
try:
    print(f"pxr version (from module attributes): {pxr.Tf.GetVersionString()}")
except AttributeError:
    # If the function is truly missing, this block will be executed.
    # We can try to get the version from the main pxr module instead.
    print(f"pxr version (from core module): {pxr.Tf.TfGetVersionString()}")
