import nbformat
from nbconvert import HTMLExporter


def convert_notebook_to_html(notebook_path):
    with open(notebook_path, "r", encoding="utf-8") as file:
        notebook_content = nbformat.read(file, as_version=4)

    html_exporter = HTMLExporter()
    (body, resources) = html_exporter.from_notebook_node(notebook_content)

    output_path = notebook_path.replace(".ipynb", ".html")
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(body)


if __name__ == "__main__":
    notebook_path = (
        "fifa15-22_player_analysis.ipynb"  # Replace with your Jupyter Notebook filename
    )
    convert_notebook_to_html(notebook_path)
