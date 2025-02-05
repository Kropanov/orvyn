from os import path


def get_img_path(file_name: str) -> str:
    """Get the path to the image file."""
    return path.abspath(path.join("src", "desktop_ui", "assets", "img", file_name))
