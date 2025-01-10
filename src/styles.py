def load_css(file_path):
    """
    Load CSS file and return its content as a Markdown string for Streamlit.

    Args:
        file_path (str): Path to the CSS file

    Returns:
        str: CSS content wrapped in HTML style tags
    """
    try:
        with open(file_path, 'r') as f:
            css_content = f.read()

        return f"""
        <style>
        {css_content}
        </style>
        """
    except FileNotFoundError:
        print(f"CSS file not found: {file_path}")
        return ""